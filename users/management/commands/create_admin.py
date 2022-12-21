from django.core.management import base, CommandError
from django.utils.crypto import get_random_string
from users.models import User
import ipdb


class Command(base.BaseCommand):
    help = "Create user admin"

    def add_arguments(self, parser):
        parser.add_argument("--username", "-u", type=str, help="inform the username")
        parser.add_argument("--password", "-p", type=str, help="inform the password")
        parser.add_argument("--email", "-e", type=str, help="inform the email")

    def handle(self, *args, **options):
        email = options.get("email")
        password = options.get("password")
        username = options.get("username")

        user_admin = {
            "email": "admin@example.com",
            "password": "admin1234",
            "username": "admin",
        }

        if email:
            user_admin["email"] = email

        if password:
            user_admin["password"] = password

        if username:
            user_admin["username"] = username
            if not email:
                user_admin["email"] = username + "@example.com"

        email_exists = User.objects.filter(email=email).exists()
        username_exists = User.objects.filter(username=username).exists()

        if email_exists:
            raise CommandError(f"Email `{user_admin['email']}` already taken.")
        if username_exists:
            raise CommandError(f"Username `{user_admin['username']}` already taken.")

        User.objects.create_superuser(**user_admin)

        self.stdout.write(
            self.style.SUCCESS(
                f"Admin `{user_admin['username']}` successfully created!"
            )
        )
