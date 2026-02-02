import os
import shutil
import subprocess
import sys
from datetime import datetime

BASE = os.getcwd()
IMAGES = os.path.join(BASE, "images")
CONTAINERS = os.path.join(BASE, "containers")
LOGS = os.path.join(BASE, "logs")


def log(container, message):
    os.makedirs(LOGS, exist_ok=True)
    with open(f"{LOGS}/{container}.log", "a") as f:
        f.write(f"{datetime.now()} : {message}\n")


def build(image_name):
    path = f"{IMAGES}/{image_name}"
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/hello.sh", "w") as f:
        f.write("#!/bin/bash\necho Hello from mini container 🚀\n")

    os.chmod(f"{path}/hello.sh", 0o755)
    print("Image created")


def run(image, container):
    src = f"{IMAGES}/{image}"
    dst = f"{CONTAINERS}/{container}"

    if not os.path.exists(src):
        print("Image not found")
        return

    shutil.copytree(src, dst)

    log(container, "STARTED")
    subprocess.run(["bash"], cwd=dst)
    log(container, "STOPPED")


def list_all():
    print("Images:", os.listdir(IMAGES))
    print("Containers:", os.listdir(CONTAINERS))


def logs(container):
    with open(f"{LOGS}/{container}.log") as f:
        print(f.read())


def remove(container):
    shutil.rmtree(f"{CONTAINERS}/{container}", ignore_errors=True)


if __name__ == "__main__":
    cmd = sys.argv[1]

    if cmd == "build":
        build(sys.argv[2])

    elif cmd == "run":
        run(sys.argv[2], sys.argv[3])

    elif cmd == "list":
        list_all()

    elif cmd == "logs":
        logs(sys.argv[2])

    elif cmd == "rm":
        remove(sys.argv[2])
