# 🏦 HoneyBank - Fake Banking File Generator

**HoneyBank** is a cybersecurity deception tool that generates realistic, fake banking documents for use in honeypots, honey shares, and insider threat detection systems.

This tool is designed to **simulate sensitive data** such as account statements, wire transfers, audit reports, and loan documents using a mix of document formats like `.docx`, `.xlsx`, `.csv`, and `.pdf`.

## 🚨 Purpose

HoneyBank helps detect unauthorized access by planting decoy data in places where attackers might go looking for valuable information. When an attacker interacts with these files, it can trigger alerts, helping security teams detect threats early.

---

## ✨ Features

- ✅ Generates realistic folder structures using fake customer names and account numbers  
- 🧠 Optionally uses **[Ollama](https://ollama.com/)** with an LLM (like `llama3`, `mistral`, or `dolphin`) to generate smart, topic-aware file contents
- 📂 Supports multiple file types: `.docx`, `.xlsx`, `.csv`, `.pdf`
- 🎯 Topic-based document generation (e.g., Account Statements, Wire Transfers, Audit Reports)
- ⚙️ Configurable via command-line arguments
- 🪤 Designed for deception environments, insider threat hunting, and threat detection research

---

## 🤪 Example Use Case

1. Deploy HoneyBank to a shared network drive labeled `CustomerDocs` or `Internal_Finance`.
2. Generate 50 fake customer folders with a mix of `.pdf`, `.xlsx`, and `.docx` files.
3. Monitor access logs for interaction with these decoy files.
4. Trigger alerts or initiate investigations when unauthorized access is detected.

---

## 💠 Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```

> If using Ollama:
> - Make sure `ollama` is installed and running locally.
> - Choose a supported model like `llama3`, `mistral`, or `dolphin-mixtral`.

---

## 🚀 Usage

```bash
python honeybank.py \
  --base_path ./decoy_shares \
  --num_folders 10 \
  --file_types docx pdf xlsx \
  --use_ollama 
```

---

## 🔐 Disclaimer

This project is intended for **defensive cybersecurity research, detection engineering, and/or educational purposes only**. Do not use this tool for malicious purposes.

---

