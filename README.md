# Minimal BPE Tokenizer

## 📌 Overview
This is a minimal implementation of a **Byte Pair Encoding (BPE) tokenizer** in Python, created for the GDG ML recruitment task.

The tokenizer can:
1. Train on a text corpus (e.g., `input.txt`)
2. Encode text into integer IDs
3. Decode IDs back to text (lossless for training data)

## 📂 File Structure
bpe_tokenizer/
│
├── src/
│ ├── tokenizer.py # Tokenizer implementation
│ └── main.py # Example runner
├── input.txt # Training corpus (e.g., alice.txt)
├── output.txt # Demo results
└── README.md

markdown
Copy code

## ⚡ Usage
1. Place your training text in `input.txt`.
2. Run the example:
```bash
python src/main.py 
```
3. The encoded IDs and decoded text will be saved in output.txt