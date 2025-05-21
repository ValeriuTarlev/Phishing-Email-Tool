# Email Phishing Detector 
This project is a simple web-based phishing email detector built with **Flask**. It combines rule-based analysis with AI text classification to identify potentially malicious emails.

---

Features

- Submit email subject, body, sender, and link through a web form
- Analyze emails using:
  - Keyword and domain-based rule engine
  - AI model integration (e.g. HuggingFace)
- View phishing score, AI classification, and final assessment

---

Tech Stack

- Python 3.12+
- Flask
- Jinja2
- HTML/CSS (no frontend frameworks)
- AI model via `check_ai_text()` (integrated in `phishing_rules.py`)

---

Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/email-phishing-detector.git
   cd email-phishing-detector
   ```
2. Create and activate a virtual environment:

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   On macOS / Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
  
3. Install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Run the Flask app:
  ```bash
  python run.py
  ```
5. Open your browser and go to:
  ```
   https://127.0.0.1:5000
  ```
