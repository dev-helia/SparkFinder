# Importion
import requests # request for website
from bs4 import BeautifulSoup # parse HTML
import csv # exportion data

# Read Keywords
# Open keywords.txt: read your keywords you wanna search
with open("keywords.txt", "r") as f:
    keywords = [kw.strip().lower() for kw in f.readlines()]

# MIT BCS (static site)
url = "https://bcs.mit.edu/research/labs"

# Send a request for web content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 找到实验室的 HTML 块（妈咪在网页里按F12看到了是 views-row）
labs = soup.find_all("div", class_="views-row")

# 打开一个CSV文件准备写入
with open("results.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Lab Name", "Link", "Matched Keyword"])

    # 遍历每个实验室
    for lab in labs:
        a_tag = lab.find("a")
        if a_tag:
            name = a_tag.get_text(strip=True)
            link = a_tag["href"]
            full_link = "https://bcs.mit.edu" + link  # 有的链接不完整

            # 匹配关键词
            match = [kw for kw in keywords if kw in name.lower()]
            if match:
                writer.writerow([name, full_link, ", ".join(match)])
