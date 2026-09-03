import json
from datetime import datetime


def save_report(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/osint_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return filename
