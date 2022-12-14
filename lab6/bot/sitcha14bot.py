import requests
import telebot




bot  = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Enter a name to predict gender(Genderize) and age")


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    name = message.text

    name_data = requests.get(f"https://api.genderize.io/?name={name}")
    age_data = requests.get(f'https://api.agify.io/?name={name}')
    #extract gender and probability
    gender = name_data.json()['gender']
    probability = name_data.json()['probability']

    #extract age
    age = age_data.json()['age']

    bot.send_message(message.chat.id,f"{name} is a most likely a {gender} name. The probability for this is {probability * 100}%")
    bot.send_message(message.chat.id,f"{name} is a most likely a {age} year old")

    print("bot running")


bot.polling(non_stop=True)


