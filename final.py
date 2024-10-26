import pymupdf
import sys
import freetype
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk,ImageFont
import tkinter.font as tkfont
from tkinter import font

# Get the default font

# Load a custom font from a file
custom_font_path = "noto_light.ttf"
custom_font = ImageFont.truetype(custom_font_path, 60)



all_rules = {
    "post-rules": [ ["(.)र्",r"र्\1"] , ["्ा", ""], ["(त्र|त्त)([^उभप]+?)m", r"\1m\2"], ["त्रm", "क्र"], ["त्तm", "क्त"], ["([^उभप]+?)m", r"m\1"], ["उm", "ऊ"], ["भm", "झ"], ["पm", "फ"], ["इ{", "ई"], ["ि((.्)*[^्])", r"\1ि"], ["(.[ािीुूृेैोौंःँ]*?){", r"{\1"], ["((.्)*){", r"{\1"], ["{", "र्"], ["([ाीुूृेैोौंःँ]+?)(्(.्)*[^्])", r"\2\1"], ["्([ाीुूृेैोौंःँ]+?)((.्)*[^्])", r"्\2\1"], ["([ंँ])([ािीुूृेैोौः]*)", r"\2\1"], ["ँँ", "ँ"], ["ंं", "ं"], ["ेे", "े"], ["ैै", "ै"], ["ुु", "ु"], ["ूू", "ू"], ["^ः", ":"], ["टृ", "ट्ट"], ["ेा", "ाे"], ["ैा", "ाै"], ["अाे", "ओ"], ["अाै", "औ"], ["अा", "आ"], ["एे", "ऐ"], ["ाे", "ो"], ["ाै", "ौ"]],
    "char-map": {
      "÷": "/", "v": "ख", "r": "च", "\"": "ू", "~": "ञ्", "z": "श", "ç": "ॐ", "f": "ा", "b": "द", "n": "ल", "j": "व", "×": "×", "V": "ख्", "R": "च्", "ß": "द्म", "^": "६", "Û": "!", "Z": "श्", "F": "ँ", "B": "द्य", "N": "ल्", "Ë": "ङ्ग", "J": "व्", "6": "ट", "2": "द्द", "¿": "रू", ">": "श्र", ":": "स्", "§": "ट्ट", "&": "७", "£": "घ्", "•": "ड्ड", ".": "।", "«": "्र", "*": "८", "„": "ध्र", "w": "ध", "s": "क", "g": "न", "æ": "“", "c": "अ", "o": "य", "k": "प", "W": "ध्", "Ö": "=", "S": "क्", "Ò": "¨", "_": ")", "[": "ृ", "Ú": "’", "G": "न्", "ˆ": "फ्", "C": "ऋ", "O": "इ", "Î": "ङ्ख", "K": "प्", "7": "ठ", "¶": "ठ्ठ", "3": "घ", "9": "ढ", "?": "रु", ";": "स", "'": "ु", "#": "३", "¢": "द्घ", "/": "र", "+": "ं", "ª": "ङ", "t": "त", "p": "उ", "|": "्र", "x": "ह", "å": "द्व", "d": "म", "`": "ञ", "l": "ि", "h": "ज", "T": "त्", "P": "ए", "Ý": "ट्ठ", "\\": "्", "Ù": ";", "X": "ह्", "Å": "हृ", "D": "म्", "@": "२", "Í": "ङ्क", "L": "ी", "H": "ज्", "4": "द्ध", "±": "+", "0": "ण्", "<": "?", "8": "ड", "¥": "र्‍", "$": "४", "¡": "ज्ञ्", ",": ",", "©": "र", "(": "९", "‘": "ॅ", "u": "ग", "q": "त्र", "}": "ै", "y": "थ", "e": "भ", "a": "ब", "i": "ष्", "‰": "झ्", "U": "ग्", "Q": "त्त", "]": "े", "˜": "ऽ", "Y": "थ्", "Ø": "्य", "E": "भ्", "A": "ब्", "M": "ः", "Ì": "न्न", "I": "क्ष्", "5": "छ", "´": "झ", "1": "ज्ञ", "°": "ङ्ढ", "=": ".", "Æ": "”", "‹": "ङ्घ", "%": "५", "¤": "झ्", "!": "१", "-": "(", "›": "द्र", ")": "०", "…": "‘", "Ü": "%"
    }
}



document = pymupdf.open(sys.argv[1])
root = tk.Tk()
custom_font_tk = font.Font(family="NotoSansDevanagari", size=40)


keyToNep = {
  
  "a": "\u093E", # ा
  "b": "\u092C", # ब
  "c": "\u091A", # च

  "d": "\u0926", # द
  "e": "\u0947", # े
  "f": "\u0909", # उ
  "g": "\u0917", # ग
  "h": "\u0939", # ह
  "i": "\u093F", # ि
  "j": "\u091C", # ज
  "k": "\u0915", # क
  "l": "\u0932", # ल
  "m": "\u092E", # म
  "n": "\u0928", # न
  "o": "\u094B", # ो
  "p": "\u092A", # प
  "q": "\u091F", # ट
  "r": "\u0930", # र
  "s": "\u0938", # स
  "t": "\u0924", # त
  "u": "\u0941", # ु
  "v": "\u0935", # व
  "w": "\u094C", # ौ
  "x": "\u0921", # ड
  "y": "\u092F", # य
  "z": "\u0937", # ष
  #
  "A": "\u0906", # आ
  "B": "\u092D", # भ
  "C": "\u091B", # छ
  "D": "\u0927", # ध
  "E": "\u0948", # ै
  "F": "\u090A", # ऊ
  "G": "\u0918", # घ
  "H": "\u0905", # अ
  "I": "\u0940", # ी
  "J": "\u091D", # झ
  "K": "\u0916", # ख
  "L": "\u0933", # ळ
  "M": "\u0902", # ं
  "N": "\u0923", # ण
  "O": "\u0913", # ओ
  "P": "\u092B", # फ
  "Q": "\u0920", # ठ
  "R": "\u0943", # ृ
  "S": "\u0936", # श
  "T": "\u0925", # थ
  "U": "\u0942", # ू
  "V": "\u0901", # ँ
  "W": "\u0914", # औ
  "X": "\u0922", # ढ
  "Y": "\u091E", # ञ
  "Z": "\u090B", # ऋ
  #
  "0": "\u0966", # ०
  "1": "\u0967", # १
  "2": "\u0968", # २
  "3": "\u0969", # ३
  "4": "\u096A", # ४
  "5": "\u096B", # ५
  "6": "\u096C", # ६
  "7": "\u096D", # ७
  "8": "\u096E", # ८
  "9": "\u096F", # ९
  #
  "^": "\u005E", # ^
  #
  "`": "\u093D", # ऽ
  "~": "\u093C", # ़
  #
  "_": "\u0952", # ॒
  #
  "+": "\u200C", # ZWNJ
  "=": "\u200D", # ZWJ
  #
  "[": "\u0907", # इ
  "{": "\u0908", # ई
  #
  "]": "\u090F", # ए
  "}": "\u0910", # ऐ
  #
  "\\": "\u0950", # ॐ
  "|": "\u0903", # ः
  #
  "<": "\u0919", # ङ
  #
  ".": "\u0964", # ।
  ">": "\u0965", # ॥
  #
  "/": "\u094D", # ्
  "?": "\u003F", # ?
};

def getAllFonts():

    fontSet = set()
    all_common = get_all_commo_fonts()
    fonts_added = []
    for i in range(document.page_count):
        fonts = document.get_page_fonts(0, full=True)
        for font in fonts:

            name =  font[3].split("+")
            if len(name)>1  and font[3] not in all_common:
                name = name[1]
                font = (font[0],font[1],font[2],name,font[4],font[5])
            if name not in fonts_added:
                fonts_added.append(name)
                fontSet.add(font)
        # page = document
    # print(all_common)
    # print(fontSet)
    # exit()
    # print(fontSet)
    return fontSet

def printAllFonts(fonts):
    for font in fonts:
        print(f"{font[0]}. {font[3]} {font[4]}")


def getFace(font_index):

    font_dict = document.extract_font(font_index)
    font_file_name = font_dict[0]+"-"+str(font_index)+"."+font_dict[1]
    
    with open(font_file_name,"wb") as f:
        f.write(font_dict[3])

    face = freetype.Face(font_file_name)
    return face


def create_glyph_image_by_gid(gid,char, face, font_size):

    # imageChar = Image.new("RGB", (150,100), (255, 255, 255))
    # draw = ImageDraw.Draw(imageChar)
    #     # print(char)
    # draw.text((10, 10), char, font=custom_font, fill=(0, 0, 0))

    # photo = ImageTk.PhotoImage(imageChar)
    # return photo
    face.set_pixel_sizes(0, font_size)
    # print(gid)
    face.load_glyph(gid, freetype.FT_LOAD_RENDER)

    bitmap = face.glyph.bitmap
    if bitmap.buffer:
        image = Image.frombytes('L', (bitmap.width, bitmap.rows),bytes( bitmap.buffer), 'raw', 'L', bitmap.pitch)
        
        return ImageTk.PhotoImage(image)
    else:
        # print("nothing")
        # Return a placeholder image if no bitmap is available
        image = Image.new("L", (font_size, font_size), "white")
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), "N/A", fill="black")
        return ImageTk.PhotoImage(image)

def get_all_commo_fonts():
    all_fonts = []
    for i in range(document.page_count):
        page = document[i]
        page_content = page.get_texttrace()

        for span in page_content:
            font = span["font"]

            if font not in all_fonts:
                all_fonts.append(font)
    # exit()
    return all_fonts



import os  
def get_all_gid_used():
    file_name = sys.argv[1]+".json"
    if os.path.exists(file_name):
        with open(file_name,"r") as f:
            data = json.loads(f.read() )
            # print(data)
            return data
    gid_to_char = {}
    for i in range(document.page_count):
        page = document[i]
        page_content = page.get_texttrace()

        for span in page_content:
            font = span["font"]
            chars = span["chars"]
            # print(font)
            # exit()
        
            for char in chars:
                unicode_char = chr( char[0] )
                gid = char[1]
                if gid==-1:continue

                if not font in gid_to_char:
                    gid_to_char[font] = {"is_preeti":False}
                gid_to_char[font][str(gid)] = unicode_char

    # print(gid_to_char)
    # exit()
    return gid_to_char


def get_all_glyph_images(all_gid_maps,font_name,font_index):
    images = []
    fonts_gids = all_gid_maps[font_name]
    face = getFace(font_index) #for kalimati
  
    for gid in fonts_gids.keys():
        # print(gid)
        # if gid==105:
            # print("Yes")
        # gid = gid+""
        # gid = 105
        if gid == -1 or gid=="-1" or gid == "is_preeti":continue
        # gid = int(gid)
        glyph_image = create_glyph_image_by_gid(int(gid),fonts_gids[gid],face,60)
        images.append([fonts_gids[gid],glyph_image,gid])
        
     
    return images


def create_scrollable_list(items,list_frame,font_name,font_index):
    global all_gids


    font_dict = document.extract_font(font_index)
    font_file_name = font_dict[0]+"-"+str(font_index)+"."+font_dict[1]
    custom_font_current = ImageFont.truetype(font_file_name, 60)

    
    # Clear previous content in the frame if any
    for widget in list_frame.winfo_children():
        widget.destroy()

    default_font = tkfont.nametofont("TkDefaultFont")

# Set a new size for the default font
    default_font.configure(size=40)

    # Create a canvas to enable scrolling
    canvas = tk.Canvas(list_frame)
    scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    imagesList = []

    # Populate the scrollable frame with rows of images and text inputs
    for index, item in enumerate(items):
        # Load a placeholder image (replace 'image.png' with your image paths)
        # img = Image.open("image.png").resize((50, 50))  # Placeholder image
        img = item[1]
        char = item[0]
        gid = item[2]
        total_cols = 1
        total_groups = 3
        row = int(index/total_cols) 
        col = (index % total_cols)* total_groups

        
        # 0,1*,2,3*,4,5*
        # row =2 , total = 4, 
        
        # print(f"{index}={row}| {col}")

        # Create label for the image
       

        

 # Create StringVar to track text changes in Entry widget
        entry_var = tk.StringVar(value=char)

        # Define the callback for text changes
        def on_text_change(event):
            # print(f"Text changed: {entry_var.get()}")  # Log or process the change
            print(event.widget.get() )
            data = event.widget.id
            id = data["index"]
            
            entry_text = event.widget.get()
            converted = ""
            
            for ch in entry_text:
                try:
                    converted = converted + keyToNep[ch]
                except Exception as e:
                    converted = converted + ch
            # event.widget.delete(0, tk.END)
            # event.widget.insert(0,converted)


            imageChar = Image.new("RGB", (100,100), (255, 255, 255))
            draw = ImageDraw.Draw(imageChar)
        # print(char)
            draw.text((10, 10), converted, font=custom_font_current, fill=(0, 0, 0))

            photo = ImageTk.PhotoImage(imageChar)
            # photo.id = id
            all_gids[font_name][data["gid"]]  = converted
            # print(all_gids)
            label = imagesList[id]
            label.image = photo
            label.config(image=photo)


        # Attach the trace method to detect changes in the input field
        entry_var.trace_add('write', on_text_change)
        
        label = tk.Label(scrollable_frame, text=f"      ")
        label.grid(row=row, column=col+2, padx=30, pady=5)  # Position for the label
#  textvariable=entry_var,

        # Create text input field with padding
        # text_entry = tk.Text(scrollable_frame, wrap="word",padx=20,pady=10, font=custom_font_tk, height=1, width=4)
        text_entry = tk.Entry(scrollable_frame,font=custom_font_tk,width=5, highlightthickness=1,fg="white",bg="white", highlightbackground="black")
        text_entry.grid(row=row, column=col+1, padx=0, pady=5, ipadx=0, ipady=0,)  # Adding internal padding
        

        img_label = tk.Label(scrollable_frame, image=img)
        img_label.image = img  # Keep a reference to avoid garbage collection
        img_label.grid(row=row, column=col, padx=5, pady=5)




        imageChar = Image.new("RGB", (100,100), (255, 255, 255))
        draw = ImageDraw.Draw(imageChar)
        # print(char)
        draw.text((10, 10), char, font=custom_font_current, fill=(0, 0, 0))

        photo = ImageTk.PhotoImage(imageChar)
        photo.id = index


        img_label_char = tk.Label(scrollable_frame, image=photo)

        imagesList.append(img_label_char)

        img_label_char.image = photo  # Keep a reference to avoid garbage collection


        
        img_label_char.grid(row=row, column=col+1, padx=5, pady=5)
        # canvas.tag_raise("preview")

        # text_entry.insert(0,char)
        text_entry.id = {"index":index,"gid":gid}
        text_entry.bind("<KeyRelease>",on_text_change)
  
    # Place the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="left", fill="y")



def getFontName(name):
    splitted = name.split("+")
    if len(splitted) >1:
        return splitted[1]
    else:
        return name

import re

def apply_replacement_rules(text, rules):
    for pattern, replacement in rules:
        text = re.sub(pattern, replacement, text)
    return text



def convertToText():
    total_pages = document.page_count
    prevX = 0
    combined_text = ""
    previous = -1

    for page_no in range(1):
        page = document[page_no]
        page_text = page.get_texttrace()
        dublicacy = []

        for span in page_text:

            font = span["font"]
            mapping = all_gids[font]
            # print(mapping)
            # exit()
            chars = span["chars"]
            size = span["size"]
            spacewidth = 5
            is_preeti = mapping["is_preeti"]
            # print(is_preeti)
            
            # if mapping["is_preeti"]:
            #     mapping = all_rules['char-map']


            for char in chars:
                unichar,gid,location,bbox = char
                temp = round( location[1] )
                searchPos = f"{location[0]} {location[1]} {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}"
                if  round(bbox[0]) - prevX > 9:
                    
                    combined_text  = combined_text + " "
                    # print(f"{round(bbox[0])} {prevX}")
                prevX = round( bbox[2] )
                if searchPos in dublicacy:
                    continue
                else:
                    dublicacy.append(searchPos)
                if abs( previous - temp ) > 5:
                # if temp !=previous:
                    total_spaces = round( round(location[0])/round(spacewidth) ) * " "
                    combined_text = combined_text + "\n" + total_spaces
                    previous = temp
                try:
                    if is_preeti:
                        # print("Hello world")
                        unicode = all_rules['char-map'][ chr(char[0]) ]
                    else:
                        unicode = mapping[str(char[1])]
                        # print(unicode)
                        # input()

                    x0, y0, x1, y1 = bbox
                    # char_count = char_count + 1
                

                    combined_text  = combined_text + unicode
                    # print(f"{unicode}")

                except Exception as e:
                    # exit()
                    if char[1] !=-1:
                        # print(e)
                        # notFoundMap[char[1]] = chr(char[0])
                        combined_text  = combined_text + chr(char[0])
                        # print(f"Exception for {chr(char[0])} with gid {char[1]}")
    combined_text = apply_replacement_rules(combined_text,all_rules["post-rules"])
    return combined_text

# Function to handle dropdown selection
def on_select(event):
    global current_font_name
    selected_option = dropdown_var.get()
    splitted = selected_option.split("*")

    current_font_name = splitted[0]
    is_Preeti = all_gids[current_font_name]["is_preeti"]
    checkbox_var.set(is_Preeti)

    images = get_all_glyph_images(all_gids,splitted[0],int(splitted[1]))

    create_scrollable_list(images,list_frame,splitted[0],int(splitted[1]))


# Dropdown menu
fonts = list( getAllFonts() )

printAllFonts(fonts)

# all_fonts = getAllFonts()


# name = fonts[3]
options_frame = tk.Frame(root)
options_frame.pack()
# print(fonts)
dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(options_frame, textvariable=dropdown_var, values=[ font[3]+"*"+str(font[0]) for font in fonts])
dropdown.bind("<<ComboboxSelected>>", on_select)
dropdown.grid(row=0,column=0,pady=20)
dropdown.set(fonts[0][3])
# # Frame for the scrollable list
import json

def on_save_click():
    with open(sys.argv[1]+".json","w") as f:
        f.write(json.dumps(all_gids,indent=5,ensure_ascii=False))
    print("Layout is saved!")


button = tk.Button(options_frame, text="Save Layout", command=on_save_click)

# Add the button to the window
button.grid(row=0,column=1,padx=20)  # You can use pack(), grid(), or place() to add it to the layout
def on_convert_click():
    print("Converting!")
    on_save_click()
    converted_text = convertToText()
    with open(sys.argv[1]+".txt","w") as f:
        f.write(converted_text)
    print("Converted")

button = tk.Button(options_frame, text="Convert", command=on_convert_click)

# Add the button to the window
button.grid(row=0,column=2)  # You can use pack(), grid(), or place() to add it to the layout


checkbox_var = tk.BooleanVar()

# Define the function that will run when the checkbox is toggled
def on_checkbox_toggle():
    all_gids[current_font_name]["is_preeti"] = checkbox_var.get()
    # print("Checkbox state:", checkbox_var.get())

# Create the checkbox
checkbox = tk.Checkbutton(options_frame, text="is_Preeti",
                          variable=checkbox_var, command=on_checkbox_toggle)
checkbox.grid(row=0,column=3)


list_frame = tk.Frame(root)
list_frame.pack(fill="both", expand=True)


all_gids = get_all_gid_used()

current_font = fonts[0]
current_font_name = current_font[3]
images = get_all_glyph_images(all_gids,current_font_name,current_font[0])

is_Preeti = all_gids[current_font_name]["is_preeti"]
checkbox_var.set(is_Preeti)


create_scrollable_list(images,list_frame,current_font[3],current_font[0])

root.mainloop()




# root.mainloop()
