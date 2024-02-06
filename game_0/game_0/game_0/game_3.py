import numpy as np

def dichotomy_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    predict_number0 = 0
    predict_number1 = 50
    predict_number2 = 100
    while True:
        count += 1
        if number == predict_number1:
            break # выход из цикла, если угадали
        elif number > predict_number1:
            predict_number0 = predict_number1
        else:
            predict_number2 = predict_number1
        
        predict_number1 = (predict_number0 +predict_number2)//2
        
    return(count)

print(f'Количество попыток: {dichotomy_predict()}')

