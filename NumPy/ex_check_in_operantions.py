#TAREFA: Uma conta bancária teve saques e depósitos rastreados em um array numpy chamado account_transactions. Com base nessa lista de transações da conta, qual é o total restante na conta? Atribua sua resposta a uma variável chamada account_total.

import numpy as np

account_transactions = np.array([100,-200,300,-400,100,100,-230,450,500,2000])

account_total =  account_transactions.sum()

print(account_total)