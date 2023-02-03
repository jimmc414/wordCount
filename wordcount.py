import PyPDF2
import collections
import csv
import tkinter as tk
from tkinter import filedialog

# Prompt the user to select a PDF file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

# Open the selected PDF file
with open(file_path, "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    text = ""
    # Extract the text from each page of the PDF
    for i in range(reader.numPages):
        page = reader.getPage(i)
        text += page.extractText()

# Split the text into words
words = text.split()

# Count the frequency of each word
word_counts = collections.Counter(words)

# Sort the word frequency in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Write the word frequency to a CSV file
with open("word_counts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Word", "Frequency"])
    for word, frequency in sorted_word_counts:
        writer.writerow([word, frequency])
