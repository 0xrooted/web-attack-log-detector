from detectors.sqli_detector import detect_sqli
from detectors.xss_detector import detect_xss
from detectors.path_traversal_detector import detect_path_traversal
from core.report_generator import generate_report

LOG_FILE = "../logs/sample_access.log"
REPORT_FILE = "../reports/attack_report.txt"

def main():
    results = {}

    sqli_count, sqli_ips = detect_sqli(LOG_FILE)
    xss_count, xss_ips = detect_xss(LOG_FILE)
    path_count, path_ips = detect_path_traversal(LOG_FILE)

    results["SQL Injection"] = {"count": sqli_count, "ips": sqli_ips}
    results["XSS"] = {"count": xss_count, "ips": xss_ips}
    results["Path Traversal"] = {"count": path_count, "ips": path_ips}

    generate_report(results, REPORT_FILE)
    print("[+] Report generated successfully")

if __name__ == "__main__":
    main()
