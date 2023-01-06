"""Ветвления с циклами."""

from datetime import datetime as dt

correct_date = dt(year=1799, month=6, day=6)

OK_MESSAGE = "Верно"
ERR_MESSAGES = {
    'FORMAT': "\t_ обнаружены некорректные символы _",
    'YEAR': "\t_ неверный год рождения _",
    'DAY_MONTH': "\t_ неверный день рождения _",
}
PROMPT1 = 'введите правильный год рождения Александра Сергеевича Пушкина цифрами > '
PROMPT2 = 'введите правильные день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > '

while True:
    ans_year = input(PROMPT1)
    if ans_year.isdecimal():
        if int(ans_year) == correct_date.year:
            break
        else:
            print(ERR_MESSAGES['YEAR'])
    else:
        print(ERR_MESSAGES['FORMAT'])

while True:
    try:
        ans_day_month = input(PROMPT2)
        ans_date = dt.strptime(f"{ans_day_month}.{ans_year}", '%d.%m.%Y')
    except ValueError:
        print(ERR_MESSAGES['FORMAT'])
        continue

    if ans_date == correct_date:
        print(OK_MESSAGE)
        break
    else:
        print(ERR_MESSAGES['DAY_MONTH'])


# stdout:
# введите правильный год рождения Александра Сергеевича Пушкина цифрами > не знаю
#     _ обнаружены некорректные символы _
# введите правильный год рождения Александра Сергеевича Пушкина цифрами > 2022
#     _ неверный год рождения _
# введите правильный год рождения Александра Сергеевича Пушкина цифрами > 1799
# введите правильные день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > какого-то июня
#     _ обнаружены некорректные символы _
# введите правильные день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > 12.06
#     _ неверный день рождения _
# введите правильные день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > 6.06
# Верно
