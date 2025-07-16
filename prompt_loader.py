import json

def load_prompt_from_json(json_file_path):
    with open(json_file_path, "r", encoding="utf-8") as f:
        prompt_object = json.load(f)

    # system, userがlistならjoinしてstrに変換
    for key in ["system", "user"]:
        if isinstance(prompt_object.get(key), list):
            prompt_object[key] = "\n".join(prompt_object[key])
    return prompt_object
