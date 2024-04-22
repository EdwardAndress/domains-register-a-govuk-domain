import logging
import os
import uuid
from typing import List

from django.conf import settings
from django.core.exceptions import ValidationError

import clamd
from dotenv import load_dotenv
from notifications_python_client import NotificationsAPIClient

logger = logging.getLogger(__name__)

# Load environment values from .env file
load_dotenv()


def handle_uploaded_file(file):
    """
    How and where to save a file that the user has uploaded

    :param file: a File object
    :return: the name of the file as store on the server
    """

    _, file_extension = os.path.splitext(file.name)

    saved_filename = f"{uuid.uuid4()}{file_extension}"

    file_path = os.path.join(settings.MEDIA_ROOT, saved_filename)
    with open(file_path, "wb") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return saved_filename


def validate_file_infection(file):
    """
    Incoming file is sent to clamd for scanning.
    Raises a ValidationError
    """

    cd = clamd.ClamdNetworkSocket(settings.CLAMD_TCP_ADDR, settings.CLAMD_TCP_SOCKET)
    result = cd.instream(file)

    if result and result["stream"][0] == "FOUND":
        raise ValidationError("File is infected with malware.", code="infected")


def route_number(session_data: dict) -> dict[str, int]:
    route = {}
    registrant_type = session_data.get("registrant_type")
    if registrant_type is not None:
        if registrant_type in ["parish_council", "village_council"]:
            route["primary"] = 1
            if session_data.get("domain_confirmation") == "no":
                route["secondary"] = 12
        elif registrant_type in ["central_government", "ndpb"]:
            route["primary"] = 2
            domain_purpose = session_data.get("domain_purpose")
            if domain_purpose is not None:
                if domain_purpose in ["email-only"]:
                    route["secondary"] = 5
                    if session_data.get("minister") == "no":
                        route["tertiary"] = 8
                elif domain_purpose in ["website-email"]:
                    route["secondary"] = 7
                else:
                    route["secondary"] = 6
                    if session_data.get("written_permission") == "no":
                        route["tertiary"] = 9
        elif registrant_type in [
            "local_authority",
            "fire_service",
            "combined_authority",
            "pcc",
            "joint_authority",
            "joint_committee",
            "representing_psb",
            "representing_profession",
        ]:
            route["primary"] = 3
            if session_data.get("written_permission") == "no":
                route["secondary"] = 10
        else:
            route["primary"] = 4

    return route


def is_central_government(registrant_type: str) -> bool:
    """
    Check if the registrant type is Central Government or Non-departmental body
    Note: If above is True then registrant type will be considered as Central Government
    """
    return registrant_type in ["central_government", "ndpb"]


def add_to_session(form, request, field_names: List[str]) -> dict:
    """
    Common utility method to clean the list of fields and save them in the session. This is to save boilerplate code.

    :param form: form object
    :param request: request object
    :param field_names: list of field names to be cleaned and saved in the session

    :return: A tuple of cleaned field value and registration data
    """
    registration_data = request.session.get("registration_data", {})
    for field_name in field_names:
        field_value = form.cleaned_data[field_name]
        registration_data[field_name] = field_value
    request.session["registration_data"] = registration_data
    return registration_data


def add_value_to_session(request, field_name: str, field_value) -> None:
    registration_data = request.session.get("registration_data", {})
    registration_data[field_name] = field_value
    request.session["registration_data"] = registration_data


def remove_from_session(session, field_names: List[str]) -> dict:
    """
    Remove fields from a session, for instance when an uploaded
    file is removed
    """
    for field_name in field_names:
        if session["registration_data"].get(field_name) is not None:
            if field_name.endswith("uploaded_filename"):
                # remove the file associated
                file_path = os.path.join(
                    settings.MEDIA_ROOT, session["registration_data"].get(field_name)
                )
                if os.path.isfile(file_path):
                    os.remove(file_path)
            del session["registration_data"][field_name]

    return session["registration_data"]


def get_env_variable(key: str, default=None) -> str:
    """
    Utility to get the environment variable

    param: key - environment variable name in .env file
    param: default - default value if environment variable not found

    :return: value - environment variable value
    """
    return os.getenv(key, default)


def send_email(email_address: str, template_id: str, personalisation: dict) -> None:
    """
    Method to send email using Notify API

    param: email_address: Email address of the recipient
    param: template_id: Template id of the Email Template
    param: personalisation: Dictionary of Personalisation data
    """
    notify_api_key = get_env_variable("NOTIFY_API_KEY")
    # If api key is found then send email, else log that it was not found
    if notify_api_key:
        notifications_client = NotificationsAPIClient(notify_api_key)
        notifications_client.send_email_notification(
            email_address=email_address,
            template_id=template_id,
            personalisation=personalisation,
        )
    else:
        logger.info("Not sending email as Notify API key not found")
