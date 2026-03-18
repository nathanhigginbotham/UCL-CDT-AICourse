## Project Overview

This is an open-source AI/ML course for secondary school students (ages 14–18) with no assumed programming or maths background. Notebooks are designed to run in **Kaggle Notebooks** (no local setup required). The course is produced by UCL DISI PhD students.

**Core dependencies:** `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `torch`, `torchvision`

Local development:
```bash
pip install -r requirements.txt
jupyter notebook
```

## Notebook Structure & Conventions

Each notebook follows the pedagogical loop: **Code → Observe → Explain → Improve**.

### Standard cell order

Every notebook must follow this structure in order:

1. **Title cell** (markdown) — lesson title and developers/reviewers
2. **Learning objectives** (markdown) — bullet list of what students will have done by the end
3. **Setup cell** (code)
4. **Conceptual intro** (markdown) — what problem are we solving?
5. **Steps** (repeat for each step):
   - Markdown intro with step heading and any key term definitions
   - Code cell
   - Markdown separator (if another code cell follows immediately)
   - Markdown observation/explanation
6. **Summary** (markdown) — recap paragraph + key words table
7. **Challenge** (markdown + code) — one thing for students to change
8. **Quiz** (markdown + code) — `from quiz import run_bXX_quiz; run_bXX_quiz()`

### Title cell template

```markdown
# <span style="color: purple;">Lesson N - Title</span>

**Developers:** [name]  |  **Reviewers:** [names]

---

## <span style="color: purple;">🎯 Learning Objectives</span>

By the end of this lesson, you will have:

- [bullet 1]
- [bullet 2]
- [bullet 3]
- [bullet 4]

<div class="alert alert-info">

**How it works:** Click the ▶ button on the top left of each code cell, top to bottom. Read the explanation after you see the output. That's it!

</div>
```

### Setup cell template

Every notebook must have a setup cell immediately after the title. It contains **all imports** for the entire notebook — never import inside individual cells.

```python
# ─────────────────────────────────────────────────────────────
# Setup cell — run this first, then you can ignore it
# ─────────────────────────────────────────────────────────────
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
# ... all other imports ...
from tqdm.notebook import tqdm

print("✓ Ready to go!")
```

### Formatting conventions

- Section headings: `## <span style="color: purple;">Step N - Title</span>`
- Key term definitions: `<div class="alert alert-success">` (green) at the **point of first use only**
- Instructions and observations: `<div class="alert alert-info">` (blue)
- Explanations always follow code cells — students run code first, then read
- Avoid jargon; define every technical term immediately in a green alert-success box
- Tables used for concept summaries and comparisons
- Never leave commented-out code in cells

### Code cell conventions

- **All imports in the setup cell only** — never re-import in later cells
- **Every code cell must end with a `print("✓ ...")`** to confirm it ran
- **No consecutive code cells** — always put a markdown cell between two code cells
- **Progress bars:** use `tqdm` with `warm_start=True` for any training loop:
  ```python
  chunk = 50
  model = MLPClassifier(max_iter=chunk, warm_start=True, random_state=42)
  for _ in tqdm(range(total_steps // chunk), desc="Training"):
      model.fit(X_train, y_train)
      model.max_iter += chunk
  ```
- **Changeable code:** mark variables students should modify with arrows:
  ```python
  # ▼▼▼▼▼▼▼▼▼▼▼▼▼▼  CHANGE THIS  ▼▼▼▼▼▼▼▼▼▼▼▼▼▼
  my_variable = 100   # ← try different values
  # ▲▲▲▲▲▲▲▲▲▲▲▲▲▲  CHANGE THIS  ▲▲▲▲▲▲▲▲▲▲▲▲▲▲
  ```

### Quiz convention

- Add a `run_bXX_quiz()` function to `quiz.py` with the lesson's questions
- The notebook quiz cell is always just two lines:
  ```python
  from quiz import run_bXX_quiz
  run_bXX_quiz()
  ```
- Questions must use `random.sample` to shuffle options on each run
- Feedback: green ✔ for correct, red ✘ + correct answer for wrong
- Score summary shown after submission

## Lesson Development Guidelines

- **Length:** Each lesson should take approximately 15 minutes to complete. Keep content concise and focused on one core idea.
- **Code-first:** Follow Code → Observe → Explain → Improve. Students should see outputs before reading explanations.
- **Balance:** Aim for 60–70% code cells, 30–40% markdown.
- **Code cells:** Use 5–8 code cells per notebook. Each cell should perform one small, clear step.
- **Markdown style:** Explanations should be 2–4 sentences. Avoid long paragraphs.
- **Code clarity:** Prioritise readability over efficiency. Use simple syntax, clear variable names, and short inline comments.
- **Early engagement:** Students should run a working example within the first few minutes.
- **Visualisation:** Use simple plots or printed outputs to make model behaviour visible.
- **Experimentation:** End each lesson with one small challenge or modification for students to try.
- **Testing:** Verify the notebook runs end-to-end in Kaggle Notebooks without errors and fits within 15 minutes.
- **Platform note:** The primary platform is Kaggle. Colab-specific features (`# @title`, `cellView: "form"`) do not work in Kaggle — do not use them. `ipywidgets` is supported in Kaggle and should be used for interactive elements.

## Audience Constraints

- Assume **zero** prior programming knowledge — never reference "Hello World" or similar programmer conventions
- Avoid mathematical notation unless introduced step-by-step
- All datasets should be either built into scikit-learn or loadable without authentication
- Never require local file downloads; use URLs or library-bundled datasets
- Use plain, direct language — avoid idioms like "keen-eyed" that may not land with a teen audience
- Never leave commented-out code cells in notebooks; students may find it confusing or think they've made an error

## Module Progression

Modules 0–2 cover ML basics (classification, regression). Modules 3–7 cover model improvement and tree-based methods. Modules 8–10 cover neural networks and CNNs with PyTorch. Modules 11–13 apply models to real scientific datasets. Module 14 covers bias and fairness.
