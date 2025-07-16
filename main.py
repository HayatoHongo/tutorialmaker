import argparse
from notebook_processor import (
    split_code_cells_in_notebook,
    annotate_code_cells_in_notebook,
    insert_markdown_above_code_cells,
    improve_all_markdown_cells,
)
from utils import load_notebook_from_file, save_notebook_to_file
from prompt_loader import load_prompt_from_json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_notebook_path")
    parser.add_argument("output_notebook_path")
    parser.add_argument("--model", default="gpt-4o-mini")
    parser.add_argument("--prompts_dir", default="prompts/")
    args = parser.parse_args()

    notebook_object = load_notebook_from_file(args.input_notebook_path)

    split_prompt = load_prompt_from_json(f"{args.prompts_dir}/split_code.json")
    notebook_object = split_code_cells_in_notebook(
        notebook_object, split_prompt, args.model
    )

    annotate_prompt = load_prompt_from_json(f"{args.prompts_dir}/annotate_code.json")
    notebook_object = annotate_code_cells_in_notebook(
        notebook_object, annotate_prompt, args.model
    )

    md_prompt = load_prompt_from_json(f"{args.prompts_dir}/markdown_generate.json")
    notebook_object = insert_markdown_above_code_cells(
        notebook_object, md_prompt, args.model
    )

    md_rewrite_prompt = load_prompt_from_json(f"{args.prompts_dir}/markdown_rewrite.json")
    notebook_object = improve_all_markdown_cells(
        notebook_object, md_rewrite_prompt, args.model
    )

    save_notebook_to_file(notebook_object, args.output_notebook_path)

if __name__ == "__main__":
    main()
