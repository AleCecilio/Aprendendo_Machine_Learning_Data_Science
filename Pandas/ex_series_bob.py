#TAREFA: As despesas dos funcionários estão sendo armazenadas em uma série do Pandas chamada despesas. Quais são as despesas do Bob? Você deve usar o Pandas para isso, não apenas escrever o número manualmente. A solução deve ser bem simples. Atribua sua resposta a uma variável chamada bob_expense. Observe que, para que o exercício seja avaliado corretamente, você deve usar a variável bob_expense.

import pandas as pd
expenses = pd.Series({'Andrew':200,'Bob':150,'Claire':450})

bob_expense = expenses['Bob']
print(bob_expense)