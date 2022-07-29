from http.client import HTTPException
from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Make simple migrations'

    def handle(self, *args, **kwargs):
        make_migrations = ["python", "manage.py", "makemigrations"]
        migrate = ["python", "manage.py", "migrate"]
        cmds = [make_migrations, migrate]
        print("Creating and publishing migrations.....\n")
        for i in range(len(cmds)-1):
            try:
                subprocess.run(cmds[i], check=True)
            except Exception as e:
                print("Error..", e)
            finally:
                continue
        print("Done creating migrations....\n")
       