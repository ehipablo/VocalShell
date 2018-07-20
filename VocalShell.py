#importo i moduli che mi servono
#DEVI INSTALLARE I MODULI 'PyAudio', 'speech_recognition', 'gtts' e 'webbrowser'
import speech_recognition as spk
from gtts import gTTS 
import subprocess, webbrowser, os

#ESTETICA

print '              .andAHHAbnn.'
print '           .aAHHHAAUUAAHHHAn.'
print '          dHP^~"        "~^THb.'
print '    .   .AHF                YHA.   .'
print '    |  .AHHb.              .dHHA.  |'
print '    |  HHAUAAHAbn      adAHAAUAHA  |'
print '    I  HF~"_____        ____ ]HHH  I'
print '   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH'
print '   HHI HHHD> .andHH  HHUUP^~YHHHH IHH'
print '   YUI ]HHP     "~Y  P~"     THH[ IUP'
print '    "  `HK                   ]HH'  "'
print '        THAn.  .d.aAAn.b.  .dHHP'
print '        ]HHHHAAUP" ~~ "YUAAHHHH['
print '        `HHP^~"  .annn.  "~^YHH''
print '         YHb    ~" "" "~    dHF'
print '          "YAb..abdHHbndbndAP"'
print '           THHAAb.  .adAHHF'
print '            "UHHHHHHHHHHU"'
print '              ]HHUUHHHHHH['
print '            .adHHb "HHHHHbn.'
print '     ..andAAHHHHHHb.AHHHHHHHAAbnn..'
print '.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.'
print '  "~^YUHHP"   "~^YUHHUP"        "^YUP^"'


#cerco il nome dell'utente che utilizza lo script
nome = input("[+] Come ti chiami? ")
print ""
testo1 = 'Ciao'
testo2 = 'sono la tua guida, dammi qualche istruzione, mi annoio!'
testo_finale = testo1 + nome + testo2
parla = 'dimmi tutto caro!'
#TUTTI I COMANDI (DA AMPLIARE)
AllCommands = ['apri il browser', 'apri leafpad', 'www']
print "[+]ALL DEFAULT COMMANDS:"
print ""
print AllCommands[0]
print ""
print AllCommands[1]
print ""
print AllCommands[2]
print ""

#creo il file audio grazie al modulo gtts
tts = gTTS(text=testo_finale, lang='it')
tts.save("tts_output.mp3")

#faccio partire grazie al modulo subprocess l'audio precedentemente salvato
subprocess.run(["audacious", "tts_output.mp3"])
print ""
print ""

tts2 = gTTS(text=parla, lang='it')
tts2.save("tts_output1.mp3")
subprocess.run(["audacious", "tts_output1.mp3"])

recognizer_instance = spk.Recognizer()
with spk.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    audio = recognizer_instance.listen(source)

#sento l'audio e lo trasformo in testo per farlo eseguire da una shell
try:
   command = recognizer_instance.recognize_google(audio, language="it-IT")
   if command == AllCommands[0]:
       subprocess.run(['firefox'])
   elif command == AllCommands[1]:
       subprocess.run(['leafpad'])
   elif AllCommands[2] in command:
       webbrowser.open(command)
   else:
       os.system(command)
except Exception as error:
    print (error)
