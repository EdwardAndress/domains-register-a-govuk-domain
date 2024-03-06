import json
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import (
    NameForm,
    EmailForm,
    ExemptionForm,
    ExemptionUploadForm,
    RegistrarForm,
    ConfirmForm,
    RegistrantTypeForm,
    DomainPurposeForm,
    RegistrantForm,
)
from .models import RegistrationData
from django.views.generic.edit import FormView

from .utils import handle_uploaded_file


"""
Some views are example views, please modify remove as needed
"""


class NameView(FormView):
    template_name = "name.html"
    form_class = NameForm
    success_url = reverse_lazy("email")

    def form_valid(self, form):
        self.request.session["registration_data"] = {
            "registrant_full_name": form.cleaned_data["registrant_full_name"]
        }
        return super().form_valid(form)


class EmailView(FormView):
    template_name = "email.html"
    form_class = EmailForm
    success_url = reverse_lazy("registrant_type")

    def form_valid(self, form):
        registration_data = self.request.session.get("registration_data", {})
        registration_data["registrant_email_address"] = form.cleaned_data[
            "registrant_email_address"
        ]
        self.request.session["registration_data"] = registration_data
        return super().form_valid(form)


class RegistrantTypeView(FormView):
    template_name = "registrant_type.html"
    form_class = RegistrantTypeForm
    success_url = reverse_lazy("registrant")

    def form_valid(self, form):
        registration_data = self.request.session.get("registration_data", {})
        registration_data["registrant_type"] = form.cleaned_data["registrant_type"]
        self.request.session["registration_data"] = registration_data
        if form.cleaned_data["registrant_type"] == "none":
            self.success_url = reverse_lazy("registrant_type_fail")
        return super().form_valid(form)


class RegistrantTypeFailView(TemplateView):
    template_name = "registrant_type_fail.html"


class RegistrantView(FormView):
    template_name = "registrant.html"
    form_class = RegistrantForm
    success_url = reverse_lazy("written_permission")

    def form_valid(self, form):
        registration_data = self.request.session.get("registration_data", {})
        registration_data["registrant_organisation_name"] = form.cleaned_data[
            "registrant_organisation_name"
        ]
        self.request.session["registration_data"] = registration_data
        if registration_data["registrant_type"] == "central_gov":
            self.success_url = reverse_lazy("domain_purpose")
        return super().form_valid(form)


class ConfirmView(FormView):
    template_name = "confirm.html"
    form_class = ConfirmForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Access session data and include it in the context
        registration_data = self.request.session.get("registration_data", {})
        context["registration_data"] = registration_data

        return context

    def form_valid(self, form):
        registration_data = self.request.session.get("registration_data", {})

        # Save data to the database
        RegistrationData.objects.create(
            registrant_full_name=registration_data["registrant_full_name"],
            registrant_email_address=registration_data["registrant_email_address"],
        )

        # Clear session data after saving
        self.request.session.pop("registration_data", None)

        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "success.html"


class ExemptionView(FormView):
    template_name = "exemption.html"
    form_class = ExemptionForm

    def form_valid(self, form):
        exe_radio = form.cleaned_data["exe_radio"]
        exe_radio = dict(form.fields["exe_radio"].choices)[exe_radio]
        if exe_radio == "Yes":
            self.success_url = reverse_lazy("exemption_upload")
        else:
            self.success_url = reverse_lazy("exemption_fail")
        return super().form_valid(form)


class ExemptionUploadView(FormView):
    template_name = "exemption_upload.html"

    def get(self, request):
        form = ExemptionUploadForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        """
        If the file is an image we encode using base64
        ex: b64encode(form.cleaned_data['file'].read()).decode('utf-8')
        If the file is a pdf we do not encode
        """
        form = ExemptionUploadForm(request.POST, request.FILES)

        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return render(
                request,
                "exemption_upload_confirm.html",
                {"file": request.FILES["file"]},
            )
        return render(request, self.template_name, {"form": form})


class ExemptionFailView(FormView):
    template_name = "exemption_fail.html"

    def get(self, request):
        return render(request, self.template_name)


class RegistrarView(FormView):
    template_name = "registrar.html"
    form_class = RegistrarForm
    success_url = reverse_lazy("email")

    def form_valid(self, form):
        self.request.session["registration_data"] = {
            "registrar_organisation": form.cleaned_data["organisations_choice"]
        }
        return super().form_valid(form)


class DomainPurposeView(FormView):
    template_name = "domain_purpose.html"
    form_class = DomainPurposeForm

    def form_valid(self, form):
        purpose = form.cleaned_data["domain_purpose"]
        registration_data = self.request.session.get("registration_data", {})
        registration_data["domain_purpose"] = purpose
        self.request.session["registration_data"] = registration_data

        if purpose == "email-only":
            self.success_url = reverse_lazy("written_permission")
        elif purpose == "website-email":
            self.success_url = reverse_lazy("exemption")
        else:
            self.success_url = reverse_lazy("domain_purpose_fail")

        return super().form_valid(form)


class DomainPurposeFailView(FormView):
    template_name = "domain_purpose_fail.html"

    def get(self, request):
        return render(request, self.template_name)


def answers_context_processor(request):
    """Temporary for ease of development: This sends the "answers" object to each form
    so we can display the data collected so far on every page"""
    answers = request.session.get("registration_data", {})
    answers_json = json.dumps(answers, indent=4)
    return {"answers": answers_json}
