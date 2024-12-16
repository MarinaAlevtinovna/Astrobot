import telebot
import random
import time
import datetime
import threading
from config import TOKEN

bot = telebot.TeleBot(token = TOKEN)

def load_facts_from_file():
    with open('facts.txt', 'r', encoding='utf-8') as file:
        facts = file.readlines()
    return [fact.strip() for fact in facts]

facts = load_facts_from_file()
sent_facts = set()
last_sent_time = None

def generate_random_fact():
    return random.choice(facts)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, '/fact - факт про знаки зодиака\n' '/horoscope - получить гороскоп на сегодня')

@bot.message_handler(commands=['start'])
def start_message(message):
    global reminder_thread
    bot.reply_to(message, 'Привет! Я гороскопик-голопопик! :) \n' f'Вот, что я могу /help')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    fact = generate_random_fact()
    bot.reply_to(message, f'А Вы знали, что {fact}')

def send_reminders(chat_id):
    global last_sent_time
    time_send = ['12:00']
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now in time_send and now != last_sent_time:
            fact = generate_random_fact()
            bot.send_message(chat_id, f'А Вы знали, что {fact}')
            last_sent_time = now
            time.sleep(61)
        time.sleep(1)


@bot.message_handler(commands=['horoscope'])
def get_horoscope(message, fact=None):
    bot.reply_to(message, 'Выбери знак зодиака: \n''/aries - Овен\n''/taurus - Телец\n''/gemini - Близнецы\n'
                          '/cancer - Рак\n''/leo - Лев\n''/virgo - Дева\n''/libra - Весы\n''/scorpio - Скорпион\n'
                          '/sagittarius - Стрелец\n''/capricorn - Козерог\n''/aquarius - Водолей\n''/pisces - Рыбы\n')

def load_horoscope_from_aries():
    with open('Aries.txt', 'r', encoding='utf-8') as file:
        aries_horoscopes = file.readlines()
    return [aries_horoscope.strip() for aries_horoscope in aries_horoscopes]

aries_horoscopes = load_horoscope_from_aries()

def generate_random_horoscope_aries():
    return random.choice(aries_horoscopes)

@bot.message_handler(commands=['aries'])
def choice_aries(message):
    aries_horoscope = generate_random_horoscope_aries()
    bot.reply_to(message, f'{aries_horoscope}')

def load_horoscope_from_taurus():
    with open('Taurus.txt', 'r', encoding='utf-8') as file:
        taurus_horoscopes = file.readlines()
    return [taurus_horoscope.strip() for taurus_horoscope in taurus_horoscopes]

taurus_horoscopes = load_horoscope_from_taurus()

def generate_random_horoscope_taurus():
    return random.choice(taurus_horoscopes)

@bot.message_handler(commands=['taurus'])
def choice_taurus(message):
    taurus_horoscope = generate_random_horoscope_taurus()
    bot.reply_to(message, f'{taurus_horoscope}')

def load_horoscope_from_gemini():
    with open('Gemini.txt', 'r', encoding='utf-8') as file:
        gemini_horoscopes = file.readlines()
    return [gemini_horoscope.strip() for gemini_horoscope in gemini_horoscopes]

gemini_horoscopes = load_horoscope_from_gemini()

def generate_random_horoscope_gemini():
    return random.choice(gemini_horoscopes)

@bot.message_handler(commands=['gemini'])
def choice_gemini(message):
    gemini_horoscope = generate_random_horoscope_gemini()
    bot.reply_to(message, f'{gemini_horoscope}')

def load_horoscope_from_cancer():
    with open('Cancer.txt', 'r', encoding='utf-8') as file:
        cancer_horoscopes = file.readlines()
    return [cancer_horoscope.strip() for cancer_horoscope in cancer_horoscopes]

cancer_horoscopes = load_horoscope_from_cancer()

def generate_random_horoscope_cancer():
    return random.choice(cancer_horoscopes)

@bot.message_handler(commands=['cancer'])
def choice_cancer(message):
    cancer_horoscope = generate_random_horoscope_cancer()
    bot.reply_to(message, f'{cancer_horoscope}')

def load_horoscope_from_leo():
    with open('Leo.txt', 'r', encoding='utf-8') as file:
        leo_horoscopes = file.readlines()
    return [leo_horoscope.strip() for leo_horoscope in leo_horoscopes]

leo_horoscopes = load_horoscope_from_leo()

def generate_random_horoscope_leo():
    return random.choice(leo_horoscopes)

@bot.message_handler(commands=['leo'])
def choice_leo(message):
    leo_horoscope = generate_random_horoscope_leo()
    bot.reply_to(message, f'{leo_horoscope}')

def load_horoscope_from_virgo():
    with open('Virgo.txt', 'r', encoding='utf-8') as file:
        virgo_horoscopes = file.readlines()
    return [virgo_horoscope.strip() for virgo_horoscope in virgo_horoscopes]

virgo_horoscopes = load_horoscope_from_virgo()

def generate_random_horoscope_virgo():
    return random.choice(virgo_horoscopes)

@bot.message_handler(commands=['virgo'])
def choice_virgo(message):
    virgo_horoscope = generate_random_horoscope_virgo()
    bot.reply_to(message, f'{virgo_horoscope}')

def load_horoscope_from_libra():
    with open('Libra.txt', 'r', encoding='utf-8') as file:
        libra_horoscopes = file.readlines()
    return [libra_horoscope.strip() for libra_horoscope in libra_horoscopes]

libra_horoscopes = load_horoscope_from_libra()

def generate_random_horoscope_libra():
    return random.choice(libra_horoscopes)

@bot.message_handler(commands=['libra'])
def choice_libra(message):
    libra_horoscope = generate_random_horoscope_libra()
    bot.reply_to(message, f'{libra_horoscope}')

def load_horoscope_from_scorpio():
    with open('Scorpio.txt', 'r', encoding='utf-8') as file:
        scorpio_horoscopes = file.readlines()
    return [scorpio_horoscope.strip() for scorpio_horoscope in scorpio_horoscopes]

scorpio_horoscopes = load_horoscope_from_scorpio()

def generate_random_horoscope_scorpio():
    return random.choice(scorpio_horoscopes)

@bot.message_handler(commands=['scorpio'])
def choice_scorpio(message):
    scorpio_horoscope = generate_random_horoscope_scorpio()
    bot.reply_to(message, f'{scorpio_horoscope}')

def load_horoscope_from_sagittarius():
    with open('Sagittarius.txt', 'r', encoding='utf-8') as file:
        sagittarius_horoscopes = file.readlines()
    return [sagittarius_horoscope.strip() for sagittarius_horoscope in sagittarius_horoscopes]

sagittarius_horoscopes = load_horoscope_from_sagittarius()

def generate_random_horoscope_sagittarius():
    return random.choice(sagittarius_horoscopes)

@bot.message_handler(commands=['sagittarius'])
def choice_sagittarius(message):
    sagittarius_horoscope = generate_random_horoscope_sagittarius()
    bot.reply_to(message, f'{sagittarius_horoscope}')

def load_horoscope_from_capricorn():
    with open('Capricorn.txt', 'r', encoding='utf-8') as file:
        capricorn_horoscopes = file.readlines()
    return [capricorn_horoscope.strip() for capricorn_horoscope in capricorn_horoscopes]

capricorn_horoscopes = load_horoscope_from_capricorn()

def generate_random_horoscope_capricorn():
    return random.choice(capricorn_horoscopes)

@bot.message_handler(commands=['capricorn'])
def choice_capricorn(message):
    capricorn_horoscope = generate_random_horoscope_capricorn()
    bot.reply_to(message, f'{capricorn_horoscope}')

def load_horoscope_from_aquarius():
    with open('Aquarius.txt', 'r', encoding='utf-8') as file:
        aquarius_horoscopes = file.readlines()
    return [aquarius_horoscope.strip() for aquarius_horoscope in aquarius_horoscopes]

aquarius_horoscopes = load_horoscope_from_aquarius()

def generate_random_horoscope_aquarius():
    return random.choice(aquarius_horoscopes)

@bot.message_handler(commands=['aquarius'])
def choice_aquarius(message):
    aquarius_horoscope = generate_random_horoscope_aquarius()
    bot.reply_to(message, f'{aquarius_horoscope}')

def load_horoscope_from_pisces():
    with open('Pisces.txt', 'r', encoding='utf-8') as file:
        pisces_horoscopes = file.readlines()
    return [pisces_horoscope.strip() for pisces_horoscope in pisces_horoscopes]

pisces_horoscopes = load_horoscope_from_pisces()

def generate_random_horoscope_pisces():
    return random.choice(pisces_horoscopes)

@bot.message_handler(commands=['pisces'])
def choice_pisces(message):
    pisces_horoscope = generate_random_horoscope_pisces()
    bot.reply_to(message, f'{pisces_horoscope}')

# lock_file_path = "C:/Users/myssy/PycharmProjects/Telegramm_Bot_project/your_bot.lock"
#
# if os.path.exists(lock_file_path):
#     print("Бот уже запущен!")
#     sys.exit()
#
# with open(lock_file_path, "w") as lock_file:
#     lock_file.write(str(os.getpid()))
#
# try:
#     # Ваш код для запуска бота
#     bot.polling(none_stop=True)
#
# finally:
#     os.remove(lock_file_path)

bot.polling(none_stop=True)