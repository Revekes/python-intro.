import random

names = ["Patryk", "Wiktoria", "Tomek", "Karolina"]
ages = [random.randint(18, 24) for _ in names]  

paired = list(zip(names, ages))
print("Imiona z wiekiem:", paired)


try:
  
    faulty_age = -5
    if faulty_age < 0:
        raise ValueError("Wiek nie może być liczbą ujemną.!BŁĄD!")
except ValueError as e:
    print("Błaad:", e)

#Link do opisu użytych funkcji: 
# https://github.com/Revekes/python-intro./blob/571949770d8bdb4390684cca86fb26fdbd235a81/Zadanie_1/Dokumentacja_3.3.py

