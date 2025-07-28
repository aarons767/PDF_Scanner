from PyPDF2 import PdfReader
from PIL import Image
import pytesseract
import fitz
import tkinter as tk
from tkinter import filedialog

native_pdf = "./resume.pdf"


def main():
    prompter()

def display():
    pyreader = PdfReader(native_pdf)
    string_of_pdf = '' 

    for page in range(len(pyreader.pages)):
        string_of_pdf   += pyreader.pages[page].extract_text()

def prompter():
    window = tk.Tk()

    window.title("Main Window")
    window.geometry("600x400") # Optional: set initial window size
    filepath = filedialog.askopenfilename(
        title="Select a file you want to conver to text",
        filetypes=[("PDF files", "*.pdf")]
    )
    native_pdf = filepath
    display()

if __name__=='__main__':
    main()