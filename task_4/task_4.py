'''
Завдання 4

Доробіть консольного бота помічника з попереднього домашнього завдання та додайте 
обробку помилок за допомоги декораторів.


Вимоги до завдання:

Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", 
"Give me name and phone please" тощо.
Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і 
це винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор 
повинен повертати відповідну відповідь користувачеві. Виконання програми 
при цьому не припиняється.
'''

# Словарь с примерами контактов
CONTACTS = {
    "Vasya": '0670001199',
    "Hariton": '0995550011',
    "Stepan": '0635554422'
}

def input_error(func):
    # Функция для декоратора, проверка валидности введенных данных
    def inner(*args, **kwargs):
        # Обработаем исключения для разных случаев
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the contact name please."
        except KeyError:
            return "This contact is not exist :("

    return inner

def parse_input(user_input):
    # Парсим команды и приводим в нижний регистр чтобы не было путаницы
    cmd, * args =user_input. split ()
    cmd = cmd.strip().lower()
    return cmd, * args

@input_error
def add_contact( args ):
    name, phone = args
    # Добавим контакт, если такого еще нет
    if name not in CONTACTS:
        CONTACTS[name] = phone
        return  "Contact added."
    else:
        return  "Contact already exist."

@input_error
def change_contact ( args ):
    name, phone = args
    # Меняем контакт, если такой есть
    if CONTACTS[name]:
        CONTACTS[name] = phone
        return name + ' changed'
    else:
        return  'Contact not found.'

@input_error
def show_phone( args ):
    name = args[0]
    #  Покажем контакт, если он есть
    if CONTACTS[name]:
        return name + ' - ' + CONTACTS[name]
    else:
        return  'Contact not found.'

def show_all ():
    res = ''
    # Сделаем удобный для чтения список
    for name, number in CONTACTS.items():
        res += name + ' - ' + number + '\n'
    return res

def main():
    print ( "Велкует к требованию!" )
    # Бот всегда слушает наши команды
    while True:
        user_input = input ( "Enter a command: " )
        command , * args = parse_input(user_input)
        # Делигируем в соответствии с командой.
        match command:
            case "close" | "exit":
                print ( "Good bye!" )
                break 
            case "hello" :
                print ( "How can I help you?" )
            case "add" :
                print (add_contact( args ))
            case "change" :
                print (change_contact( args ))
            case "phone" :
                print (show_phone( args ))
            case "all" :
                print (show_all())
            case _:
                print ( "Invalid command." )

if __name__ == "__main__" :
    main()