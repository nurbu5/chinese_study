from gtts import gTTS

ANKI_MEDIA_DIRECTORY = '/Users/dawasherpa/Library/Application Support/Anki2/User 1/collection.media/'
#ANKI_MEDIA_DIRECTORY = "./tempDir/" #Temporary workaround

phrase = input('Enter the phrase you\'d like pronounced (or "exit" to quit): ')

while phrase != 'exit':
    tts = gTTS(phrase, lang="zh-cn") #or zh-tw for taiwanese pronunciation
    tts.save(ANKI_MEDIA_DIRECTORY + phrase + '.mp3')
    phrase = input('Enter the phrase you\'d like pronounced (or "exit" to quit): ')

#CARD_LIST_FILE = "./anki_card_list.txt"

#with open(CARD_LIST_FILE) as f:
#    for line in f:
#        phrase = line.strip()
#        tts = gTTS(phrase, lang="zh-cn") #or zh-tw for taiwanese pronunciation
#        tts.save(ANKI_MEDIA_DIRECTORY + phrase + '.mp3')
