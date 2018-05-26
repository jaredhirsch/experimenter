# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("experiments", "0006_auto_20180221_1939")]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="risk_brand",
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name="experiment",
            name="risk_confidential",
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name="experiment",
            name="risk_fast_shipped",
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name="experiment",
            name="risk_partner_related",
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name="experiment",
            name="risk_release_population",
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name="experiment",
            name="risks",
            field=models.TextField(
                blank=True,
                default='If you answered yes to any of the above, your study is considered\n"High Risk" and will require an executive sponsor to sign off\nexplicitly in the bug and state the known risk.\n\nFor a high risk study, each of the following\nmust be provided and accounted for:\n\n\nFinal Experiment Design\nResponsible: Experiment owner\nAccountable: Shield Team\n\n\nPopulation Size\nResponsible: Experiment owner\nAccountable: SHIELD Team\n\n\nData Analysis\nResponsible: Assigned analyst\nAccountable: SHIELD Team\n\n\nLegal Sign-Off\nResponsible: Experiment owner\nAccountable: SHIELD\n\n\nShipping\nResponsible: Release Management\nAccountable: Shield Team\n\n\nRisk Matrix\nResponsible: Experiment owner\nAccountable: Shield Team\n    ',
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="experiment",
            name="testing",
            field=models.TextField(
                blank=True,
                default="QA Status of your code: Green, yellow, red.\n\n\nIf additional QA is required, provide a plan for\ntesting each branch of this study:\n    ",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="analysis",
            field=models.TextField(
                blank=True,
                default="What is the main effect you are looking for and what data will\nyou use to make these decisions? What metrics are you using to measure success\n\n\nWho is the owner of the data analysis for this study?\n\n\nDo you plan on surveying users at the end of the study? Yes/No.\nStrategy and Insights can help create surveys if needed\n    ",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="firefox_channel",
            field=models.CharField(
                choices=[
                    (None, "Firefox Channel"),
                    ("Nightly", "Nightly"),
                    ("Beta", "Beta"),
                    ("Release", "Release"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="firefox_version",
            field=models.CharField(
                choices=[
                    (None, "Firefox Version"),
                    ("55.0", "Firefox 55.0"),
                    ("56.0", "Firefox 56.0"),
                    ("57.0", "Firefox 57.0"),
                    ("58.0", "Firefox 58.0"),
                    ("59.0", "Firefox 59.0"),
                    ("60.0", "Firefox 60.0"),
                    ("61.0", "Firefox 61.0"),
                    ("62.0", "Firefox 62.0"),
                    ("63.0", "Firefox 63.0"),
                    ("64.0", "Firefox 64.0"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="objectives",
            field=models.TextField(
                blank=True,
                default="What is the objective of this study?  Explain in detail.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="pref_branch",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Firefox Pref Branch"),
                    ("default", "default"),
                    ("user", "user"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="pref_type",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Firefox Pref Type"),
                    ("boolean", "boolean"),
                    ("integer", "integer"),
                    ("string", "string"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="experiments",
                to="projects.Project",
            ),
        ),
    ]
