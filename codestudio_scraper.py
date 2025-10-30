import requests
from bs4 import BeautifulSoup
import datetime

# Your CodeStudio profile URL
PROFILE_URL = "https://www.naukri.com/code360/profile/9ab92edb-7b65-4d09-a6ae-afcf126f9973"
OUTPUT_FILE = "codestudio_stats.md"

def fetch_codestudio_stats():
    try:
        response = requests.get(PROFILE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        stats = {
            "problems_solved": None,
            "accuracy": None,
            "rank": None
        }

        # Try to find problem count
        problem_section = soup.find_all("p")
        for p in problem_section:
            text = p.text.strip()
            if "Problems Solved" in text:
                stats["problems_solved"] = text.split(":")[-1].strip()
            if "Accuracy" in text:
                stats["accuracy"] = text.split(":")[-1].strip()
            if "Rank" in text:
                stats["rank"] = text.split(":")[-1].strip()

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(f"### 🧠 CodeStudio Stats (Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n\n")
            f.write("| Metric | Value |\n|--------|--------|\n")
            for key, val in stats.items():
                f.write(f"| {key.replace('_', ' ').title()} | {val or 'N/A'} |\n")

        print("✅ CodeStudio stats updated successfully!")

    except Exception as e:
        print(f"❌ Error fetching stats: {e}")

if __name__ == "__main__":
    fetch_codestudio_stats()
