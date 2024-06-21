import concurrent
import functools
from concurrent.futures import ThreadPoolExecutor
from typing import Any
from unittest.mock import Mock

from django.db import connection
from django.test import TransactionTestCase

from request_a_govuk_domain.request.models import Registrar, Application
from request_a_govuk_domain.request.views import SuccessView


def release_connection(wrapped_function):
    # Decorator to release connection at the end.
    # This should be usd to wrap the function that runs in a thread.
    # There is a Django issue, that does not cose the connection if used within a thread pool
    # https://stackoverflow.com/questions/44802617/database-is-being-accessed-by-other-users-error-when-using-threadpoolexecutor
    # https://james.lin.net.nz/2016/04/22/make-sure-you-are-closing-the-db-connections-after-accessing-django-orm-in-your-threads/
    #
    @functools.wraps(wrapped_function)
    def _release_connection(*args, **kwargs) -> Any:
        try:
            return wrapped_function(*args, **kwargs)
        finally:
            connection.close()

    return _release_connection


class ServiceFailureErrorHandlerTests(TransactionTestCase):
    def setUp(self):
        self.registrar = Registrar.objects.create(name="dummy registrar")
        self.registration_data = {
            "registrant_type": "parish_council",
            "domain_name": "test.domain.gov.uk",
            "registrar_name": "dummy registrar",
            "registrar_email": "dummy_registrar_email@gov.uk",
            "registrar_phone": "23456789",
            "registrar_organisation": f"{self.registrar.name}-{self.registrar.id}",
            "registrant_organisation": "dummy org",
            "registrant_full_name": "dummy user",
            "registrant_phone": "012345678",
            "registrant_email": "dummy@test.gov.uk",
            "registrant_role": "dummy",
            "registrant_contact_email": "dummy@test.gov.uk",
        }

    def test_application_submit_not_saved_if_no_token_in_session(self):
        """
        If the token in the url does not match the one in the session or
        if there is no token in the session, then application save is not attempted.
        :return:
        """
        s = self.client.session
        s.update(
            {
                "token": "GOVUK20062024QTLX",
            }
        )
        s.save()
        with self.assertLogs() as ctx_:
            self.assertEqual("GOVUK20062024QTLX", self.client.session.get("token"))
            res = self.client.get("/success/GOVUK20062024QTLV/")
            self.assertNotIn(
                "INFO:request_a_govuk_domain.request.views:Saving application GOVUK20062024QTLV",
                ctx_.output,
            )
            self.assertEqual(200, res.status_code)
        self.assertIsNone(self.client.session.get("token"))

    def test_application_submit_saved_if_tokens_match(self):
        """
        If the token in the url does matches the one in the session,
        then application saved.
        :return:
        """
        s = self.client.session
        s.update(
            {"token": "GOVUK20062024QTLV", "registration_data": self.registration_data}
        )
        s.save()
        with self.assertLogs() as ctx_:
            self.assertEqual("GOVUK20062024QTLV", self.client.session.get("token"))
            res = self.client.get("/success/GOVUK20062024QTLV/")
            self.assertIn(
                "INFO:request_a_govuk_domain.request.views:Saving application GOVUK20062024QTLV",
                ctx_.output,
            )
            self.assertEqual(200, res.status_code)
            self.assertEqual(1, Application.objects.count())
        self.assertIsNone(self.client.session.get("token"))

    def test_application_submit_only_saved_once_on_concurrent_submits(self):
        """
        Make sure we only create one application in the database even if the user sends multiple
        concurrent submits - multiple click on submit button
        :return:
        """

        @release_connection
        def make_request():
            class SessionDict(dict):
                def __init__(self, *k, **kwargs):
                    self.__dict__ = self
                    super().__init__(*k, **kwargs)
                    self.session_key = "session-key"

            mock_request = Mock()
            mock_request.session = SessionDict(
                {
                    "token": "GOVUK20062024QTLG",
                    "registration_data": self.registration_data,
                }
            )
            res = SuccessView().get(mock_request, "GOVUK20062024QTLG")
            self.assertEqual(200, res.status_code)

        num_threads = 5
        with ThreadPoolExecutor() as executor:
            features = [executor.submit(make_request) for i in range(num_threads)]
            concurrent.futures.wait(features)

        self.assertEqual(1, Application.objects.count())
        self.assertIsNone(self.client.session.get("token"))
