import argparse

from osint.validator import analyze_number
from osint.public_search import build_searches
from osint.risk import calculate_risk
from osint.scanner import run_scan
from osint.report import save_report


VERSION = "1.0.0"

BANNER = r"""
╔══════════════════════════════════════════╗
║                                          ║
|         AMMAAR CYBER WARRIOR             |
║          PHONE OSINT ENGINE              ║
║                                          ║
║     ETHICAL • PASSIVE • DEFENSIVE        ║
║ Whatsapp Hacking tool commingsoon...     ║
╚══════════════════════════════════════════╝
"""


def mask_number(number):
    if len(number) <= 7:
        return "*" * len(number)

    return number[:4] + "*" * (len(number) - 7) + number[-3:]


def main():

    parser = argparse.ArgumentParser(
        description="Ammaar Cyber Warrior Defensive Phone OSINT"
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show tool version"
    )

    parser.add_argument(
        "--number",
        help="Phone number in international format"
    )

    parser.add_argument(
        "--name",
        help="Your name for self-OSINT"
    )

    args = parser.parse_args()

    if args.version:
        print(f"Ammaar Cyber Warrior Phone OSINT v{VERSION}")
        return

    print(BANNER)

    number = args.number

    if not number:
        number = input("Enter phone number: ").strip()

    name = args.name

    if name is None:
        name = input(
            "Your name (optional, OSINT): "
        ).strip()

    print("\n[+] Starting  OSINT scan")

    run_scan(number)

    print("\n[+] Analysing phone metadata")

    result = analyze_number(number)

    if "error" in result:
        print("\n[!] Invalid input")
        print(result["error"])
        return

    searches = build_searches(
        result["international"],
        name if name else None
    )

    risk = calculate_risk(0)

    print("""
────────────────────────────────────────────
 PHONE ANALYSIS
────────────────────────────────────────────
""")

    print(
        f"Number       : "
        f"{mask_number(result['international'])}"
    )

    print(
        f"Country      : "
        f"{result['country'] or 'Unknown'}"
    )

    print(
        f"Valid        : "
        f"{'YES' if result['valid'] else 'NO'}"
    )

    print(
        f"Possible     : "
        f"{'YES' if result['possible'] else 'NO'}"
    )

    print(f"Type         : {result['type']}")
    print(f"Carrier      : {result['carrier']}")

    print("""
────────────────────────────────────────────
 IDENTITY
────────────────────────────────────────────
""")

    if name:
        print(f"User supplied : {name}")

    print("Automatic owner identification :DISABLED")
    print("Reason                        : Privacy protection")

    print("""
────────────────────────────────────────────
 REAL PUBLIC SEARCH LINKS
────────────────────────────────────────────
""")

    for index, item in enumerate(searches, 1):

        print(f"[{index}] {item['source']}")
        print(f"    Query: {item['query']}")
        print(f"    URL  : {item['url']}")
        print()

    print("""
────────────────────────────────────────────
 EXPOSURE
────────────────────────────────────────────
""")

    print("Automatic public-result count : UNAVAILABLE")
    print(f"Initial exposure score         : {risk['score']}/100")
    print(f"Risk level                     : {risk['level']}")

    report = {
        "tool": "Ammaar Cyber Warrior Phone OSINT Engine",
        "version": VERSION,
        "mode": "Defensive Self-OSINT",
        "phone": {
            "masked": mask_number(result["international"]),
            "country": result["country"],
            "valid": result["valid"],
            "possible": result["possible"],
            "type": result["type"],
            "carrier": result["carrier"]
        },
        "identity": {
            "user_supplied_name": name if name else None,
            "automatic_owner_identification": True
        },
        "public_searches": searches,
        "exposure": {
            "automatic_result_count": None,
            "risk_score": risk["score"],
            "risk_level": risk["level"]
        }
    }

    filename = save_report(report)

    print("""
────────────────────────────────────────────
 REPORT
────────────────────────────────────────────
""")

    print(f"[+] JSON report saved: {filename}")

    print("""
============================================
 Created by Ammaar Cyber Warrior
 Ammaar Cyber Security
 Ethical OSINT • Defensive Security
============================================
""")


if __name__ == "__main__":
    main()

