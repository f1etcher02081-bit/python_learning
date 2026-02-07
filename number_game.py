number = 23
running = True

while running:
    guess = int(input("Введіть ціле число : "))

    if guess == number:
        print("Вітаю, ви відгадали!")
        running = False #Зупиняє цикл while
    elif guess < number:
        print("Ні, загадане число трохи більше цього.")
    else:
        print("Ні, загадане число трохи менше цього.")
else:
    print("Цикл while завершений.")

print("Завершення.")