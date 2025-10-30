import requests
from bs4 import BeautifulSoup

USERNAME = "AkhileshRawat"
URL = f"https://www.codingninjas.com/codestudio/profile/{USERNAME}"

try:
    page = requests.get(URL, timeout=10)
    soup = BeautifulSoup(page.text, "html.parser")

    # Extract stats — adjust selectors if CodeStudio layout changes
    data = {}
    for div in soup.find_all("div"):
        if "Problems Solved" in div.text:
            data["Problems Solved"] = div.text.strip()
        if "Contest Rating" in div.text:
            data["Contest Rating"] = div.text.strip()
        if "Rank" in div.text:
            data["Rank"] = div.text.strip()

    # Write Markdown summary
    with open("codestudio_stats.md", "w", encoding="utf-8") as f:
        f.write("### 💻 CodeStudio Stats\n")
        for k, v in data.items():
            f.write(f"- **{k}:** {v}\n")

    print("✅ CodeStudio stats updated.")

except Exception as e:
    print("❌ Error fetching data:", e)
