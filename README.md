# Chinese Tools

-Make sure to create a "data/pronunciations" directory
-The data directory also contains csv data of chinese words/phrases
-Software contains software for creating chinese anki cards, a pronunciation generator, and a workout routine in Chinese

#Pronunciation Generation Example
```
from gtts import gTTS

tts = gTTS('空心的', lang="zh-cn") #or zh-tw for taiwanese pronunciation
tts.save('pronunciations/空心的.mp3')
```
