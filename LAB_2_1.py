money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

number = 0
while money_capital + salary >=spend:
    number += 1
    money_capital+=salary
    money_capital-=spend
    spend *= (increase + 1)


print("Количество месяцев, которое можно протянуть без долгов:", number)
