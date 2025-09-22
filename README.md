# Python Exercises

This repository contains my practice exercises and tutorials for learning **Python**, focusing on both **data analysis with pandas** and **general Python programming** (based on the *Python for Everybody (PY4E)* course).

---

## 📂 Project Structure

### 🐼 Pandas Tutorials (`Pandas Tutorials/`)
Hands-on scripts that follow along with the official pandas documentation and tutorials.

- `tutorial1.py` – Reading and writing tabular data  
- `tutorial2.py` – Selecting and subsetting data  
- `tutorial3.py` – Dealing with missing data  
- `tutorial4.py` – Creating plots in pandas  
- `tutorial5.py` – Creating new columns from existing ones  
- `tutorial6.py` – Aggregation and summary statistics  
- `tutorial7.py` – Reshaping and pivoting tables  
- `tutorial8.py` – Combining and merging data  

> These scripts demonstrate pandas basics: I/O, indexing, transformations, visualizations, reshaping, and joins.

---

### 🐍 PY4E Exercises (`PY4E/`)
Exercises from the [Python for Everybody](https://www.py4e.com/) course, covering Python fundamentals and applied programming.

- **Text parsing & regex**  
  - `regex_sum.py`, `regex_sum.txt`  
  - `mbox-short.txt`  

- **APIs & Web scraping**  
  - `geocoding_api.py`  
  - `beautiful_soup.py`, `beautiful_soup2.py`, `beautiful_soup3.py`  

- **JSON & XML**  
  - `json_counter.py`  
  - `xml_counter.py`  

- **Databases with SQLite**  
  - `sqlwork.py`, `sqlwork2.py`, `sqlwork3.py`, `sqlwork4.py`, `sqlwork5.py`  
  - `sqlwork.sqlite`, `sqlwork2.sqlite`, `sqlwork3.sqlite`, `sqlwork4.sqlite`, `sqlwork5.sqlite`  

- **Miscellaneous**  
  - `email_counter.py`  
  - `socket_practice.py`  
  - `sorted_counter.py`  
  - `roster_data.json`  
  - `tracks.csv`  

---

## 🚀 How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/<your-username>/python-exercises.git
   cd python-exercises
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on macOS/Linux
   venv\Scripts\activate      # on Windows
   ```

3. **Install requirements (for pandas tutorials)**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run any script**

   ```bash
   python "Pandas Tutorials/tutorial4.py"
   ```

---

### 📝 Notes

* Some scripts (especially Pandas tutorials) require CSV datasets located in the `data/` folder.
* Python version 3.8+ is recommended.
* Virtual environment (`venv/`) is included in `.gitignore` so it won’t clutter the repo.
* SQLite files (`.sqlite`) are provided for database exercises.

---

### 📚 References

* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Python for Everybody (PY4E)](https://www.py4e.com/)
