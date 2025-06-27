import os
import re
import json

# Base directory containing the HTML files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Output file that will contain the search index as JavaScript
OUTPUT_PATH = os.path.join(BASE_DIR, "search_index.js")

# Function to strip HTML tags and normalise the text
def strip_html_tags(html):
    # Remove content inside <script> and <style> tags
    html = re.sub(r'(?s)<(script|style).*?>.*?</\1>', '', html)
    # Remove all other HTML tags
    html = re.sub(r'<.*?>', '', html)
    # Collapse multiple whitespace characters into a single space
    html = re.sub(r'\s+', ' ', html)
    return html.strip()

# List to hold the search index
search_index = []

# Recursive traversal of the BASE_DIR
for root, _, files in os.walk(BASE_DIR):
    for file in files:
        # Only process .html files
        if file.endswith(".html"):
            full_path = os.path.join(root, file)
            content = None

            # First attempt: open using UTF-8 encoding
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                # If it fails: fall back to CP1252 (Windows-1252)
                try:
                    with open(full_path, "r", encoding="cp1252") as f:
                        content = f.read()
                    print("Warning: Used CP1252 for {}".format(full_path))
                except Exception as e:
                    print("Failed to process {}: {}".format(full_path, e))
                    continue

            # Clean the HTML
            text = strip_html_tags(content)

            # Get path relative to BASE_DIR
            rel_path = os.path.relpath(full_path, start=BASE_DIR).replace("\\", "/")

            # Add entry to the index
            search_index.append({
                "file": rel_path,
                "text": text.replace('"', '\\"')  # Escape double quotes
            })

# Write the index to the JavaScript file
with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
    out.write("const searchIndex = ")
    json.dump(search_index, out, ensure_ascii=False, indent=2)
    out.write(";")

print("Index written to {}".format(OUTPUT_PATH))
