from http.client import HTTPException
from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Automate the setup'

    def handle(self, *args, **kwargs):
        upgrade_pip_v = ["python", "-m", "pip", "install", "--upgrade", "pip"]
        install_dependencies = ["pip", "install",
                                "-r", "requirements.txt"]
        create_venv = ["python", "-m", "venv", "env"]
        activate_venv = ["env\\scripts\\activate"]
        cmds = [upgrade_pip_v, install_dependencies,
                create_venv, activate_venv]
        for i in range(len(cmds)-1):
            try:
                subprocess.run(cmds[i], check=True)
            except Exception as e:
                print("Error. Check your network..", e)
            finally:
                continue
