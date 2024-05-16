# Generated by Django 4.2.11 on 2024-05-12 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import request_a_govuk_domain.request.models.storage_util
import simple_history.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("reference", models.CharField(max_length=17)),
                ("time_submitted", models.DateTimeField(auto_now_add=True)),
                ("time_decided", models.DateTimeField(null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                            ("in_progress", "In Progress"),
                            ("new", "New"),
                        ],
                        default="new",
                        max_length=11,
                    ),
                ),
                ("domain_name", models.CharField(max_length=253)),
                ("domain_purpose", models.CharField(blank=True, null=True)),
                (
                    "written_permission_evidence",
                    models.FileField(
                        storage=request_a_govuk_domain.request.models.storage_util.select_storage,
                        upload_to="",
                    ),
                ),
                (
                    "ministerial_request_evidence",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=request_a_govuk_domain.request.models.storage_util.select_storage,
                        upload_to="",
                    ),
                ),
                (
                    "policy_exemption_evidence",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=request_a_govuk_domain.request.models.storage_util.select_storage,
                        upload_to="",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Registrar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="ReviewFormGuidance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField()),
                ("how_to", models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "registrar_details",
                    models.CharField(
                        blank=True,
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
                (
                    "registrar_details_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "domain_name_availability",
                    models.CharField(
                        blank=True,
                        choices=[
                            (
                                "approve",
                                "Name is available and organisation has no existing third-level .gov.uk domain - approve",
                            ),
                            (
                                "holding",
                                "Name not available - on hold awaiting response",
                            ),
                            ("reject", "Name not available - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "domain_name_availability_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "registrant_org",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "registrant_org_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "registrant_person",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "registrant_person_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "registrant_permission",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "registrant_permission_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "policy_exemption",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "policy_exemption_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "domain_name_rules",
                    models.CharField(
                        blank=True,
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
                (
                    "domain_name_rules_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "registrant_senior_support",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "registrant_senior_support_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "application",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="request.application",
                    ),
                ),
            ],
            options={
                "default_related_name": "review",
            },
        ),
        migrations.CreateModel(
            name="RegistryPublishedPerson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField()),
                ("email_address", models.EmailField(max_length=320)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None
                    ),
                ),
                ("role", models.CharField()),
            ],
            options={
                "unique_together": {("email_address", "role")},
            },
        ),
        migrations.CreateModel(
            name="RegistrarPerson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField()),
                ("email_address", models.EmailField(max_length=320)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None
                    ),
                ),
                (
                    "registrar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="request.registrar",
                    ),
                ),
            ],
            options={
                "unique_together": {
                    ("name", "email_address", "phone_number", "registrar")
                },
            },
        ),
        migrations.CreateModel(
            name="RegistrantPerson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField()),
                ("email_address", models.EmailField(max_length=320)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "email_address", "phone_number")},
            },
        ),
        migrations.CreateModel(
            name="Registrant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            (
                                "central_government",
                                "Central government department or agency",
                            ),
                            (
                                "alb",
                                "Non-departmental body - also known as an arm's length body",
                            ),
                            ("parish_council", "Parish or community council"),
                            (
                                "local_authority",
                                "Town, county, borough, metropolitan or district council",
                            ),
                            ("fire_service", "Fire service"),
                            ("village_council", "Neighbourhood or village council"),
                            ("combined_authority", "Combined or unitary authority"),
                            ("pcc", "Police and crime commissioner"),
                            ("joint_authority", "Joint authority"),
                            ("joint_committee", "Joint committee"),
                            (
                                "psb_group",
                                "Organisation representing a group of public sector bodies",
                            ),
                            (
                                "psb_profession",
                                "Organisation representing a profession across public sector bodies",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "type")},
            },
        ),
        migrations.CreateModel(
            name="HistoricalReview",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "registrar_details",
                    models.CharField(
                        blank=True,
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
                (
                    "registrar_details_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "domain_name_availability",
                    models.CharField(
                        blank=True,
                        choices=[
                            (
                                "approve",
                                "Name is available and organisation has no existing third-level .gov.uk domain - approve",
                            ),
                            (
                                "holding",
                                "Name not available - on hold awaiting response",
                            ),
                            ("reject", "Name not available - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "domain_name_availability_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "registrant_org",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "registrant_org_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "registrant_person",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "registrant_person_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "registrant_permission",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "registrant_permission_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "policy_exemption",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "policy_exemption_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "domain_name_rules",
                    models.CharField(
                        blank=True,
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
                (
                    "domain_name_rules_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "registrant_senior_support",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Strong evidence exists - approve"),
                            ("holding", "Need more info - on hold, awaiting response"),
                            ("reject", "Insufficient evidence exists - reject"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "registrant_senior_support_notes",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "application",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="request.application",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical review",
                "verbose_name_plural": "historical reviews",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name="application",
            name="registrant_org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="request.registrant"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="registrant_person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="registrant_application",
                to="request.registrantperson",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="registrar_org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="request.registrar"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="registrar_person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="registrar_application",
                to="request.registrarperson",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="registry_published_person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="registry_published_application",
                to="request.registrypublishedperson",
            ),
        ),
    ]
