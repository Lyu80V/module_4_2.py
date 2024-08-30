
def test_function():
    def inner_function():
        d = "Я в области видимости функции test_function"
        print(d)

    inner_function()

test_function()
#inner_function()