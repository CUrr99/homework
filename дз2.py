numb1 = int(input("Введите первое число: ")) 
numb2 = int(input("Введите второе число: ")) 
if numb2 == 0: 
  print("На ноль делить нельзя.")
  print('Программа завершена')
else: 
  if numb1 % numb2 == 0: 
    print(f"{numb1} кратно {numb2}") 
  else: 
    print(f"{numb1} не кратно {numb2}")
