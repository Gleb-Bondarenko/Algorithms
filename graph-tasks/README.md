### **Submission Rules**

#### 1) Repository contents (5 files on GitHub)

Put **all five** required files in your repo:

* `graph_abc.py`
* `graph_building.py`
* `graph_factory.py`
* `algorithmics.py`
* your notebook (`tasks.ipynb`)

Track only what’s needed. Add a proper `.gitignore` (see below).

---

#### 2) `requirements.txt` must be auto-generated (not handwritten)

Create and activate a virtual environment, install only the packages you use (e.g., `networkx`, `matplotlib`), then export exact versions:

```bash
# create venv (one option)
python -m venv .venv

# activate (Windows)
.venv\Scripts\activate
# activate (macOS/Linux)
source .venv/bin/activate

# export exact versions automatically 
pip freeze > requirements.txt
```

Commit `requirements.txt` to the repo.

---

#### 3) Deadline

**Due:** **16 Oct 2025, 23:59**
The **last commit** must be **no later** than this timestamp.

---

#### 4) Submit your link

Add your GitHub repo URL to the shared Google Sheet (See the link in the Lecture 8.pptx) in the format:

```
student_name | https://github.com/<user>/<repo>
```

---

#### Recommended `.gitignore`

Create a `.gitignore` at the root of your repo with at least:

```
# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environments
.venv/
venv/
env/
```
