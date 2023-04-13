import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 689606612 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.06
    n = [x_cnt, y_cnt]
    successes = [x_success, y_success]

    stat, p_value = proportions_ztest(successes, nobs = n, alternative='larger')
    if 1 - p_value <= alpha:
      result = bool(1)
    else:
      result = bool(0)
    return result # Ваш ответ, True или False
