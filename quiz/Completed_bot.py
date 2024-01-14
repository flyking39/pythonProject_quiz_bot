import telebot
import json
import time
from Keyboard_creation import paintings_buttons, painters_buttons
Token = '6779776698:AAE7rveOtd2vRKLdp3doG8jQQ0lqgf_h3_Q'
bot = telebot.TeleBot(Token)
Correct_Painter = ''
Correct_Painting = ''
Counter = 0
Storage = []


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Hello!')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Enter /help if '''
                                               'you still do not know what this programme does\n '
                                               'If you do then '
                                               'enter /proceed ')
        bot.register_next_step_handler(message, process)
    else:
        bot.send_message(message.from_user.id, 'write /start in order to launch the programme')


def process(message):
    """
    this function awaits for a command from a user and initiates a quiz
    if the command /proceed is entered or in case if the command is /help it sends a clarification message or if it's
    anything else it sends a clarification message consisting of information of valid commands
    :param message:
    :return:
    """
    if message.text == '/proceed':
        bot.send_message(message.from_user.id, 'Your Quiz is about to begin....')
        time.sleep(1.5)
        bot.send_message(message.from_user.id, 'Now!')
        continuation(message)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'I am Painting_bot988 bot. ''I have been created by '
                                               'a great programmer '
                                               'to entertain you. ''Write /proceed in order to begin '
                                               'taking part '
                                               'in this magnificent quiz about '
                                               'the most famous art works of the mankind ')
        bot.register_next_step_handler(message, process)

    else:
        bot.send_message(message.from_user.id, 'You have entered the wrong command, Enter /help if '
                                               'you still do not know what this programme does\n '
                                               'If you do then '
                                               'enter /proceed ')
        bot.register_next_step_handler(message, process)


def continuation(message):
    """
    this function is the core of the quiz. It opens a json file with the zero index name of the painting
    and sends it to a user after that this function  sends the zero index items form the Storage variable
    :param message:
    :return:
    """
    try:
        global Counter
        if Counter == 0:
            with open('Full_information_storage.json', 'r') as file:
                result = json.load(file)
                key = list(result.keys())[0]
                value = result[key]
                del result[key]
                global Storage
                Storage = result
                Counter += 1
        else:
            key = list(Storage.keys())[0]
            value = Storage[key]
            del Storage[key]
        global Correct_Painting
        Correct_Painting = key
        keyboard = paintings_buttons(key, value)
        bot.send_photo(message.from_user.id, photo=open(f'{key}' + '.png', 'rb'), reply_markup=keyboard)
        time.sleep(5)
        with open('Painting_creator.json') as first_file:
            inf = json.load(first_file)
            global Correct_Painter
            Correct_Painter = inf[key]
        keyboard1 = painters_buttons(Correct_Painter)
        bot.send_message(message.from_user.id, 'Who is the painter of the masterpiece?', reply_markup=keyboard1)
    except IndexError:
        bot.send_message(message.from_user.id, 'you have completed the quiz')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'correct_painting':
        bot.send_message(call.message.chat.id, f'{Correct_Painting} is the correct answer\n'
                                               f'Good job, keep it up')
    elif call.data == 'correct_painter':
        bot.send_message(call.message.chat.id, f'{Correct_Painter} is the correct answer\n'
                                               f'Good job, keep it up')
        continuation(call)
    elif call.data == 'invalid_painting':
        bot.send_message(call.message.chat.id, f'{Correct_Painting} is actually the correct answer\n'
                                               f'Do not worry, you will get the next one')
    elif call.data == 'invalid_painter':
        bot.send_message(call.message.chat.id, f'{Correct_Painter} is actually the correct answer\n'
                                               f'Do not worry, you will get the next one')
        continuation(call)


bot.polling(none_stop=True, interval=0)


# # the next photo is sent only after a user has already replied
# #typisation, description
# #GitHub
# # clarification for a user in case of a wrong command
