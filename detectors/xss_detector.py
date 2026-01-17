XSS_KEYWORDS = ["<script", "</script", "javascript:", "onerror=", "onload=", "<img"]

def detect_xss(log_file):
    count = 0
    attacker_ips = {}

    with open(log_file, "r") as file:
        for line in file:
            lower_line = line.lower()

            if any(keyword in lower_line for keyword in XSS_KEYWORDS):
                count += 1
                ip = line.split(" ")[0]
                attacker_ips[ip] = attacker_ips.get(ip, 0) + 1

    return count, attacker_ips
