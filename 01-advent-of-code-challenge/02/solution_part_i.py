#Rock     (A) 
#Paper    (B)  
#Scissors (C) 
#Lose         - 0 
#draw         - 3
#Win          - 6
#Rock     (X) - 1
#Paper    (Y) - 2 
#Scissors (Z) - 3  
with open("input1.txt", encoding="utf-8", mode="r")as tabela:
  lines = [(a.replace('\n', " ")) if a =="\n" else str(a.replace('\n', "")) for a in tabela.readlines()]
  total = 0
  for x in lines:
    if x == 'A X':
      total += 4
    elif x == 'A Y':
      total += 8
    elif x == 'A Z':
      total += 3
    elif x == 'B X':
      total += 1
    elif x == 'B Y':
      total += 5
    elif x == 'B Z':
      total += 9
    elif x == 'C X':
      total += 7
    elif x == 'C Y':
      total += 2
    elif x == 'C Z':
      total += 6
    else:
      total += 0
  print(total)
