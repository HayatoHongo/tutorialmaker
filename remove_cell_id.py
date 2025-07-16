import nbformat
import sys

def remove_id_from_all_cells(notebook_path, output_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    for cell in nb.cells:
        if 'id' in cell:
            del cell['id']
    with open(output_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_cell_id.py input.ipynb output.ipynb")
        sys.exit(1)
    remove_id_from_all_cells(sys.argv[1], sys.argv[2])
    print("idフィールド削除が完了しました。")
