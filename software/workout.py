import os
import time

PRONUNCIATIONS_DIRECTORY = "../data/pronunciations/"
OS_PLAY_COMMAND = "afplay "

exercises={
    "Gymnastic Ring":"体操环",
    #"Jumping Jacks":"开合跳",
    "Wall Sits":"贴墙半蹲",
    "Push-ups":"伏地挺身",
    "Sit-ups":"仰卧起坐",
    #"Weight Bearing Stool (Step-ups)":"负重登凳",
    "Squats":"深蹲",
    "Double arm flexion (Tricep Dips)":"双杠臂屈伸",
    "Plank":"平板支撑",
    #"High Knees":"高抬腿运动",
    "Handstand":"手倒立",
    "Hollow Hold":"空心的",
    "Lunges":"弓步",
    "Push-ups with rotation":"伏地挺身+上半身轉體",
    "Pull-up Bar":"引體向上單槓"
}

lr_exercises={
    "Side Bridge":"侧桥"
}

os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "多少.mp3")
circuits = input("多少 ")

for _ in range(int(circuits)):
    for en, zh in exercises.items():
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "下一个练习.mp3")
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + zh + ".mp3")
        print("中文:", zh)
        print("English:", en)
        print("\n")
        time.sleep(9)
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "倒数.mp3") #countdown.mp3
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "开始.mp3")
        time.sleep(30)
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "停止.mp3")

    for en, zh in lr_exercises.items():
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "下一个练习.mp3")
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + zh + ".mp3")
        print("中文:", zh)
        print("English: ", en)
        print("\n")
        time.sleep(9)
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "倒数.mp3") #countdown.mp3
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "开始.mp3")
        time.sleep(20)
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "替换.mp3")
        time.sleep(21)
        os.system(OS_PLAY_COMMAND + PRONUNCIATIONS_DIRECTORY + "停止.mp3")


