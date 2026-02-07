while True:
    s = input('Введіть щось : ')
    if s == 'вихід':
        break
    if len(s) < 3:
        print('Надто мало.')
        continue
    print('Введений рядок достатньо довгий.')
