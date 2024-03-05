from django.shortcuts import redirect
from django.urls import reverse


class FormProgressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path != reverse("start") and not self.is_valid_progress(request):
            return redirect("start")  # Redirect to start page if progress is invalid
        return response

    def is_valid_progress(self, request):
        if request.session.get("registration_data") is None:
            print("FALSE: no reg data")
            return False
        for key in request.session.get("registration_data"):
            if key not in [
                "registrant_type",
                "registrant_full_name",
                "registrant_email_address",
                "registrar_organisation",
            ]:
                # A key in the session data is invalid. So go back to the beginning
                request.session["registration_data"] = {}
                print("FALSE: unknown reg data:", key)
                return False
        print("TRUE")
        return True
