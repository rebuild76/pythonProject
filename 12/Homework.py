# Моя первая лямбда
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите размер депозита: "))
deposit_list = list(map(lambda x: int(x * money / 100), list(per_cent.values())))

print("deposit = {}".format(deposit_list))
print("Максимальная сумма, которую вы можете заработать — {}".format(max(deposit_list)))

