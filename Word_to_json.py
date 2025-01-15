from docx import Document
import json
import re

# Load the Word document
doc = Document('data/Input-Kopie.docx')  # Replace with your file path

# Combine all text into a single string
full_text = "\n".join(paragraph.text for paragraph in doc.paragraphs)

# Split the text into parts whenever "Problem:" or "Lösung:" is found


# Use regex to split by "Problem:" or "Lösung:", keeping the keywords as part of the split text
split_text = re.split(r'(Problem:|Lösung:)', full_text)

# Merge the keywords back with their respective sections
result = []
for i in range(1, len(split_text), 2):
     result.append(split_text[i] + split_text[i+1])

data = []
# Read the content of the Word document
for i in range(0, len(result), 2):
     data.append({"question": result[i], "answer": result[i+1]})

# Save the data to a JSON file
with open('data/output.json', 'w', encoding='utf-8') as f:
     json.dump(data, f, ensure_ascii=False, indent=4)

print("Data successfully converted to JSON!")
