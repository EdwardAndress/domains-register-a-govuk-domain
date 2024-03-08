"""
URL configuration for request_a_govuk_domain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .request.views import (
    NameView,
    EmailView,
    ConfirmView,
    SuccessView,
    ExemptionView,
    ExemptionUploadView,
    ExemptionFailView,
    RegistrarView,
    RegistrantTypeView,
    RegistrantTypeFailView,
    DomainView,
    DomainPurposeView,
    DomainPurposeFailView,
    RegistrantView,
    MinisterView,
    ApplicantDetailsView,
    RegistrantDetailsView,
    RegistryDetailsView,
    WrittenPermissionView,
    WrittenPermissionFailView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RegistrarView.as_view(), name="start"),
    path("name/", NameView.as_view(), name="name"),
    path("email/", EmailView.as_view(), name="email"),
    path("domain/", DomainView.as_view(), name="domain"),
    path("registrant_type/", RegistrantTypeView.as_view(), name="registrant_type"),
    path(
        "registrant_type_fail/",
        RegistrantTypeFailView.as_view(),
        name="registrant_type_fail",
    ),
    path("registrant/", RegistrantView.as_view(), name="registrant"),
    path("confirm/", ConfirmView.as_view(), name="confirm"),
    path("success/", SuccessView.as_view(), name="success"),
    path("exemption/", ExemptionView.as_view(), name="exemption"),
    path("exemption_upload/", ExemptionUploadView.as_view(), name="exemption_upload"),
    path("exemption_fail/", ExemptionFailView.as_view(), name="exemption_fail"),
    path("registrar/", RegistrarView.as_view(), name="registrar"),
    path("domain_purpose/", DomainPurposeView.as_view(), name="domain_purpose"),
    path(
        "domain_purpose_fail/",
        DomainPurposeFailView.as_view(),
        name="domain_purpose_fail",
    ),
    path("minister/", MinisterView.as_view(), name="domain_purpose"),
    path(
        "applicant_details/",
        ApplicantDetailsView.as_view(),
        name="applicant_details",
    ),
    path(
        "registrant_details/",
        RegistrantDetailsView.as_view(),
        name="registrant_details",
    ),
    path(
        "registry_details/",
        RegistryDetailsView.as_view(),
        name="registry_details",
    ),
    path(
        "written-permission/",
        WrittenPermissionView.as_view(),
        name="written_permission",
    ),
    path(
        "written-permission-fail/",
        WrittenPermissionFailView.as_view(),
        name="written_permission_fail",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
