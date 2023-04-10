import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p_cnt = x_success / x_cnt
    p_test = y_success / y_cnt
    if p_cnt -  p_test > 0.06:
      result = bool(0) 
    else:
      result = bool(1)
    return result # Ваш ответ, True или False
