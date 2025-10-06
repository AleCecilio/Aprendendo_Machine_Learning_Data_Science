# TAREFA: Um dado de seis lados foi lançado várias vezes e os resultados foram salvos em um array numPy chamado dice_rolls. Quantas vezes um dado maior que 2 foi lançado? Em outras palavras, quantos inteiros no array dice_rolls são maiores que 2? Atribua sua resposta (deve ser um inteiro) a uma variável chamada total_rolls_over_two.


import numpy as np
dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

total_rolls_over_two = len(dice_rolls[dice_rolls>2])

print(total_rolls_over_two)