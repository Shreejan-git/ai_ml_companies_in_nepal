import csv

CSV_FILE = "companies.csv"
README_FILE = "README.md"

GLOBE_ICON = "https://icons-for-free.com/iff/png/512/globe+international+work+world+icon-1320086521784287131.png"
LINKEDIN_ICON = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg"

companies = []

# Read CSV
with open(CSV_FILE, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        companies.append(row)

# Sort alphabetically
companies = sorted(companies, key=lambda x: x["Company Name"].lower())

# Generate Markdown Table
table = "| S.N | Company Name | Website | LinkedIn |\n"
table += "|----|---------------|----------|----------|\n"

for i, company in enumerate(companies, start=1):
    website_link = f'<a href="{company["Website"]}" target="_blank" rel="noopener noreferrer"><img src="{GLOBE_ICON}" width="20"/></a>' if company["Website"] else ""
    linkedin_link = f'<a href="{company["LinkedIn"]}" target="_blank" rel="noopener noreferrer"><img src="{LINKEDIN_ICON}" width="20"/></a>' if company["LinkedIn"] else ""

    table += f"| {i} | {company['Company Name']} | {website_link} | {linkedin_link} |\n"

# Write README
with open(README_FILE, "w", encoding="utf-8") as readme:
    readme.write("# Nepal AI/ML Companies\n\n")
    readme.write(table)
    readme.write(">\n\n#### This repo uses Github Actions to automatically update `README.md`. Just make changes on `companies.csv` and push the changes.")


print("README updated successfully!")

