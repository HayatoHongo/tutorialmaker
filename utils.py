import nbformat

def load_notebook_from_file(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        return nbformat.read(f, as_version=4)

def save_notebook_to_file(notebook_object, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        nbformat.write(notebook_object, f)
