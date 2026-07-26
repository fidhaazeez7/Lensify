import os
import zipfile

UPLOAD_FOLDER = "uploads"


def save_and_extract_zip(upload_file):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    zip_path = os.path.join(UPLOAD_FOLDER, upload_file.filename)

    with open(zip_path, "wb") as buffer:
        buffer.write(upload_file.file.read())

    extract_path = os.path.join(
        UPLOAD_FOLDER,
        upload_file.filename.replace(".zip", "")
    )

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)

    return extract_path


def get_project_files(folder):
    files = []

    for root, _, filenames in os.walk(folder):
        for file in filenames:
            files.append(
                os.path.relpath(
                    os.path.join(root, file),
                    folder
                )
            )

    return files