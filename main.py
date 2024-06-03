immutable_var = ('figure','number',5,7,8)
print(immutable_var)
# immutable_var [1] = 200 Кортежи в Python — это неизменяемые структуры сведений, применяемые для хранения сгруппированной последовательности. Они похожи на списки, но имеют одно важное отличие: их невозможно изменять после разработки.

immutable_var = ['figure','number',5,7,8, True]
immutable_var [2] = 6
print(immutable_var)

immutable_var = ['figure','number',5,7,8, True]
immutable_var.append(9)
print(immutable_var)

immutable_var = ['figure','number',5,7,8, True]
immutable_var.extend([4, False])
print(immutable_var)

immutable_var = ['figure','number',5,7,8, True]
immutable_var.remove(5)
print(immutable_var)