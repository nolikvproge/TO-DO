from datetime import date

with open (f'{date.today()}.txt,"w"') as f:
    print("Введите список дел")
    while True:
        todo = input()
        if todo.lower() == 'стоп':
            break
        f.write(todo + '\n')