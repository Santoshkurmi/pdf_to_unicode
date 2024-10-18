import fitz  # PyMuPDF
import re
import sys
import pyperclip
# pip install pymupdf
# Open a PDF file

printFonts = False
no_of_pages_to_print = 0
print_in_terminal = False
convertToUnicodeFromPreetiFonts = ["Preeti","CIDFont+F4"]

filename = sys.argv[1]
doc = fitz.open(filename)

all_rules = {
    "post-rules": [["्ा", ""], ["(त्र|त्त)([^उभप]+?)m", r"\1m\2"], ["त्रm", "क्र"], ["त्तm", "क्त"], ["([^उभप]+?)m", r"m\1"], ["उm", "ऊ"], ["भm", "झ"], ["पm", "फ"], ["इ{", "ई"], ["ि((.्)*[^्])", r"\1ि"], ["(.[ािीुूृेैोौंःँ]*?){", r"{\1"], ["((.्)*){", r"{\1"], ["{", "र्"], ["([ाीुूृेैोौंःँ]+?)(्(.्)*[^्])", r"\2\1"], ["्([ाीुूृेैोौंःँ]+?)((.्)*[^्])", r"्\2\1"], ["([ंँ])([ािीुूृेैोौः]*)", r"\2\1"], ["ँँ", "ँ"], ["ंं", "ं"], ["ेे", "े"], ["ैै", "ै"], ["ुु", "ु"], ["ूू", "ू"], ["^ः", ":"], ["टृ", "ट्ट"], ["ेा", "ाे"], ["ैा", "ाै"], ["अाे", "ओ"], ["अाै", "औ"], ["अा", "आ"], ["एे", "ऐ"], ["ाे", "ो"], ["ाै", "ौ"]],
    "char-map": {
      "÷": "/", "v": "ख", "r": "च", "\"": "ू", "~": "ञ्", "z": "श", "ç": "ॐ", "f": "ा", "b": "द", "n": "ल", "j": "व", "×": "×", "V": "ख्", "R": "च्", "ß": "द्म", "^": "६", "Û": "!", "Z": "श्", "F": "ँ", "B": "द्य", "N": "ल्", "Ë": "ङ्ग", "J": "व्", "6": "ट", "2": "द्द", "¿": "रू", ">": "श्र", ":": "स्", "§": "ट्ट", "&": "७", "£": "घ्", "•": "ड्ड", ".": "।", "«": "्र", "*": "८", "„": "ध्र", "w": "ध", "s": "क", "g": "न", "æ": "“", "c": "अ", "o": "य", "k": "प", "W": "ध्", "Ö": "=", "S": "क्", "Ò": "¨", "_": ")", "[": "ृ", "Ú": "’", "G": "न्", "ˆ": "फ्", "C": "ऋ", "O": "इ", "Î": "ङ्ख", "K": "प्", "7": "ठ", "¶": "ठ्ठ", "3": "घ", "9": "ढ", "?": "रु", ";": "स", "'": "ु", "#": "३", "¢": "द्घ", "/": "र", "+": "ं", "ª": "ङ", "t": "त", "p": "उ", "|": "्र", "x": "ह", "å": "द्व", "d": "म", "`": "ञ", "l": "ि", "h": "ज", "T": "त्", "P": "ए", "Ý": "ट्ठ", "\\": "्", "Ù": ";", "X": "ह्", "Å": "हृ", "D": "म्", "@": "२", "Í": "ङ्क", "L": "ी", "H": "ज्", "4": "द्ध", "±": "+", "0": "ण्", "<": "?", "8": "ड", "¥": "र्‍", "$": "४", "¡": "ज्ञ्", ",": ",", "©": "र", "(": "९", "‘": "ॅ", "u": "ग", "q": "त्र", "}": "ै", "y": "थ", "e": "भ", "a": "ब", "i": "ष्", "‰": "झ्", "U": "ग्", "Q": "त्त", "]": "े", "˜": "ऽ", "Y": "थ्", "Ø": "्य", "E": "भ्", "A": "ब्", "M": "ः", "Ì": "न्न", "I": "क्ष्", "5": "छ", "´": "झ", "1": "ज्ञ", "°": "ङ्ढ", "=": ".", "Æ": "”", "‹": "ङ्घ", "%": "५", "¤": "झ्", "!": "१", "-": "(", "›": "द्र", ")": "०", "…": "‘", "Ü": "%"
    }
}

def apply_replacement_rules(text, rules):
    for pattern, replacement in rules:
        text = re.sub(pattern, replacement, text)
    return text


# Iterate over the pages of the PDF
if no_of_pages_to_print==0:
    total_pages = doc.page_count
else:
    total_pages = no_of_pages_to_print

con_text = ""
for page_num in range(total_pages):
    page = doc[page_num]  # Get the specific page
    blocks = page.get_text("dict")["blocks"]  # Extract blocks using dict format
    
    # Loop through all the blocks
    for block in blocks:
        if "lines" in block:  # Check if the block contains text lines
            for line in block["lines"]:
                # Loop through spans in each line
                for span in line["spans"]:
                    font = span["font"]   # Get the font name (e.g., Preeti)
                    text = span["text"]   # Get the actual text of the span
                    size = span["size"]   # Get font size (optional, can be useful)
                    
                    # Print font and text for each span
                    if printFonts:
                        print(font,text)
                    if font in convertToUnicodeFromPreetiFonts:
                        temp = ""
                        for char in text:
                            try:
                                
                                temp = temp + all_rules['char-map'][char]
                            except Exception as e:
                                temp = temp + char
                        con_text = con_text + apply_replacement_rules(temp,all_rules["post-rules"])
                    else:
                        con_text = con_text + text 
                con_text = con_text + "\n"
            

pyperclip.copy(con_text)

with open(filename.replace(".pdf",".txt"),"w") as f:
    f.write(con_text)    


if print_in_terminal:
    print(con_text)
