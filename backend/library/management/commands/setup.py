from http.client import HTTPException
from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Install required files and create venv'

    def handle(self, *args, **kwargs):
        upgrade_pip_v = ["python", "-m", "pip", "install", "--upgrade", "pip"]
        install_dependencies = ["pip", "install",
                                "-r", "requirements.txt"]
        create_venv = ["python", "-m", "venv", "env"]
        cmds = [upgrade_pip_v, install_dependencies]
                
        for i in range(len(cmds)-1):
            try:
                subprocess.run(cmds[i], check=True)
            except Exception as e:
                print("Error..", e)
            finally:
                continue
        print("Succesfully Installed all requirements.")
        print("Creating virtual environment....")
        subprocess.run(create_venv, check=True)
        print("Finished Creating the virtual environment.")
        print("Run the cmd below to activate venv\n")
        print("env\\Scripts\\activate")