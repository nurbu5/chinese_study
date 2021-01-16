from gtts import gTTS

tts = gTTS('空心的', lang="zh-cn") #or zh-tw for taiwanese pronunciation
tts.save('pronunciations/空心的.mp3')
