SQLI_KEYWORDS = ["'", " OR ", "--", "UNION", "SELECT"]

def detect_sqli(log_file):
    count = 0
    attacker_ips = {}

    with open(log_file, "r") as file:
        for line in file:
            if any(keyword.lower() in line.lower() for keyword in SQLI_KEYWORDS):
                count += 1
                ip = line.split(" ")[0]
                attacker_ips[ip] = attacker_ips.get(ip, 0) + 1

    return count, attacker_ips