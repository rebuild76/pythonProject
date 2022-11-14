tickets = int(input("Введите количество билетов:\t"))


def res_from_year_old(year):
    if year < 18:
        return 0
    elif 18 <= year < 25:
        return 990
    else:
        return 1390

print()
result_list = [res_from_year_old(int(input(f'Возраст {i + 1} посетителя: '))) for i in range(tickets)]
sum_result = int(sum(result_list) * 0.9) if tickets >= 4 else sum(result_list)
print()
print("Сумма к оплате: {} руб".format(sum_result))