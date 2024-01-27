print('==========================================')
print('Розрахунок співвідношення учнів в класі')
girls = int(input("Кількість дівчат: "))
boys = int(input("Кількість хлопців: "))
all_students = boys + girls
girls_percent = girls * 100 / all_students
boys_percent = boys - girls_percent
print(f"Дівчат: {girls_percent}% Хлопців {boys_percent}%")
