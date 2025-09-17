far_temperature = float(
    input(
        'Введите температуру по Фаренгейту: '
         )
                        )

cels_temperature = (far_temperature - 32)*5/9

print(cels_temperature)
