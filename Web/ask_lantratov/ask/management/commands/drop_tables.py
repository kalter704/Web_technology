# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from django.db import connection

class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
		cursor = connection.cursor()
		cursor.execute("DROP TABLE auth_user_groups;")
		cursor.execute("DROP TABLE auth_user_user_permissions;")
		cursor.execute("DROP TABLE auth_group_permissions;")
		cursor.execute("DROP TABLE auth_group;")
		cursor.execute("DROP TABLE auth_permission;")
		cursor.execute("DROP TABLE django_admin_log;")
		cursor.execute("DROP TABLE auth_user;")
		cursor.execute("DROP TABLE django_migrations;")
		cursor.execute("DROP TABLE django_content_type;")
		cursor.execute("DROP TABLE django_session;")
