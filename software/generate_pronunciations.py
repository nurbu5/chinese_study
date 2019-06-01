from gtts import gTTS

PRONUNCIATIONS_DIRECTORY = "../data/pronunciations/"

phrase = input('Enter the phrase you\'d like pronounced (or "exit" to quit): ')

for phrase != 'exit':
    tts = gTTS(phrase, lang="zh-cn") #or zh-tw for taiwanese pronunciation
    tts.save(PRONUNCIATIONS_DIRECTORY + phrase + '.mp3')
    phrase = input('Enter the phrase you\'d like pronounced (or "exit" to quit): ')
