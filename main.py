import requests
import time
import telebot
import random
token = "8155270205:AAFrcQaPFN1I04x7R3E8qTIP-kNohivlg5I"
bot = telebot.TeleBot(token)
lict = []
urlv = ''
lang = 'ru'
attempsl = 0
status = ''
@bot.message_handler(commands=['start'])
def start(message):
     bot.reply_to(message, 'Привет!\nЯ - бот, который подскажет какая сегодня погода.\nЯ поддерживаю все города мира! Так же поддерживаю два языка - en / ru.\n Напиши /set для установки города.\n/help - список комманд. Приятного использования!')
     print("LOG: NEW USER!")
@bot.message_handler(commands=['help'])
def help(message):
     global lang
     if lang == 'en':
           bot.reply_to(message, 'Got it! Here are the commands:\n1. /start - The very first command! It starts me.\n2. /help - You-re here now!\n3. /weather - check the weather\n4. /set city - set a city. Example: /set Moscow\n5. /language - set the language. Example: /language en\n6. /reset - change the city to a new one. Example: /reset Moscow.\n7. /leset - change the language to a new one. Example: /leset en. (supported ru/en)\n8. /mycity - a list of your cities and viewing up-to-date information.\n9. /updlist - add your favorite city to the list. Example: /updlist Moscow\n10. /delcity - remove a city from the favorites list. Example: /delcity Moscow\n.11. /import - an interesting command that will show the weather in favorite cities.')
     else:
          bot.reply_to(message, 'Понял! Вот команды:\n1. /start - Самая первая команда! Она запускает меня.\n2. /help - Ты сейчас здесь!\n3. /weather - узнать погоду\n4. /set город - установить город. Пример: /set Москва\n5. /language - установить язык. Пример - /language en\n6. /reset - сменить город на новый. Пример: /reset Москва.\n7. /leset - сменить язык на новый. Пример: /leset en. (поддерживаются ru/en)\n8. /mycity - список ваших городов, и просмотр актуального.\n9. /updlist - добавить в список любимый город. Пример: /updlist Москва\n10. /delcity - удалить город из фаворит списка. Пример: /delcity Москва\n11. /import - интересная команда, которая покажет погоду в фаворит-городах.')
@bot.message_handler(commands=['set'])
def set(message):
     global urlv, status, lang
     if urlv != '':
          if lang == 'en':
               bot.reply_to(message, 'The city is already set. If you want to change it - /reset city.Example: /reset Kazan')
          else:
               bot.reply_to(message, 'Город уже установлен. Если хотите сменить - /reset город.\nПример: /reset Казань')
          print("LOG: MODULE = SET. STATUS = OK. TEXT = СМЕНА ГОРОДА ЗАБЛОКИРОВАНА. ГОРОД УЖЕ УСТАНОВЛЕН ")
     else:
          commandone = message.text.replace('/set', '').strip()
          startofbot = time.time()
          urlv = commandone 
          if urlv == commandone:
               status = 'ok'
               if lang == 'en':
                    bot.reply_to(message, 'Success! The city has been set. ' + urlv)
               else:
                    bot.reply_to(message, 'Успешно! Город установлен, ' + urlv)
               endofbot = time.time()
               timebot = endofbot - startofbot
               print(f"LOG: MODULE = SET / STATUS OK, TIME: {timebot}")
          else: 
               jhk = time.time()
               status = 'no'
               if lang == 'en':
                      bot.reply_to(message, 'Oops! Mistake on my part - ' + '.  STATUS = ' + status + '. Try again.')
               else:
                    bot.reply_to(message, 'Ой! Ошибка на моей стороне - ' + '.  STATUS = ' + status + '. Попробуйте снова.')
               jkh = time.time()
               timebotq = jkh - jhk
               print(f"LOG: MODULE = SET / STATUS NO, TIME: {timebotq}")
@bot.message_handler(commands=['language'])
def language(message):
     global lang, status, attempsl
     if lang != '' and attempsl >= 1:
          if lang == 'en':
               bot.reply_to(message, 'The language is already set. If you want to change it, use /leset language.\nExample: /leset ru')
          else:
               bot.reply_to(message, 'Язык уже установлен. Если хотите сменить - /leset язык.\nПример: /leset en')
          print("LOG: MODULE = LANGUAGE. STATUS = OK. TEXT = СМЕНА ЯЗЫКА ЗАБЛОКИРОВАНА. ЯЗЫК УЖЕ УСТАНОВЛЕН ")
     else:
          status = ''
          starttimebot = time.time()
          lange = message.text.replace('/language', '').strip()
          lang = lange
          if lang == lange and lang != '':
               status = 'ok'
               attempsl = attempsl+ 1 
               if lang == 'en':
                    bot.reply_to(message, 'Language set! Language: ' + lang)
               else:
                    bot.reply_to(message, 'Язык установлен! Язык: ' + lang)
               endttimebot = time.time()
               eoe = endttimebot - starttimebot
               print(f"LOG: MODULE = LANGUAGE / STATUS OK, TIME: {eoe}")
          else:
               sbt = time.time()
               status = ''
               if lang == 'en':
                    bot.reply_to(message, 'Oh! The language was not set. Please try again later. ' + ' STATUS = ' + status)
               else:
                    bot.reply_to(message, 'Ой! Язык не был установлен. Попробуйте позже. ' + ' STATUS = ' + status)
               status = 'no'
               ebt = time.time()
               sumt = ebt - sbt
               print(f"LOG: MODULE = LANGUAGE / STATUS NO, TIME: {sumt}")
@bot.message_handler(commands=['weather'])
def weather(message):
     global urlv, lang
     url = requests.get(f"http://wttr.in/{urlv}?format=3&lang={lang}")
     if url.status_code == 200:
          if lang == 'en':
                bot.reply_to(message, f'The weather in the city {urlv}\n{url.text}')
          else:
                bot.reply_to(message, f'Погода в городе {urlv}\n{url.text}')
          print("LOG: MODULE = WEATHER. STATUS = 200")
     else:
          if lang == 'en':
               bot.reply_to(message, 'Oops, failed to get the weather. Try again in a few minutes.!')
          else:
               bot.reply_to(message, 'Ой, не получилось получить погоду. Попробуй через несколько минут!')
          print(f"LOG: MODULE = WEATHER. STATUS = {url.status_code} and {url.text}")
@bot.message_handler(commands=['reset'])
def reset(message):
     global urlv, lang
     resetm = message.text.replace('/reset', '').strip()
     urlv = ''
     urlv = resetm
     if urlv == resetm:
          print("LOG: MODULE == RESET // STATUS = OK")
          if lang == 'en':
               bot.reply_to(message, 'The city has been reset! City: ' + urlv)
          else:
               bot.reply_to(message, 'Город переустановлен! Город: ' + urlv)
     else:
          print("LOG: MODULE == RESET // STATUS = ERROR")
          if lang == 'en':
               bot.reply_to(message, 'Oh! My mistake! Sorry.')
          else:
               bot.reply_to(message, 'Ой! Ошибка на моей стороне! Прости.')
@bot.message_handler(commands=['leset'])
def leset(message):
     global lang
     flang = message.text.replace('/leset', '').strip()
     lang = ''
     lang = flang 
     if lang == flang:
          if lang == 'en':
               bot.reply_to(message, 'Language reinstalled! The language is now: ' + lang)
          else:
               bot.reply_to(message, 'Язык переустановлен! Язык теперь: ' + lang)
          print("LOG: MODULE LESET. STATUS = OK")
     else:
          if lang == 'en':
               bot.reply_to(message, 'Oops! My mistake. Try again in a few minutes.')
          else:
               bot.reply_to(message, 'Ой! Ошибка на моей стороне. Попробуй через несколько минут')
          print("LOG: MODULE LESET. STATUS = NO")
@bot.message_handler(commands=['mycity'])
def mycity(message):
     global urlv, lict
     if lang == 'en':
          bot.reply_to(message, 'Your city right now: ' + urlv)
          bot.reply_to(message, f'Your list of favorite cities: {lict}')
     else:
          bot.reply_to(message, 'Ваш город прямо сейчас: ' + urlv)
          bot.reply_to(message, f'Ваш список любимых городов: {lict}')
     print("LOG:FAVOURITE REQUEST")
@bot.message_handler(commands=['updlist'])
def updlist(message):
     global lict
     dfe = message.text.replace('/updlist', '').strip()
     lict.append(dfe)
     if dfe in lict:
          print("LOG: APPEND LICT STATUS = OK")
          if lang == 'en':
               bot.reply_to(message, f'The list has been updated! The new list of favorites: {lict}')
          else:
               bot.reply_to(message, f'Список был обновлён! Новый список избранного: {lict}')
@bot.message_handler(commands=['delcity'])
def deletecity(message):
     global lict, lang
     asd = message.text.replace('/delcity', '').strip()
     if asd in lict:
          lict.remove(asd)
          print("LOG: 1/2 DELETE SUC.")
     else:
          if lang == 'en':
               bot.reply_to(message, 'The list has been updated! Removed from the list: ' + asd)
          else:
               bot.reply_to(message, 'Список обновлен! Удалено из списка: ' + asd)
     if asd not in lict:
          print("LOG: DELETE SUC. STATUS = OK")
          if lang == 'en':
               bot.reply_to(message, 'There is no h csucity in your list. Please enter it again /delcity ' + asd)
          else:
               bot.reply_to(message, 'В вашем списке нет такого города. Пожалуйста, введите его снова /delcity  ' + asd)
     else:
          print("LOG: ERROR IN DELETE LIST")
          if lang == 'en':
               bot.reply_to(message, 'Oh, sorry! I couldn-t update the list and remove the city. ' + asd)
          else:
               bot.reply_to(message, 'Ой, прости! Не получилось обновить список и удалить город. ' + asd)
@bot.message_handler(commands=['import'])
def fimport(message):
     global lict, lang
     for i in lict:
          urlf = requests.get(f'http://wttr.in/{i}?format=3&lang={lang}')
          if urlf.status_code == 200:
               print("LOG: SUC. WEATHER LIST FAVOURITE")
               if lang == 'en':
                    bot.reply_to(message, f'The weather in the city is {i}: {urlf.text}')
               else:
                    bot.reply_to(message, f'Погода в городе {i}: {urlf.text}')
                    time.sleep(2)
bot.polling()
