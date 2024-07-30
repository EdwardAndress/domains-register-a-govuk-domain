from django.db import models
from django.core.validators import MinLengthValidator

from simple_history.models import HistoricalRecords
from .application import Application
from request_a_govuk_domain.request.models.review_choices import (
    RegistrarDetailsReviewChoices,
    DomainNameAvailabilityReviewChoices,
    RegistrantOrgReviewChoices,
    RegistrantPersonReviewChoices,
    RegistrantPermissionReviewChoices,
    PolicyExemptionReviewChoices,
    DomainNameRulesReviewChoices,
    RegistrantSeniorSupportReviewChoices,
    RegistryDetailsReviewChoices,
)

NOTES_MAX_LENGTH = 5000
NOTES_MIN_LENGTH = 1


# We've added simple-history to the dependencies but need to implement it,
# principally for this this class.
class Review(models.Model):
    """
    An extension of the Application class (has a one-to-one) relationship
    to hold details of the review carried out by the reviewing team. Each
    pair of Boolean/TextField fields represents something the reviewing
    team have to check or confirm before making a decision on the application.
    """

    application = models.OneToOneField(Application, on_delete=models.CASCADE)

    registrar_details = models.CharField(choices=RegistrarDetailsReviewChoices.choices)
    registrar_details_notes = models.TextField(
        max_length=NOTES_MAX_LENGTH, validators=[MinLengthValidator(NOTES_MIN_LENGTH)]
    )

    domain_name_availability = models.CharField(
        choices=DomainNameAvailabilityReviewChoices.choices
    )
    domain_name_availability_notes = models.TextField(
        max_length=NOTES_MAX_LENGTH, validators=[MinLengthValidator(NOTES_MIN_LENGTH)]
    )

    registrant_org = models.CharField(choices=RegistrantOrgReviewChoices.choices)
    registrant_org_notes = models.TextField(
        max_length=NOTES_MAX_LENGTH, validators=[MinLengthValidator(NOTES_MIN_LENGTH)]
    )

    registrant_person = models.CharField(choices=RegistrantPersonReviewChoices.choices)
    registrant_person_notes = models.TextField(
        max_length=NOTES_MAX_LENGTH, validators=[MinLengthValidator(NOTES_MIN_LENGTH)]
    )

    registrant_permission = models.CharField(
        choices=RegistrantPermissionReviewChoices.choices
    )
    registrant_permission_notes = models.TextField(
        max_length=NOTES_MAX_LENGTH, validators=[MinLengthValidator(NOTES_MIN_LENGTH)]
    )

    policy_exemption = models.CharField(
        choices=PolicyExemptionReviewChoices.choices,
        blank=True,
        null=True,
    )
    policy_exemption_notes = models.TextField(
        max_length=NOTES_MAX_LENGTH, blank=True, null=True
    )

    domain_name_rules = models.CharField(choices=DomainNameRulesReviewChoices.choices)
    domain_name_rules_notes = models.TextField(
        max_length=NOTES_MAX_LENGTH, validators=[MinLengthValidator(NOTES_MIN_LENGTH)]
    )

    registrant_senior_support = models.CharField(
        choices=RegistrantSeniorSupportReviewChoices.choices,
        blank=True,
        null=True,
    )
    registrant_senior_support_notes = models.TextField(
        max_length=NOTES_MAX_LENGTH, blank=True, null=True
    )

    registry_details = models.CharField(choices=RegistryDetailsReviewChoices.choices)
    registry_details_notes = models.TextField(
        max_length=NOTES_MAX_LENGTH, validators=[MinLengthValidator(NOTES_MIN_LENGTH)]
    )

    reason = models.TextField(
        max_length=NOTES_MAX_LENGTH, validators=[MinLengthValidator(NOTES_MIN_LENGTH)]
    )

    history = HistoricalRecords()

    def is_approvable(self) -> bool:
        if (
            self.registrar_details == RegistrarDetailsReviewChoices.APPROVE
            and self.domain_name_availability
            == DomainNameAvailabilityReviewChoices.APPROVE
            and self.registrant_org == RegistrantOrgReviewChoices.APPROVE
            and self.registrant_person == RegistrantPersonReviewChoices.APPROVE
            and (
                not self.application.written_permission_evidence
                or (
                    self.application.written_permission_evidence
                    and self.registrant_permission
                    == RegistrantPermissionReviewChoices.APPROVE
                )
            )
            and self.domain_name_rules == DomainNameRulesReviewChoices.APPROVE
            and self.registry_details == RegistryDetailsReviewChoices.APPROVE
        ):
            return True
        else:
            return False

    def is_rejectable(self):
        return True

    def __str__(self):
        return str(self.application)

    class Meta:
        default_related_name = "review"


class ReviewFormGuidance(models.Model):
    name = models.CharField()
    how_to = models.CharField()
