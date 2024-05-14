# Generated by Django 5.0.4 on 2024-05-03 12:41

import django.db.models.deletion
import iam.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_auto_20240501_1342"),
        ("iam", "0003_alter_folder_updated_at_alter_role_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appliedcontrol",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="asset",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="complianceassessment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="evidence",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="framework",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="project",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="referencecontrol",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="requirementassessment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="requirementnode",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="riskacceptance",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="riskassessment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="riskmatrix",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="riskscenario",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="threat",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.CreateModel(
            name="LoadedLibrary",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="published"),
                ),
                (
                    "ref_id",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Reference ID",
                    ),
                ),
                (
                    "locale",
                    models.CharField(
                        default="en", max_length=100, verbose_name="Locale"
                    ),
                ),
                (
                    "default_locale",
                    models.BooleanField(default=True, verbose_name="Default locale"),
                ),
                (
                    "provider",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Provider"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, null=True, verbose_name="Name"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "annotation",
                    models.TextField(blank=True, null=True, verbose_name="Annotation"),
                ),
                (
                    "urn",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="URN"
                    ),
                ),
                (
                    "copyright",
                    models.CharField(
                        blank=True, max_length=4096, null=True, verbose_name="Copyright"
                    ),
                ),
                ("version", models.IntegerField(verbose_name="Version")),
                (
                    "packager",
                    models.CharField(
                        blank=True,
                        help_text="Packager of the library",
                        max_length=100,
                        null=True,
                        verbose_name="Packager",
                    ),
                ),
                ("builtin", models.BooleanField(default=False)),
                ("objects_meta", models.JSONField()),
                (
                    "dependencies",
                    models.ManyToManyField(
                        blank=True, to="core.loadedlibrary", verbose_name="Dependencies"
                    ),
                ),
                (
                    "folder",
                    models.ForeignKey(
                        default=iam.models.Folder.get_root_folder,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_folder",
                        to="iam.folder",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("urn", "locale", "version")},
            },
        ),
        migrations.AlterField(
            model_name="framework",
            name="library",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="frameworks",
                to="core.loadedlibrary",
            ),
        ),
        migrations.AlterField(
            model_name="referencecontrol",
            name="library",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reference_controls",
                to="core.loadedlibrary",
            ),
        ),
        migrations.AlterField(
            model_name="riskmatrix",
            name="library",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="risk_matrices",
                to="core.loadedlibrary",
            ),
        ),
        migrations.AlterField(
            model_name="threat",
            name="library",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="threats",
                to="core.loadedlibrary",
            ),
        ),
        migrations.CreateModel(
            name="StoredLibrary",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="published"),
                ),
                (
                    "ref_id",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Reference ID",
                    ),
                ),
                (
                    "locale",
                    models.CharField(
                        default="en", max_length=100, verbose_name="Locale"
                    ),
                ),
                (
                    "default_locale",
                    models.BooleanField(default=True, verbose_name="Default locale"),
                ),
                (
                    "provider",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Provider"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, null=True, verbose_name="Name"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "annotation",
                    models.TextField(blank=True, null=True, verbose_name="Annotation"),
                ),
                (
                    "urn",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="URN"
                    ),
                ),
                (
                    "copyright",
                    models.CharField(
                        blank=True, max_length=4096, null=True, verbose_name="Copyright"
                    ),
                ),
                ("version", models.IntegerField(verbose_name="Version")),
                (
                    "packager",
                    models.CharField(
                        blank=True,
                        help_text="Packager of the library",
                        max_length=100,
                        null=True,
                        verbose_name="Packager",
                    ),
                ),
                ("builtin", models.BooleanField(default=False)),
                ("objects_meta", models.JSONField()),
                ("dependencies", models.JSONField(null=True)),
                ("is_obsolete", models.BooleanField(default=False)),
                ("is_loaded", models.BooleanField(default=False)),
                ("hash_checksum", models.CharField(max_length=64)),
                ("content", models.TextField()),
                (
                    "folder",
                    models.ForeignKey(
                        default=iam.models.Folder.get_root_folder,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_folder",
                        to="iam.folder",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("urn", "locale", "version")},
            },
        ),
        migrations.DeleteModel(
            name="Library",
        ),
    ]
