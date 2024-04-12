# Generated by Django 4.2.11 on 2024-04-12 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                            ("Pending", "Pending"),
                        ],
                        default="Pending",
                        max_length=8,
                    ),
                ),
                ("domain_name", models.CharField(max_length=253)),
                ("written_permission_evidence", models.FileField(upload_to="")),
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
                ("registrant_org_exists", models.BooleanField(default=False)),
                ("registrant_org_exists_notes", models.TextField(max_length=500)),
                ("registrant_org_eligible", models.BooleanField(default=False)),
                ("registrant_org_eligible_notes", models.TextField(max_length=500)),
                ("registrant_person_id_confirmed", models.BooleanField(default=False)),
                (
                    "registrant_person_id_confirmed_notes",
                    models.TextField(max_length=500),
                ),
                (
                    "permission_signatory_role_confirmed",
                    models.BooleanField(default=False),
                ),
                (
                    "permission_signatory_role_confirmed_notes",
                    models.TextField(max_length=500),
                ),
                ("domain_name_validated", models.BooleanField(default=False)),
                ("domain_name_validated_notes", models.TextField(max_length=500)),
                ("gds_exemption_validated", models.BooleanField(null=True)),
                ("gds_exemption_validated_notes", models.TextField(max_length=500)),
                ("ministerial_request_validated", models.BooleanField(null=True)),
                (
                    "ministerial_request_validated_notes",
                    models.TextField(max_length=500),
                ),
                ("nac_appeal_validated", models.BooleanField(null=True)),
                ("nac_appeal_validated_notes", models.TextField(max_length=500)),
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
                                "Central government department or agency",
                                "Central Government",
                            ),
                            (
                                "Non-departmental body - also known as an arm's length body",
                                "Ndpb",
                            ),
                            ("Parish or community council", "Parish Council"),
                            (
                                "Town, county, borough, metropolitan or district council",
                                "Local Authority",
                            ),
                            ("Fire service", "Fire Service"),
                            ("Neighbourhood or village council", "Village Council"),
                            ("Combined or unitary authority", "Combined Authority"),
                            ("Police and Crime Commissioner", "Pcc"),
                            ("Joint Authority", "Joint Authority"),
                            ("Joint Committee", "Joint Committee"),
                            (
                                "Organisation representing a group of public sector bodies",
                                "Representing Psb",
                            ),
                            (
                                "Organisation representing a profession across public sector bodies",
                                "Representing Profession",
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
                ("registrant_org_exists", models.BooleanField(default=False)),
                ("registrant_org_exists_notes", models.TextField(max_length=500)),
                ("registrant_org_eligible", models.BooleanField(default=False)),
                ("registrant_org_eligible_notes", models.TextField(max_length=500)),
                ("registrant_person_id_confirmed", models.BooleanField(default=False)),
                (
                    "registrant_person_id_confirmed_notes",
                    models.TextField(max_length=500),
                ),
                (
                    "permission_signatory_role_confirmed",
                    models.BooleanField(default=False),
                ),
                (
                    "permission_signatory_role_confirmed_notes",
                    models.TextField(max_length=500),
                ),
                ("domain_name_validated", models.BooleanField(default=False)),
                ("domain_name_validated_notes", models.TextField(max_length=500)),
                ("gds_exemption_validated", models.BooleanField(null=True)),
                ("gds_exemption_validated_notes", models.TextField(max_length=500)),
                ("ministerial_request_validated", models.BooleanField(null=True)),
                (
                    "ministerial_request_validated_notes",
                    models.TextField(max_length=500),
                ),
                ("nac_appeal_validated", models.BooleanField(null=True)),
                ("nac_appeal_validated_notes", models.TextField(max_length=500)),
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
        migrations.CreateModel(
            name="CentralGovernmentAttributes",
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
                ("domain_purpose", models.CharField()),
                (
                    "ministerial_request_evidence",
                    models.FileField(blank=True, null=True, upload_to=""),
                ),
                (
                    "policy_exemption_evidence",
                    models.FileField(blank=True, null=True, upload_to=""),
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
                "default_related_name": "centralgovt",
            },
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
