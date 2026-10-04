from collections import Counter
from datetime import datetime


LOG_FILE = "sample_security.log"


def load_logs():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Log file not found: {LOG_FILE}")
        return []


def analyze_logs(logs):
    failed_logins = []
    source_ips = Counter()

    for entry in logs:
        parts = entry.split()

        if "FAILED_LOGIN" in entry:
            failed_logins.append(entry)

        if "IP=" in entry:
            for part in parts:
                if part.startswith("IP="):
                    source_ips[part.split("=", 1)[1]] += 1

    return failed_logins, source_ips


def generate_alerts(failed_logins, source_ips):
    print("\n=== Security Alerts ===")

    if failed_logins:
        print(f"[ALERT] Failed login attempts: {len(failed_logins)}")
    else:
        print("[OK] No failed login attempts detected.")

    for ip, count in source_ips.items():
        if count >= 3:
            print(f"[ALERT] Repeated activity from {ip}: {count} events")


def main():
    print("Cybersecurity Log Correlation & Alert System")
    print("-" * 45)
    print("Scan started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    logs = load_logs()

    if not logs:
        return

    failed_logins, source_ips = analyze_logs(logs)
    generate_alerts(failed_logins, source_ips)


if __name__ == "__main__":
    main()
