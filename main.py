#python audio Book
import PyPDF2
import pyttsx3


book = open("robotic.pdf", "rb") #Add your pdf name here
pdf_reader = PyPDF2.PdfReader(book)
speaker = pyttsx3.init()


speaker.say("Hey, Now I'm reading your PDF file ")
speaker.runAndWait()


pages = len(pdf_reader.pages)
for pageNum in range(pages):
    page = pdf_reader.pages[pageNum]
    text = page.extract_text()
    if text:
        speaker.say(text)
        speaker.runAndWait()

book.close()
