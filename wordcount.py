import PyPDF2
from collections import Counter
import string
import nltk
nltk.download("words")
from nltk.corpus import words
import pyperclip

filename = input("Enter the filename: ")
with open(filename, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    words = []
    for page_num in range(pdf_reader._get_num_pages()):
        page = pdf_reader._get_page(page_num)
        text = page.extract_text().strip().split()
        words.extend(text)

    words = [word.lower().translate(str.maketrans("", "", string.punctuation)) for word in words]
    word_counts = Counter(words)

    english_words = set(nltk.corpus.words.words())
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    result = []
    for word, count in sorted_words:
        if word in english_words:
            result.append(word)

    result_str = '\n'.join(result)
    print(result_str)

    with open('words.txt', 'w') as f:
        f.write(result_str)

    pyperclip.copy(result_str)
