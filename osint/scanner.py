import time
import sys


def scan_step(number, label, seconds=5):

    print(f"\n[+] {label}")

    steps = 10

    for i in range(steps + 1):

        percent = int((i / steps) * 100)

        bar = "#" * (i * 2) + "-" * (20 - i * 2)

        sys.stdout.write(
            f"\r    [{bar}] {percent}%"
        )

        sys.stdout.flush()

        time.sleep(seconds / steps)

    print("  DONE")


def run_scan(number):

    scan_step(number, "Validating phone number", 3)
    scan_step(number, "Analysing phone metadata", 4)
    scan_step(number, "Preparing public web searches", 5)
    scan_step(number, "Preparing public code searches", 5)
    scan_step(number, "Building defensive report", 3)
