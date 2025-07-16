import argparse
import logging
from notebook_processor import (
    split_code_cells_in_notebook,
    annotate_code_cells_in_notebook,
    insert_markdown_above_code_cells,
    improve_all_markdown_cells,
)
from utils import load_notebook_from_file, save_notebook_to_file
from prompt_loader import load_prompt_from_json

def main():
    # ログ設定
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser()
    parser.add_argument("input_notebook_path")
    parser.add_argument("output_notebook_path")
    parser.add_argument("--model", default="gpt-4o-mini")
    parser.add_argument("--prompts_dir", default="prompts/")
    args = parser.parse_args()

    logger.info(f"入力ノートブック: {args.input_notebook_path}")
    logger.info(f"出力ノートブック: {args.output_notebook_path}")
    logger.info(f"使用モデル: {args.model}")
    logger.info(f"プロンプトディレクトリ: {args.prompts_dir}")

    logger.info("ノートブックを読み込み中...")
    notebook_object = load_notebook_from_file(args.input_notebook_path)

    logger.info("STEP1: コードセルの分割を実行中...")
    split_prompt = load_prompt_from_json(f"{args.prompts_dir}/split_code.json")
    notebook_object = split_code_cells_in_notebook(
        notebook_object, split_prompt, args.model
    )

    logger.info("STEP2: コードセルへの #TODO コメント付与を実行中...")
    annotate_prompt = load_prompt_from_json(f"{args.prompts_dir}/annotate_code.json")
    notebook_object = annotate_code_cells_in_notebook(
        notebook_object, annotate_prompt, args.model
    )

    logger.info("STEP3: 解説Markdownの挿入を実行中...")
    md_prompt = load_prompt_from_json(f"{args.prompts_dir}/markdown_generate.json")
    notebook_object = insert_markdown_above_code_cells(
        notebook_object, md_prompt, args.model
    )

    logger.info("STEP4: Markdownの改良を実行中...")
    md_rewrite_prompt = load_prompt_from_json(f"{args.prompts_dir}/markdown_rewrite.json")
    notebook_object = improve_all_markdown_cells(
        notebook_object, md_rewrite_prompt, args.model
    )

    logger.info("ノートブックを保存中...")
    save_notebook_to_file(notebook_object, args.output_notebook_path)
    logger.info("すべての処理が完了しました！")

if __name__ == "__main__":
    main()
