#TESTATO su Python 2.7.15

#importo i moduli che mi servono
#DEVI INSTALLARE I MODULI 'PyAudio', 'speech_recognition', 'gtts' e 'webbrowser'
import speech_recognition as spk
from gtts import gTTS 
import subprocess, os, time

#ESTETICA

print '                                  _____'
print '                                 |     |'
print '                                 | | | |'
print '                                 |_____|'
print '                           ____ ___|_|___ ____'
print '                          ()___)         ()___)'
print '                          // /|           |\ \\'
print '                         // / |           | \ \\'
print '                        (___) |___________| (___)'
print '                        (___)   (_______)   (___)'
print '                        (___)     (___)     (___)'
print '                        (___)      |_|      (___)'
print '                        (___)  ___/___\___   | |'
print '                         | |  |           |  | |'
print "                         | |  |___________| /___"
print '                        /___\  |||     ||| //   \\'
print '                       //   \\ |||     ||| \\   //'
print '                       \\   // |||     |||  \\ //'
print '                        \\ // ()__)   (__()'
print '                              ///       |||'
print '                             ///         |||'
print '                           _______     _______'
print '                          |_______|   |_______|'

print ''
#cerco il nome dell'utente che utilizza lo script
nome = raw_input("[+] Come ti chiami? ")
print ""
testo1 = 'Ciao'
testo2 = 'sono la tua guida, dammi qualche istruzione, mi annoio!'
testo_finale = testo1 + nome + testo2
parla = 'dimmi tutto caro!'
#TUTTI I COMANDI (DA AMPLIARE)
AllCommands = ['apri il browser', 'apri leafpad']
print "[+]ALL DEFAULT COMMANDS:"
print ""
print AllCommands[0]
print ""
print AllCommands[1]
print ""


#creo il file audio grazie al modulo gtts
tts = gTTS(text=testo_finale, lang='it')
tts.save("tts_output.mp3")

#faccio partire grazie al modulo subprocess l'audio precedentemente salvato
subprocess.Popen(["audacious", "tts_output.mp3"])
print ""
print ""
time.sleep(10)

tts2 = gTTS(text=parla, lang='it')
tts2.save("tts_output1.mp3")
subprocess.Popen(["audacious", "tts_output1.mp3"])

recognizer_instance = spk.Recognizer()
with spk.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print 'sto ascoltando...'
    audio = recognizer_instance.listen(source)

#sento l'audio e lo trasformo in testo per farlo eseguire da una shell
try:
   command = recognizer_instance.recognize_google(audio, language="it-IT")
   if command == AllCommands[0]:
	   subprocess.Popen(['firefox'])
   if command == AllCommands[1]:
       subprocess.Popen(['leafpad'])
   elif AllCommands[2] in command:
       subprocess.Popen(command)
   else:
       os.system(command)
except Exception as error:
       print (error)
