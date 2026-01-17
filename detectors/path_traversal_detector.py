PATH_TRAVERSAL_KEYWORDS = ["../", "..\\", "..%2f", "..%2F", "/etc/passwd", "/etc/shadow", "config.php"]

def detect_path_traversal(log_file):
    count = 0
    attacker_ips = {}

    with open(log_file, "r") as file:
        for line in file:
            lower_line = line.lower()

            if any(keyword.lower() in lower_line for keyword in PATH_TRAVERSAL_KEYWORDS):
                count += 1
                ip = line.split(" ")[0]
                attacker_ips[ip] = attacker_ips.get(ip, 0) + 1

    return count, attacker_ips
