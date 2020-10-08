d = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
}
#1
a = d.keys()

test_keys = []
for i in a:
    test_keys.append(f'{i}' + f'{len(i)}')

test_values = d.values()

res = dict(zip(test_keys, test_values))
print(res)

#2
a = d.keys()
test_keys = []
rez = []
i = 0
j = len(a)

while i < j:

    i += 1

test_values = d.values()

res = dict(zip(test_keys, test_values))
print(res)