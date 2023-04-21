from main2 import upper, lower


def sum_arg(a, b):
    return a + b


print(sum_arg(a=1, b=2))

print(sum([1, 7]))

print('A' * 5)

a: dict = {
    'a': 5,
    'b': 3
}
b: list = [1, 2, 3]
c: tuple = (1, 2, 3)
d: set = set()

names = ['Тимур', 'Стас']

names.append('Саша')
names.append('Саша')

print(set(names))

print(upper('abc'))
print(lower('aBc'))

print('Hello git')