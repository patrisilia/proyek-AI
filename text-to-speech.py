from gtts import gTTS #pip install gTTS

kalimat = input("masuka kata: ")

bahasa = "id"

filesaya = gTTS(text=kalimat, lang=bahasa)

filesaya.save("sampel.mp3")
print("File Tersimpan")
