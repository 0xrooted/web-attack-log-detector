# Web Attack Log Detector (Mini SIEM-style)

This project is a simple web attack detection tool built as a DFIR-focused learning project.
It analyzes web server access logs (Apache/Nginx style) and detects common web attacks based
on request patterns.

The goal of this project is not exploitation, but detection and analysis — similar to how
SOC and DFIR teams investigate suspicious web activity using server logs.

---

## What this tool does

The tool scans access logs and detects the following attack types:

- SQL Injection attempts
- Cross-Site Scripting (XSS) attempts
- Path Traversal attempts

For each attack type, it:
- Counts total attempts
- Identifies attacker IP addresses
- Generates a human-readable incident report

---

## Project Structure

```
web-attack-log-detector/
│
├── detectors/
│ ├── sqli_detector.py
│ ├── xss_detector.py
│ └── path_traversal_detector.py
│
├── core/
│ └── report_generator.py
│
├── logs/
│ └── sample_access.log
│
├── reports/
│ └── attack_report.txt
│
├── main.py
└── README.md
```

---

## How detection works (high level)

- Access logs are read line by line
- Each detector searches for known attack indicators
- Attacker IPs are extracted from log entries
- Results are returned to a central controller (`main.py`)
- A DFIR-style incident report is generated

This approach is similar to how real-world log-based detection pipelines work.

---

## Output

The tool generates a plain text incident report that includes:
- SQL Injection activity
- XSS activity
- Path Traversal activity

The report is saved inside the `reports/` directory.

---

## Note

The `sample_access.log`file included in this repository is **synthetically generated** for learning and demonstration purposes only.

It does **not** belong to any real system, server, or organization.  
All IP addresses, usernames, and timestamps are dummy and used only to simulate real-world DFIR scenarios such as brute-force attacks and suspicious login behavior.

---

## How to run

From the project root directory:

```bash
python -m core.main