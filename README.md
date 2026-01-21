# Web Attack Log Detector (Mini SIEM-style)

This project is a simple web attack detection tool built as a DFIR-focused learning project.
It analyzes web server access logs (Apache/Nginx style) and detects common web attacks based
on request patterns.

The goal of this project is not exploitation, but detection and analysis — similar to how
SOC and DFIR teams investigate suspicious web activity using server logs.

---

## 🔍 What this tool does

The tool scans access logs and detects the following attack types:

- SQL Injection attempts
- Cross-Site Scripting (XSS) attempts
- Path Traversal attempts

For each attack type, it:
- Counts total attempts
- Identifies attacker IP addresses
- Generates a human-readable incident report

Each detector works independently and produces forensic evidence that can
later be correlated during an investigation.

---

## 📁 Project Structure

```
web-attack-log-detector/
│
├── core/
│ └── main.py
│
├── modules/
│ ├── sqli_detector.py
│ ├── xss_detector.py
│ └── path_traversal_detector.py
│
├── utils/
│ ├── evidance_csv.py
│ ├── report_generator.py
│ └── timeline_generator.py
│
├── logs/
│ └── sample_access.log
│
├── evidence_data/
│ ├── sqli_summary.csv
│ ├── xss_summary.csv
│ └── path_traversal_summary.csv
│
├── reports/
│ └── attack_report.txt
│
└── README.md
```

---

## 🧠 Detection & Evidence Logic

Each detector:
- Scans raw access logs
- Identifies malicious patterns
- Extracts:
  - Timestamp
  - Attacker IP
  - Attack type
  - Full log entry
- Writes structured CSV evidence

This mirrors how real DFIR investigations preserve raw evidence before
correlation.

---

## ⏱️ Timeline Correlation

The timeline module processes all generated evidence files and builds a
chronological view of attack activity.

This helps answer:
- When did the attack start?
- Which attack came first?
- Were multiple attack types launched by the same IP?

## 📝 Note

The `sample_access.log`file included in this repository is **synthetically generated** for learning and demonstration purposes only.

It does **not** belong to any real system, server, or organization.  
All IP addresses, usernames, and timestamps are dummy and used only to simulate real-world DFIR scenarios such as brute-force attacks and suspicious login behavior.

---

## How to run

From the project root directory:

```bash
python -m core.main
```
---

## 📊 Output

The tool generates a plain text incident report that includes:
- SQL Injection activity
- XSS activity
- Path Traversal activity

The report is saved inside the `reports/` directory and evidance CSV's isnide `evidace_data/`