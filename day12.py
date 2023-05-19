import random

responses = {
  "你好": ["hello", "嗨", "怎么了"],
  "再见": ["再见", "待会见", "拜拜"],
  "谢谢": ["不客气", "没问题", "没事"],
  "default": ["抱歉，我没有明白你的意思"]
}

def chatbot():
    while True:
        user_input = input("你: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        elif user_input.lower() in responses:
            bot_response = random.choice(responses[user_input.lower()])
        else:
            bot_response = random.choice(responses["default"])
        print("回复: " + bot_response)

chatbot()
