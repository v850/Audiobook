import pyttsx3
import PyPDF2
book=open("unit 3.1.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init('sapi5')
# male voice- voices[0]
# Female voice-- voices[1]
speaker.say("Press 0 for male voice or press 1 for female voice ")
speaker.runAndWait()
n=int(input())
voices=speaker.getProperty('voices')
if(n==0):
    speaker.setProperty('voice',voices[0].id)
else:
    speaker.setProperty('voice',voices[1].id)

for i in range(pages):
    page=pdfReader.getPage(i)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()