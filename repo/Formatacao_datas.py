from datetime import datetime, timedelta

data_atual = datetime.now()

# Este objeto precisa ser convertido para string quando for concatenado com uma string
print('Hoje é: ' + str(data_atual))

# Timedelta pode ser utilizado para adicionar ou remover dias ou semanas de uma data
um_dia = timedelta(days=1)
ontem = data_atual - um_dia
print('Ontem foi: ' + str(ontem))

uma_semana = timedelta(weeks=1)
ultima_semana = data_atual - uma_semana
print('Semana passada foi: ' + str(ultima_semana))

# É possivel exibir somente parte da data
print('Dia: ' + str(data_atual.day))
print('Mês: ' + str(data_atual.month))
print('Ano: ' + str(data_atual.year))
print('Hora: ' + str(data_atual.hour))
print('Minuto: ' + str(data_atual.minute))
print('Segundo: ' + str(data_atual.second))

# O strptime é utilizado para definir o formato de entrada da data
aniversario = input('Aniversário: (dd/mm/aaaa): ')
data_aniversario = datetime.strptime(aniversario, '%d/%m/%Y')
print('Dia do nascimento: ' + str(data_aniversario))