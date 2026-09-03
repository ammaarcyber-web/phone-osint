🛡️ Ammaar Cyber Warrior — Phone OSINT Engine

A defensive and ethical phone-number OSINT tool designed for infomation gathering-OSINT, privacy auditing, and public-exposure analysis.

The project analyzes phone-number metadata and generates links to legitimate public search services. It does not attempt to discover private information, passwords, OTPs, account access, or identify/deanonymize a person from their phone number.

---

✨ Features

- 📱 Phone-number validation
- 🌍 Country/region detection
- 📞 Number-type detection
- 📡 Carrier metadata when available
- 🔎 Real public search URLs
- 💻 Public GitHub search
- 🌐 Google search
- 🔍 Bing search
- 👤 Optional user-supplied name for self-OSINT
- 📊 Privacy/exposure scoring
- 📄 JSON report generation
- 🖥️ Professional terminal interface
- 🛡️ Defensive/privacy-focused design
- ⚡ CLI support
- 🏷️ Version information

---

⚠️ Ethical Use

This project is intended for:

- OSINT
- Privacy auditing
- Defensive cybersecurity
- Security education
- Testing information that you personally control
- Authorized security assessments

Do not use this project to stalk, harass, deanonymize, impersonate, or obtain private information about another person.

The tool intentionally does not perform automatic owner-name identification or social-account attribution from a phone number.

---

📂 Project Structure

phone-osint/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── osint/
│   ├── __init__.py
│   ├── validator.py
│   ├── public_search.py
│   ├── scanner.py
│   ├── risk.py
│   └── report.py
└── reports/

---

🚀 Installation

Termux / gathe

installation:

pkg install python && pkg install git

Clone the repository:

git clone https://github.com/YOUR-USERNAME/phone-osint.git
cd phone-osint

Create a virtual environment:

python -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

▶️ Basic Usage

Run the tool:

python scan.py

The program will ask for:

Enter phone number:
Your name (optional, OSINT):

Use international phone-number format, for example:

+234XXXXXXXXXX

---

⚡ Command-Line Usage

Show version:

python app.py --version

Run with a phone number:

python app.py --number "+234XXXXXXXXXX"

python app.py --number "+234XXXXXXXXXX" --name "Your Name"

---

🔎 Public Search

The tool generates links to legitimate public search services such as:

- Google
- Bing
- GitHub

The tool does not fabricate search results.

If no public result is available, the correct result is:

NO PUBLIC RESULT

rather than a fake finding.

---

📊 Example Output

╔══════════════════════════════════════════╗
║        AMMAAR CYBER WARRIOR              ║
║          PHONE OSINT ENGINE              ║
║                                          ║
║     ETHICAL • PASSIVE • DEFENSIVE        ║
╚══════════════════════════════════════════╝

[+] Validating phone number ........ DONE
[+] Analysing phone metadata ........ DONE
[+] Preparing public searches ....... DONE
[+] Building defensive report ... DONE

────────────────────────────────────────────
 PHONE ANALYSIS
────────────────────────────────────────────

Number       : +234*********
Country      : Nigeria
Valid        : YES
Possible     : YES
Type         : MOBILE

────────────────────────────────────────────
 IDENTITY
────────────────────────────────────────────

Automatic owner identification : DISABLED
Reason                        : Privacy protection

────────────────────────────────────────────
 REAL PUBLIC SEARCH LINKS
────────────────────────────────────────────

[1] Google
[2] Bing
[3] GitHub Code

────────────────────────────────────────────
 REPORT
────────────────────────────────────────────

[+] JSON report saved

============================================
 Created by Ammaar Cyber Warrior
 Ammaar Cyber Security
 Ethical OSINT • Defensive Security
============================================

---

📄 Reports

Reports are generated in:

reports/

Example:

reports/osint_20260901_182500.json

Reports contain structured information such as:

- Number metadata
- Country
- Number type
- Carrier metadata
- User-supplied name, if provided
- Public search URLs
- Risk information

Private credentials and authentication information are not collected.

---

🛠️ Technology

Built with:

- Python
- "phonenumbers"
- Standard Python libraries
- Termux/Linux compatible CLI design

---

🔐 Privacy Design

The project follows a privacy-first approach.

It intentionally avoids:

- Password discovery
- OTP interception
- Account takeover
- Private location tracking
- Private database access
- Social-account takeover
- Automatic identity deanonymization
- Credential harvesting

---

👨‍💻 Author

Ammaar Cyber Warrior

Ammaar Cyber Security

Ethical OSINT • Defensive Security • Cybersecurity Education
Whatsapp Havking tool is comingsoon...

---

📜 License

This project is intended for ethical and educational cybersecurity use.

See the repository license for the complete terms.
