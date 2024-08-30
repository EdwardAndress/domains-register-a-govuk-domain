# Generated by Django 4.2.13 on 2024-08-13 11:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("request", "0013_merge_20240805_1025"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="status",
            field=models.CharField(
                choices=[
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                    ("in_progress", "In Progress"),
                    ("ready_2i", "Ready for 2i"),
                    ("more_information", "More Information"),
                    ("with_nac", "Currently with NAC"),
                    ("new", "New"),
                    ("duplicate_application", "Duplicate application"),
                    ("failed_confirmation_email", "Failed Confirmation Email"),
                    ("failed_decision_email", "Failed Decision Email"),
                ],
                default="new",
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="domain_name_availability",
            field=models.CharField(
                choices=[
                    (
                        "approve",
                        "Name is available and organisation has no existing third-level .gov.uk domain - approve",
                    ),
                    ("holding", "Name not available - on hold awaiting response"),
                    ("reject", "Name not available - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="domain_name_availability_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="domain_name_rules",
            field=models.CharField(
                choices=[
                    ("approve", "Meets domain naming rules - approve"),
                    (
                        "holding",
                        "Organisation already has a third-level .gov.uk domain - on hold awaiting response",
                    ),
                    (
                        "reject",
                        "Does not meet naming rules - reject unless minister/perm sec request",
                    ),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="domain_name_rules_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="policy_exemption",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="policy_exemption_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="reason",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrant_org",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrant_org_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrant_permission",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrant_permission_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrant_person",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrant_person_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrant_senior_support",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrant_senior_support_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrar_details",
            field=models.CharField(
                choices=[
                    (
                        "approve",
                        "Registrar's email address matches Registrar's recognised domain - approve",
                    ),
                    (
                        "reject",
                        "Registrar's email address does not match Registrar's recognised domain - reject",
                    ),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registrar_details_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registry_details",
            field=models.CharField(
                choices=[
                    ("approve", "Role and/or email address meet guidelines - approved"),
                    ("holding", "Need more info - on hold/awaiting response"),
                    (
                        "reject",
                        "Role and/or email address does not meet guidelines - reject",
                    ),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalreview",
            name="registry_details_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="domain_name_availability",
            field=models.CharField(
                choices=[
                    (
                        "approve",
                        "Name is available and organisation has no existing third-level .gov.uk domain - approve",
                    ),
                    ("holding", "Name not available - on hold awaiting response"),
                    ("reject", "Name not available - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="domain_name_availability_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="domain_name_rules",
            field=models.CharField(
                choices=[
                    ("approve", "Meets domain naming rules - approve"),
                    (
                        "holding",
                        "Organisation already has a third-level .gov.uk domain - on hold awaiting response",
                    ),
                    (
                        "reject",
                        "Does not meet naming rules - reject unless minister/perm sec request",
                    ),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="domain_name_rules_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="policy_exemption",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="policy_exemption_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="reason",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrant_org",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrant_org_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrant_permission",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrant_permission_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrant_person",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrant_person_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrant_senior_support",
            field=models.CharField(
                choices=[
                    ("approve", "Strong evidence exists - approve"),
                    ("holding", "Need more info - on hold, awaiting response"),
                    ("reject", "Insufficient evidence exists - reject"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrant_senior_support_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrar_details",
            field=models.CharField(
                choices=[
                    (
                        "approve",
                        "Registrar's email address matches Registrar's recognised domain - approve",
                    ),
                    (
                        "reject",
                        "Registrar's email address does not match Registrar's recognised domain - reject",
                    ),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registrar_details_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registry_details",
            field=models.CharField(
                choices=[
                    ("approve", "Role and/or email address meet guidelines - approved"),
                    ("holding", "Need more info - on hold/awaiting response"),
                    (
                        "reject",
                        "Role and/or email address does not meet guidelines - reject",
                    ),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="registry_details_notes",
            field=models.TextField(
                max_length=5000,
                null=True,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
    ]