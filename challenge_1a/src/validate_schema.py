import json
import os
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "file_name": {"type": "string"},
        "title": {"type": "string"},
        "headings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "page": {"type": "integer"},
                    "level": {"type": "string"}
                },
                "required": ["text", "page", "level"]
            }
        }
    },
    "required": ["file_name", "title", "headings"]
}

def main():
    output_dir = "output"
    for file in os.listdir(output_dir):
        if file.endswith(".json"):
            with open(os.path.join(output_dir, file)) as f:
                data = json.load(f)
                validate(instance=data, schema=schema)
                print(f"{file} is valid ✅")

if __name__ == "__main__":
    main()