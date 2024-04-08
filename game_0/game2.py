import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

def dichotomy_predict(number:int=1) -> int:
    """Угадываем число методом дихотомии

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    #разбиваем диапазон на два отрезка
    predict_number0 = 0
    predict_number1 = 50
    predict_number2 = 101

    while True:
        count += 1
        if number == predict_number1:
            break # выход из цикла, если угадали
        elif number > predict_number1:
            predict_number0 = predict_number1 #переопределяем отрезок
        else:
            predict_number2 = predict_number1 #переопределяем отрезок
        
        predict_number1 = (predict_number0 +predict_number2)//2 #делим отрезок пополам
    return(count)

print(f'Количество попыток: {dichotomy_predict()}')

def score_game(predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
    score_game(dichotomy_predict)