# -*- coding: cp1251 -*-
import os 
from path_file import path_p

dirrectory=['10','task4']
extract_zip=path_p(dirrectory)
file_text=path_p(dirrectory,'history_chat.txt')
while True: 
    try: 
        username = input("Введите ваше имя или никнейм: ") 
        if username.isalpha(): 
            break 
        else: 
            raise ValueError 
    except ValueError: 
        print("Неправильный ввод! Пожалуйста, убедитесь, что вводите только буквенные символы.\n") 
    

while True: 
   
    print('\n1. Посмотреть текущий текст чата.' 
          '\n2. Отправить сообщение.' 
          '\n3. Выйти из чата.') 
    action_choice = int(input('Выберите действие: ')) 
    if action_choice == 1: 
        try: 
            if not os.path.exists(file_text) or os.stat(file_text).st_size == 0: 
                raise FileNotFoundError 
            else: 
                with open(file_text, 'r', encoding='utf-8') as chat_text: 
                    print(f'\nТекущий текст чата:\n{chat_text.read()}') 
        except FileNotFoundError: 
            print('--> Чат пуст. Начните общение.') 
    elif action_choice == 2: 
        try: 
            with open(file_text, 'a', encoding='utf-8') as message_record: 
                print(f'\n{username} напишите сообщение:') 
                user_message = input('--> ') 
                if user_message.strip() == '': 
                    raise ValueError 
                else: 
                    message_record.write(f'{username}: {user_message}\n') 
        except ValueError: 
            print('Сообщение не может быть пустой строкой!') 
    elif action_choice == 3: 
        os.truncate(file_text, 0) 
        break 
    else: 
        print('Ошибка! Выберите одно из доступных действий.')