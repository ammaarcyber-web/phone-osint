📱 AMMAAR CYBER WARRIOR — PHONE OSINT ENGINE

Ethical • Passive • Defensive OSINT

Phone OSINT Engine kayan aiki ne na Python da aka tsara domin passive phone-number intelligence da defensive security research.

Yana amfani da bayanan metadata na lambar waya da public search links domin taimakawa wajen binciken abin da zai iya kasancewa a fili game da wata lambar waya.

«⚠️ Ethical Use Only: Yi amfani da wannan project ne kawai akan lambarka, bayananka, ko bayanan da kana da izinin bincikawa. Kada a yi amfani da shi wajen stalking, harassment, account takeover, ko samun bayanan sirri ba tare da izini ba.»

---

🚀 Features

- 📞 Phone-number validation
- 🌍 Country detection
- 📱 Number type detection
- 📡 Carrier information
- ✅ Valid / Possible number analysis
- 🔎 Public Google search link
- 🔎 Public Bing search link
- 💻 GitHub code-search link
- 👤 Optional user-supplied name search
- 🔎 Google name-search link
- 🔎 Bing name-search link
- 🛡️ Defensive exposure/risk assessment
- 📄 JSON report generation
- 🔐 Privacy-preserving number masking
- 🧩 Modular Python architecture

---

🖥️ Example Output

╔══════════════════════════════════════════╗
║                                          ║
║         AMMAAR CYBER WARRIOR             ║
║          PHONE OSINT ENGINE              ║
║                                          ║
║     ETHICAL • PASSIVE • DEFENSIVE        ║
╚══════════════════════════════════════════╝

Enter phone number: +234XXXXXXXXXX

Your name (optional, OSINT): Example Name

[+] Starting OSINT scan

[+] Validating phone number
[+] Analysing phone metadata
[+] Preparing public web searches
[+] Preparing public code searches
[+] Building defensive report

---

📦 Installation

1. Clone the repository

A sabon Termux:

pkg update
pkg install git python -y

Sai ka clone repository:

git clone https://github.com/ammaarcyber-web/phone-osint.git

Shiga cikin folder:

cd phone-osint

Duba files:

ls

---

2. Create Virtual Environment

python -m venv .venv

Kunna virtual environment:

source .venv/bin/activate

Ya kamata ka ga:

(.venv) ~/phone-osint $

---

3. Install Dependencies

python -m pip install -r requirements.txt

Current dependency:

phonenumbers

---

▶️ Run the Tool

Bayan installation:

python scan.py

Sai tool ya tambaye ka:

Enter phone number:

Ka saka number a international format, misali:

+234XXXXXXXXXX

Zai kuma iya tambayar:

Your name (optional, OSINT):

Name ɗin optional ne.

---

🔎 Public Search

Tool ɗin yana samar da links zuwa public search engines kamar:

Google

Search ɗin lambar waya:

https://www.google.com/search?q=...

Bing

https://www.bing.com/search?q=...

GitHub Code Search

https://github.com/search?q=...&type=code

Idan an bayar da suna, yana kuma samar da public Google da Bing searches na sunan.

«Tool ɗin yana samar da search links; ba ya nufin cewa search engine zai gano ko tabbatar da ainihin mai lambar ba.»

---

🛡️ Privacy & Defensive Design

Phone OSINT Engine yana da wasu privacy protections.

Number Masking

A report/output, cikakkiyar lambar ba lallai ta bayyana ba.

Misali:

+234**********224

Automatic Owner Identification

Tool ɗin baya ƙoƙarin tabbatar da ainihin owner na private phone number.

Automatic owner identification: DISABLED
Reason: Privacy protection

Wannan yana taimakawa wajen rage kuskuren attribution da privacy risks.

---

📄 Reports

Tool ɗin yana iya samar da JSON report a cikin:

reports/

Misali:

reports/osint_YYYYMMDD_HHMMSS.json

An saka:

reports/*.json

a cikin ".gitignore".

Saboda haka generated reports ba sa shiga Git repository ta default.

---

📁 Project Structure

phone-osint/
│
├── scan.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── osint/
│   ├── __init__.py
│   ├── public_search.py
│   ├── report.py
│   ├── risk.py
│   ├── scanner.py
│   └── validator.py
│
└── reports/
    └── generated JSON reports

---

🧩 Main Modules

"scan.py"

Babban entry point na tool.

python scan.py

---

"osint/validator.py"

Yana taimakawa wajen:

- validating phone numbers
- checking possible numbers
- identifying number type
- extracting phone metadata

---

"osint/public_search.py"

Yana shirya public search URLs domin:

- Google
- Bing
- GitHub Code Search
- name-based public searches

---

"osint/scanner.py"

Yana tsara matakan OSINT scan kuma yana haɗa sassan tool ɗin.

---

"osint/report.py"

Yana samar da defensive JSON reports.

---

"osint/risk.py"

Yana taimakawa wajen defensive exposure/risk assessment.

---

🔄 Updating the Tool

Idan ka riga ka clone repository ɗin kuma kana son samun sabon version:

cd phone-osint
git pull

Idan akwai sabbin dependencies:

source .venv/bin/activate
python -m pip install -r requirements.txt

---

💻 Development

Don duba Git status:

git status

Bayan ka gyara code:

git add .
git commit -m "Update Phone OSINT"
git push

---

🔐 Security Rules

Kada ka saka abubuwa kamar:

API keys
passwords
tokens
private credentials
.env files
private reports

cikin GitHub.

An riga an tanadi ".gitignore" domin wasu daga cikin waɗannan abubuwa:

.venv/
__pycache__/
*.pyc
reports/*.json
.env

---

⚠️ Legal & Ethical Notice

Wannan project an tsara shi ne domin:

- cybersecurity education
- defensive security
- authorized OSINT research
- privacy/exposure assessment
- security testing akan bayanan da aka ba ka izini

Kada ka yi amfani da shi wajen:

- stalking
- harassment
- doxxing
- identity theft
- unauthorized surveillance
- account takeover
- neman private information ba tare da izini ba

Public information ba yana nufin cewa duk wani amfani da ita ya dace ba. Ka mutunta privacy da dokokin yankinka.

---

👨‍💻 Author

Ammaar Cyber Warrior

Ammaar Cyber Security

Ethical OSINT • Defensive Security

---

⭐ Project

GitHub Repository:

https://github.com/ammaarcyber-web/phone-osint

Idan wannan project ya taimaka maka wajen koyon cybersecurity, zaka iya ⭐ repository ɗin a GitHub.

---

📜 License

Ka tabbatar ka saka license da ya dace da manufar project ɗinka kafin ka bayyana shi a matsayin open-source project.
