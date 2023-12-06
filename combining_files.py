import pandas as pd


crm_file = pd.read_excel('CRMFile1251023.xlsx')

# vmock_file = pd.read_excel()


crm_file.to_csv('crm_file.csv', index=False)

print(crm_file[' Full Name'])

print(crm_file.keys())

for columns in crm_file.columns:
    columns.strip()
    print(columns)

# lambda function syntax: map  parameters: expression

items = [
    ('two', 2),
    ('three', 3),
    ('four', 4),
    ('five', 5),
    ('one', 1)
]

print(sorted(items))

items.sort(key=lambda item: item[1])

print(f'print 1{items}')


def sort_list(item):
    return item[1]


items.sort(key=sort_list)
print(f'print 2 {items}')

# iterate through a list and assign it values to a new list
# method 1
new_list = []
for item in items:
    new_list.append(item[1])
print(f'method 1: {new_list}')

# method 2
x = list(map(lambda item: item[1], items))
print(f'method 2: {x}')
