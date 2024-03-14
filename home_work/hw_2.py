# Задача №1
def task_1(a: int = 7, b: float = 1.1, c: str = 'Hello',
           d: list = [1, 2, 3], e: bool = False):
    print(a, 'относится к типу', type(a))
    print(b, 'относится к типу', type(b))
    print(c, 'относится к типу', type(c))
    print(d, 'относится к типу', type(d))
    print(e, 'относится к типу', type(e))
task_1()

# Задача №2
def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list: # Последовательность Фибаначчи
    return a[0:3]
print(task_2())

# Задача №3
def task_3(a: int) -> int:
    return a ** 2
print(task_3(5))