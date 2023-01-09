import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('Swapnil_Verlekar.pdf','rb'), strict=False)
speaker = pyttsx3.init()

for page_no in pdfreader.pages:
    text = page_no.extract_text()
    clean_text = text.strip().replace('\n',' ')
    print(clean_text)
speaker.setProperty('rate',175)
speaker.say(clean_text)
speaker.runAndWait()
speaker.stop()

