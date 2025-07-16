from openai_api import call_openai_chat_completion
import nbformat

def split_code_cells_in_notebook(notebook_object, prompt_object, model_name):
    new_cells = []
    for cell in notebook_object.cells:
        if cell.cell_type == "code":
            result = call_openai_chat_completion(
                model_name, prompt_object, cell.source
            )
            code_blocks = result.split('\n\n---\n\n')  # 分割出力例
            for code_block in code_blocks:
                new_cell = nbformat.v4.new_code_cell(code_block)
                new_cells.append(new_cell)
        else:
            new_cells.append(cell)
    notebook_object.cells = new_cells
    return notebook_object

def annotate_code_cells_in_notebook(notebook_object, prompt_object, model_name):
    for cell in notebook_object.cells:
        if cell.cell_type == "code":
            annotated_source = call_openai_chat_completion(
                model_name, prompt_object, cell.source
            )
            cell.source = annotated_source
    return notebook_object

def insert_markdown_above_code_cells(notebook_object, prompt_object, model_name):
    new_cells = []
    for cell in notebook_object.cells:
        if cell.cell_type == "code":
            markdown_content = call_openai_chat_completion(
                model_name, prompt_object, cell.source
            )
            md_cell = nbformat.v4.new_markdown_cell(markdown_content)
            new_cells.append(md_cell)
        new_cells.append(cell)
    notebook_object.cells = new_cells
    return notebook_object

def improve_all_markdown_cells(notebook_object, prompt_object, model_name):
    for cell in notebook_object.cells:
        if cell.cell_type == "markdown":
            improved_content = call_openai_chat_completion(
                model_name, prompt_object, cell.source
            )
            cell.source = improved_content
    return notebook_object
