def student_data(info):
    print(f'name: {info[0]}')
    print(f'course: {info[1]}')
    print(f'Gra_year: {info[2]}')
    print('------end--------')

data = [['varsha','FPS','2026'],
        ['SAAKETH','JFS','2025'],
        ['DILEEP','DA','2025'],
        ['SIRISHA','DS','2026']
        ]

for i in data:
        student_data(i)
