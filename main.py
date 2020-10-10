#       КОД АРИНЫ
#import telebot
#
#bot = telebot.TeleBot('1240641183:AAEYMBx8u9nKU2pdvjGIvMHfWbR5OTDDIJU')
#
#@bot.message_handler(commands=['start'])
#def start_message(message):
#    bot.send_message(message.chat.id, 'Здравствуй, хозяин.')
#
#bot.polling()


#       КОД МАКСИМА

#Класс задания (никак не связан с классом пользователя)
class task:
    #Класс состоит из следующих полей, задающихся при инициализации
    id = ""
    text = ""
    media_link = ""
    answer = []
    right_answer = ""
    def __init__(self,id,text, answer,right_answer,media = Null):
        self.id = int(id)                   # Уникальный ID задания
        self.text = text                    # Текст задания
        self.answer = answer                # Все возможные ответы на задачу
        self.right_answer = right_answer    # Верный ответ
        self.media_link = media             # Опциональная ссылка на всевозможные фото/видео

#Класс пользователя, содержащий информацию о когда либо прорешенных задачах и кол-ве полученных за них баллов
class user:
    user_id = ""
    user_FS_Name = ""
    tasks_active = []                       #Пререшенные задачи
    tasks_marks = []                        #Оценки за задчачи
    
    def __init__(self,id,name):
        self.user_id = id
        user_FS_Name = name

    def solve_task(self, task, answer):     # Проверка конкретного задания и начисление баллов за правильный ответ
        self.tasks_active.append(task.id)
        if task.right_answer  == answer:
            mark = 100
            isRight = True
        else:
            mark = 0
            isRight = False
        self.tasks_marks.append(int(mark))  # TODO - добавить обработку ранее решенных задач (изменение записи, вместо "append")
        return isRight
        

# Образец интерфейса взаимодействия начало
#Задание пользователя для работы
first_user = user(1,"Kostyuchenko Max")

answers_possible = ["Ann","Chack","Sasha","Slava"]                          # Список всех возможных ответов 
first_task = task( 1,"Who is the best man?",  answers_possible,"Sasha")     # Задание задания в памяти передачей 
                                                                            # Уникального идентификатора, Текста задания, Массива возможных ответов, Правильного ответа и опциональной ссылки на медиа
if first_user.solve_task(first_task,"Sasha") == True:                       # Проверка задания, таке автматически начисляющая баллы обьекту пользователя, сохраняя ID выполненной задачи
    print("You're goddamn right")
else:
    print("Nope")