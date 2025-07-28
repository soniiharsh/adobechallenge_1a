# 🧠 PDF Outline Extractor 🔍📄

## 🚀 Overview

This project extracts structured outlines (Title, H1, H2, H3 headings) along with page numbers from PDF files and converts them into a valid JSON format. It is designed to run in **Docker**, on **CPU (amd64)**, and complete processing within **10 seconds** for a 50-page PDF — perfect for constrained hackathon environments.

---

## ✅ Features

- ⚙️ Fully automated PDF to JSON conversion  
- 🔖 Heading structure detection: Title, H1, H2, H3  
- 🧪 JSON schema validation  
- 🐳 Docker support  
- 🧼 Clean and modular code  
- 📁 Batch processing of multiple PDFs in `input/` folder  
- 📦 Output stored as JSON files in `output/` folder  

---

## 📦 Project Structure

```
📁 input/           # Place your PDF files here
📁 output/          # Processed JSONs are saved here
📁 src/
  ├── extract_outline.py    # Core logic for heading extraction
  ├── process_pdfs.py       # PDF batch processor & JSON validator
📄 requirements.txt         # Python dependencies
🐳 Dockerfile               # Container definition
README.md                  # You're reading it!
```

---

## 🔧 Prerequisites

- Python 3.8+  
- `pip` installed  
- Docker (optional but recommended for deployment)

---

## 🛠️ Installation

1. **Clone the repo**:

```bash
git clone https://github.com/your-username/pdf-outline-extractor.git
cd pdf-outline-extractor
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🧪 Step-by-step (Locally)

1. Place your `.pdf` files inside the `input/` folder.

2. Run the processing script:

```bash
python src/process_pdfs.py
```

3. All extracted JSONs will be saved in the `output/` folder.

4. To validate the JSON structure:

```bash
python src/validate_jsons.py
```

---

### 🐳 Step-by-step (Docker)

1. **Build the Docker image**:

```bash
docker build -t pdf-outline-extractor .
```

2. **Run the Docker container**:

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-outline-extractor
```

> This will process all PDFs in `input/` and save outputs in `output/`.

---

## 🧾 Output Format (Schema)

Each JSON output will follow this schema:

```json
{
  "file_name": "sample.pdf",
  "title": "Introduction to Quantum Computing",
  "headings": [
    {
      "text": "1. Quantum Basics",
      "page": 1,
      "level": "H1"
    },
    {
      "text": "1.1 Qubits",
      "page": 2,
      "level": "H2"
    }
  ]
}
```

---

## 🧪 Testing

To validate all generated JSONs against the schema:

```bash
python src/validate_jsons.py
```

---

## 📂 Sample PDFs & Output

To test the system, you can use the included sample PDFs in the `input/` folder. Corresponding valid JSONs are automatically created in `output/`.

---

## 🧩 Troubleshooting

- **PDF not found?**  
  > Ensure the files are inside the `input/` folder with `.pdf` extension.

- **No headings extracted?**  
  > Some PDFs use scanned images or non-standard fonts. Try with text-based PDFs.

- **Invalid JSON format?**  
  > Run the validator using `validate_jsons.py` for details.

- **Docker build fails?**  
  > Ensure you have internet access and Docker is properly installed.

---

## 🙌 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss.

---

## 📜 License

This project is licensed under the MIT License.

---

## ✨ Authors

- Harsh Soni  
- Team Adobe Hackathon 2025
