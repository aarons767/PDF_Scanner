
import requests
from IPython.display import HTML, display
from flask import Flask
from PyPDF2 import PdfReader
from PIL import Image

print("!!!!!!!!!We back mff. lets get started!!!")
app = Flask(__name__)

def main():
    opener = open("text.txt", "r")
    file = opener.read()
    print(file)
    opener.close()

    url = "https://google.com"
    response = requests.get(url)
    print(response)

@app.route("/")
def home():
    return "Hi from Fask on my Mac!"

if __name__ == "__main__":
    app.run()




