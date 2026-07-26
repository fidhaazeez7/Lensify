import os
import shutil
import tempfile
from fastapi import UploadFile


def save_uploaded_folder(files: list[UploadFile]) -> str:

    temp_dir = tempfile.mkdtemp()

    if not files or not files[0].filename:
        return temp_dir

    project_name = files[0].filename.split("/")[0].split("\\")[0]

    project_dir = os.path.join(temp_dir, project_name)

    os.makedirs(project_dir, exist_ok=True)

    # 👇 Replace your existing for loop with this
    for file in files:

        print("Received:", file.filename)

        if not file.filename:
            continue

        relative_path = file.filename.replace("\\", "/")
        print("Saving:", relative_path)

        destination = os.path.join(temp_dir, relative_path)
        print("Destination:", destination)

        os.makedirs(os.path.dirname(destination), exist_ok=True)

        with open(destination, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    # 👇 Add this before return
    print("\n===== Saved Project Structure =====")

    for root, _, filenames in os.walk(temp_dir):
        print(root)
        for f in filenames:
            print("   ", f)

    print("==================================\n")

    return project_dir