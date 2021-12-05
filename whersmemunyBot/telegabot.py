import telebot
from config import currencies_list
from tokens import TBTOKEN
from extentions import APIException, CurrencyConverter

bot = telebot.TeleBot(TBTOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Здравствуй, {message.chat.username}.\nЭтот бот поможет тебе конвертировать"
                                      f" деньги из одной валюты в другую. \n"
                                      f"Напишите свой запрос в формате:\n <исходная валюта>, <желаемая валюта>, "
                                      f"<сумма в исходной валюте> \n Пример: Cuban Peso, Euro, 1000 \n"
                                      f"Для получения справки о работе бота"
                                      f" отправьте команду /start или /help.\nДла получения списка доступных валют"
                                      f" отправьте команду /values.")


@bot.message_handler(commands=['values'])
def send_currencies(message):
    text = 'Доступные валюты:\n'
    bot.send_message(message.chat.id, {text + '\n'.join(dict(sorted(currencies_list.items(), key=lambda x: x[0].lower())))})


@bot.message_handler()
def send_calcs(message:  telebot.types.Message):
    try:
        entries = message.text.split(', ')

        if len(entries) < 3:
            raise APIException('Слишком мало параметров!')

        if len(entries) > 3:
            raise APIException('Слишком много параметров!')

        base, quote, amount = entries
        result = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя!\n{e}')       
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду!\n{e}')
    else:
        bot.send_message(message.chat.id, f'Стоимость {amount} {base} в {quote}: {result}')


bot.polling(non_stop=True)
