
# Resume vs Job Description Matcher 🔍

A smart, AI-powered web app that compares your resume with a job description and gives a **match score** to help you tailor your resume more effectively. Built using Python, Streamlit, and Sentence-BERT, this project is perfect for job seekers, career coaches, or developers looking to showcase their NLP skills.

---

## 📌 Features

- ✅ Upload your resume in **PDF format**
- ✅ Paste any job description text
- ✅ Get a **semantic match score (%)**
- ✅ Simple, clean UI using Streamlit
- ✅ Fast and accurate thanks to Sentence-BERT
- ✅ All processing is local — no resume data is stored

---

## 🧠 How It Works

1. Extracts text from the uploaded resume using **PyMuPDF**
2. Accepts job description input in a text area
3. Converts both texts to embeddings using **SentenceTransformers**
4. Calculates **cosine similarity** between embeddings
5. Returns a match percentage with feedback

---

## 🛠 Tech Stack

| Component         | Library / Tool                          |
|------------------|------------------------------------------|
| Web Interface     | [Streamlit](https://streamlit.io/)      |
| PDF Parsing       | [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) |
| NLP Model         | [Sentence-BERT](https://www.sbert.net/) |
| Matching Metric   | Cosine Similarity (via `util.pytorch_cos_sim`) |
| Language          | Python 3.8+                             |

---

## 📂 Project Structure

```
resume_matcher/
├── app.py                # Streamlit web app
├── matcher.py            # Core matching logic (NLP + similarity)
├── resume_parser.py      # Resume text extractor using PyMuPDF
├── requirements.txt      # Project dependencies
└── README.md             # You're here
```

---

## 🚀 Getting Started

Follow the steps below to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/Durvesh84/Resume-Checker.git
cd Resume-Checker
```

### 2. (Optional) Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

### 5. Open in your browser

Go to `http://localhost:8501`

---

## ✅ Example Use Case

> **Job Description:** Junior Data Analyst (SQL, Power BI, Python)  
> **Resume:** PDF resume with Power BI & SQL skills  
> **Result:** Match Score = 83.45%  
> ✅ *Feedback: Great match! Your resume aligns well with the job description.*

---

## 🔮 Future Enhancements

- [ ] Section-wise match scoring (Skills, Education, Experience)
- [ ] Suggest missing skills/keywords from the JD
- [ ] Resume improvement tips using OpenAI API
- [ ] PDF report download option
- [ ] Streamlit Cloud deployment
- [ ] Upload JD as PDF

---

## 📦 Example `requirements.txt`

```
streamlit
pymupdf
sentence-transformers
numpy
```

---

## 🌐 Deployment

You can deploy this app to [Streamlit Cloud](https://streamlit.io/cloud) for free:

```bash
# After pushing to GitHub
1. Go to https://streamlit.io/cloud
2. Click “New App”
3. Select your GitHub repo
4. Set `app.py` as the entry point
5. Deploy and share your link!
```

---

## 👨‍💻 Author

**Durvesh Chaudhari**  
B.Sc. Computer Science Student | Aspiring Data Scientist  
📧 [durveshchaudhari7777@gmail.com](mailto:durveshchaudhari7777@gmail.com)  
🔗 [GitHub Profile](https://github.com/Durvesh84)

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.

---

## ⭐️ Support & Feedback

If you like this project, consider giving it a ⭐ on GitHub!  
Have ideas or feedback? Feel free to open an issue or reach out.
