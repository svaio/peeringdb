# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 14:54


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0009_rename_json_member_list_field"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ixlan",
            old_name="ixf_member_export_url",
            new_name="ixf_ixp_member_list_url",
        ),
    ]
