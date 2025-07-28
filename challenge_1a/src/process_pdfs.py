import os
import fitz
import json

def extract_outline(path):
    doc = fitz.open(path)
    outlines = []
    toc = doc.get_toc(simple=True)
    for item in toc:
        level, title, page = item
        outlines.append({
            "level": level,
            "title": title.strip(),
            "page_number": page
        })
    return outlines

def build_json(outlines, filename):
    result = {
        "file_name": filename,
        "title": "",
        "headings": []
    }

    if outlines:
        result["title"] = outlines[0]["title"]
        for item in outlines[1:]:
            level = item["level"]
            heading = {
                "text": item["title"],
                "page": item["page_number"],
                "level": f"H{level}"
            }
            result["headings"].append(heading)

    return result

def main():
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            path = os.path.join(input_dir, file)
            outlines = extract_outline(path)
            result = build_json(outlines, file)
            out_file = os.path.join(output_dir, file.replace(".pdf", ".json"))
            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4)

if __name__ == "__main__":
    main()