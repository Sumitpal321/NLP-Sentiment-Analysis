# Copilot / AI Agent Instructions for "NLP Project"

This repository is a small, single-package NLP project with three top-level Python scripts: `main.py` (entrypoint), `process.py` (text preprocessing), and `sentiment.py` (sentiment analysis logic). `requirement.txt` holds Python dependencies.

Goals for AI coding agents
- Keep changes minimal and local to the referenced files unless asked to re-structure the project.
- Produce explicit, runnable code edits and include how to run or test them locally on Windows PowerShell.
- Reference concrete file paths and function names in your edits (examples below).

Quick facts (discovered from the repo)
- Project root files: `main.py`, `process.py`, `sentiment.py`, `requirement.txt`.
- No tests or CI are present; expect manual verification by running `python main.py`.
- Project is on Windows (user working directory under OneDrive); be mindful of path/encoding/line-ending differences.

Patterns and conventions to follow
- Single-file responsibilities: keep preprocessing in `process.py` and model/analysis logic in `sentiment.py`. `main.py` should orchestrate (load -> process -> analyze -> output).
- If you add a new public function, prefer a clear name and signature. Example: add `def clean_text(text: str) -> str:` in `process.py` and call it from `main.py`.
- Return structured results from analysis functions. Example expected from `sentiment.py`: `def analyze_sentiment(text: str) -> dict:` returning `{"score": float, "label": "positive|neutral|negative"}`.

Examples of short, safe edits to request or implement
- Add a preprocessing helper in `process.py`:

  def clean_text(text: str) -> str:
      """Lowercase, strip, remove extra whitespace and basic punctuation."""
      ...

- Add a simple wrapper in `sentiment.py`:

  def analyze_sentiment(text: str) -> dict:
      """Return sentiment score and label. Keep deterministic and small for unit checks."""
      ...

- Update `main.py` to show expected orchestration:

  if __name__ == '__main__':
      raw = "..."
      cleaned = clean_text(raw)
      result = analyze_sentiment(cleaned)
      print(result)

How to run and verify edits locally (Windows PowerShell)
- Install dependencies (if updated):

  pip install -r requirement.txt

- Run the main script:

  python main.py

What NOT to change without permission
- Do not introduce new top-level packages or change the project layout without confirming with the repo owner.
- Avoid adding heavy third-party ML models or large data files directly in the repo; propose them as external downloads or requirements entries.

When pulling or modifying dependencies
- If you add packages, update `requirement.txt` and include a one-line justification in your PR description.

If anything is unclear or you need runtime examples, ask for:
- A small sample input string to exercise `process.py` and `sentiment.py`.
- Any preferred output format (JSON, plain text, CSV).

End of guidance — please show the exact patch you plan to apply before editing multiple files.
