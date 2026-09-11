import os
from typing import List, Tuple

from pypdf import PdfReader

from app.config import DATA_DIR


def _read_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _read_pdf(path: str) -> str:
    reader = PdfReader(path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


def load_documents(
    data_dir: str = DATA_DIR,
) -> List[Tuple[str, str]]:
    """
    Return a list of (filename, full_text)
    for every .txt, .md, and .pdf file in data_dir.
    """

    documents = []

    if not os.path.exists(data_dir):
        raise FileNotFoundError(
            f"Data directory '{data_dir}' does not exist."
        )

    for filename in sorted(os.listdir(data_dir)):

        path = os.path.join(data_dir, filename)

        if not os.path.isfile(path):
            continue

        ext = filename.lower().rsplit(".", 1)[-1]

        if ext in ("txt", "md"):
            text = _read_txt(path)

        elif ext == "pdf":
            text = _read_pdf(path)

        else:
            continue

        if text.strip():
            documents.append((filename, text))

    return documents

