# entrypoint.py
import subprocess

subprocess.run(["python", "-m", "core_crowler.runners.run_loc_crowler"])
