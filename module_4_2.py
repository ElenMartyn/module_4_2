def test_function():# локальная область видимости
    def inner_function(): # объемлющая область видимости
        print("Я в области видимости функции test_function")
    inner_function()



test_function() # Вызов функции test_function

try:
    inner_function()
except NameError as e:
    print(e)  # Это выведет сообщение name 'inner_function' is not defined, так не является глобальным