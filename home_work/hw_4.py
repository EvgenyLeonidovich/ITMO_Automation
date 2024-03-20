# Задача № 1
class Triangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def surface(self):
        return self.width * self.heigth

    def perimeter(self):
        return self.width + self.heigth


home = Triangle(10, 10)
home_surface = home.surface()
home_perimeter = home.perimeter()
print(home_surface)
print(home_perimeter)


# Задача № 2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


numbers = Math(10, 5)
numbers_1 = numbers.addition()
numbers_2 = numbers.multiplication()
numbers_3 = numbers.division()
numbers_4 = numbers.subtraction()
print(numbers_1)
print(numbers_2)
print(numbers_3)
print(numbers_4)

# Задача № 3
class Elements:
    def __init__(self, text, type):
        self.text = text
        self.type = type
    def click(self):
        return "Клик по кнопке - {}".format(self.text)
button_1 = Elements('Text Box', 'Кнопка')
button_2 = Elements('Check Box', 'Кнопка')
button_3 = Elements('Radio Button', 'Кнопка')
button_4 = Elements('Web Tables', 'Кнопка')
button_5 = Elements('Button', 'Кнопка')
button_6 = Elements('Links', 'Кнопка')
button_7 = Elements('Broken Links - Images', 'Кнопка')
button_8 = Elements('Upload and Download', 'Кнопка')
button_9 = Elements('Dynamic Properties', 'Кнопка')
print(button_1.text)
print(button_2.text)
print(button_3.text)
print(button_4.text)
print(button_5.text)
print(button_6.text)
print(button_7.text)
print(button_8.text)
print(button_9.text)
print(button_1.click())
print(button_2.click())
print(button_3.click())
print(button_4.click())
print(button_5.click())
print(button_6.click())
print(button_7.click())
print(button_8.click())
print(button_9.click())
