"""Викторина с подсказками."""

# здесь привожу код очень похожей викторины, которую мы разрабатываем с моими детскими группами Python
# постановка задачи находится в файле victory_ТЗ.txt
# с интересом послушаю комментарии и предложения =)


from random import randrange, shuffle

QA = {
    'Год рождения Ломоносова?': '1711',
    'Год рождения Ландау?': '1908',
    'Год рождения Попова?': '1859',
    'Год рождения Курчатова?': '1903',
    'Год рождения Тамма?': '1895',
    'Год рождения Гейма?': '1958',
}
MESSAGES = {
    'CORRECT': "Верно!\n",
    'INCORRECT': "ответ неверный... попробуйте ещё\n",
    'QUIT': "Слабак!\n",
    'NEW': "хотите сыграть ещё раз? [y/n] ",
}
QUIT_KW = ("я хочу выйти", "выйти", "выход", )

answers = {
    'total': 0,
    'correct': 0,
    'wrong': 0,
}


def get_letter(word, mask):
    if not mask:
        return '*' * len(word)
    while True:
        i = randrange(len(word))
        if mask[i] == '*':
            mask = mask[:i] + word[i] + mask[i+1:]
            break
    return mask


def calc_stats() -> str:
    """Возвращает статистику результатов игры в форматированном виде.

    Процент правильных ответов считается от количества вопросов. Процент неправильных ответов считается от всех ответов.
    """
    return (f"Количество правильных ответов: {answers['correct']}\n"
            f"Процент отвеченных вопросов: {answers['correct']*100/len(QA):.0f}%\n"
            f"Количество неправильных ответов: {answers['wrong']}\n"
            f"Процент неправильных ответов: {answers['wrong']*100/answers['total']:.0f}%")


print('='*30, 'ВИКТОРИНА', '='*30)

quit: bool = False

question_list = list(QA.keys())
shuffle(question_list)

while True:
    for question in question_list:
        print(f"\n{question}\n")
        mask = ''
        let_in_ans = len(QA[question])
        while True:
            mask = get_letter(QA[question], mask)
            prompt = f"{let_in_ans} букв: {mask}\nваш ответ: "
            answer = input(prompt)
            answers['total'] += 1
            if answer == QA[question]:
                print(MESSAGES['CORRECT'])
                answers['correct'] += 1
                break
            elif answer.lower().strip() in QUIT_KW:
                print(MESSAGES['QUIT'])
                quit = True
                break
            else:
                answers['wrong'] += 1
                if mask.count('*') > 1:
                    print(MESSAGES['INCORRECT'])
                else:
                    print(f"Правильный ответ: {QA[question]}\n")
                    break
        if quit:
            break
    print(calc_stats(), end='\n\n')
    if quit or input(MESSAGES['NEW']).lower().strip() != 'y':
        break
    print()
