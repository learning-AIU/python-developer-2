"""Ветвление."""

from datetime import datetime as dt

correct_date = dt(year=1799, month=6, day=6)

OK_MESSAGE = "Верно"
ERR_MESSAGES = {
    'FORMAT': "_ обнаружены некорректные символы _",
    'YEAR': "_ неверный год рождения _",
    'DAY_MONTH': "_ неверный день рождения _",
}
PROMPT1 = '\nвведите год рождения Александра Сергеевича Пушкина цифрами > '
PROMPT2 = 'введите день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > '

try:
    ans_year = int(input(PROMPT1))
    if ans_year == correct_date.year:
        ans_day_month = input(PROMPT2)
        ans_date = dt.strptime(f"{ans_day_month}.{ans_year}", '%d.%m.%Y')
        if ans_date == correct_date:
            print(OK_MESSAGE)
        else:
            print(ERR_MESSAGES['DAY_MONTH'])
    else:
        print(ERR_MESSAGES['YEAR'])
# на случай, если пользователь ввёл запрашиваемые данные в неверном формате
except ValueError:
    print(ERR_MESSAGES['FORMAT'])


# stdout:
# введите год рождения Александра Сергеевича Пушкина цифрами > 1836
# _ неверный год рождения _

# введите год рождения Александра Сергеевича Пушкина цифрами > 1799
# введите день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > 01.01
# _ неверный день рождения _

# введите год рождения Александра Сергеевича Пушкина цифрами > 1799
# введите день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > 6.06
# Верно
