# Password Cracking & Credential Attack Suite

A Python-based password security assessment and controlled credential attack simulation toolkit developed using Streamlit.

## Project Overview

This project demonstrates password security concepts through five functional modules. It helps users understand password weaknesses, hash formats, password strength, and controlled password-guessing simulations.

## Key Features

1. **Dictionary Generator** – Generates sample password variations from seed words.
2. **Hash Analysis** – Generates hashes and identifies possible hash formats using synthetic examples.
3. **Brute-Force Simulation** – Performs controlled local candidate-list testing and theoretical cracking-time estimation.
4. **Password Strength Analyzer** – Evaluates password complexity, patterns, and theoretical entropy.
5. **Security Audit Report Generator** – Generates downloadable CSV and PDF audit reports.

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- ReportLab
- Hashlib
- Regular Expressions

## Project Structure

```text
Password_Cracking_Credential_Attack_Suite/
│
├── app.py
├── dictionary_generator.py
├── hash_analyzer.py
├── brute_force_simulator.py
├── password_analyzer.py
├── report_generator.py
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

## Reports

The application supports downloadable TXT wordlists and CSV/PDF security audit reports.

## Security and Ethical Use

This project is developed strictly for educational and controlled security testing purposes.

- Uses synthetic test data.
- Performs brute-force demonstrations only through local sample candidate lists.
- Does not extract actual system credentials.
- Does not attack real login systems.
- Does not store plaintext passwords in generated audit reports.

## Disclaimer

This project is intended for educational and portfolio demonstration purposes only. It must not be used for unauthorized access or malicious activities.
