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
}
QUIT_KW = ("я хочу выйти", "выйти", "выход", )

scores = 0


def get_letter(word, mask):
    global scores
    if not mask:
        return '*' * len(word)
    while True:
        i = randrange(len(word))
        if mask[i] == '*':
            mask = mask[:i] + word[i] + mask[i+1:]
            scores -= 1
            break
    return mask


def show_score():
    print(f"Ваш общий счёт: {scores}\n")


print('='*30, 'ВИКТОРИНА', '='*30)

quit: bool = False

question_list = list(QA.keys())
shuffle(question_list)

for question in question_list:
    print(f"\n{question}\n")
    mask = ''
    let_in_ans = len(QA[question])
    while True:
        mask = get_letter(QA[question], mask)
        prompt = f"{let_in_ans} букв: {mask}\nваш ответ: "
        answer = input(prompt)
        if answer == QA[question]:
            print(MESSAGES['CORRECT'])
            scores += let_in_ans
            show_score()
            break
        elif answer.lower().strip() in QUIT_KW:
            print(MESSAGES['QUIT'])
            quit = True
            break
        else:
            if mask.count('*') > 1:
                print(MESSAGES['INCORRECT'])
            else:
                print(f"Правильный ответ: {QA[question]}\n")
                scores -= 1
                show_score()
                break
    if quit:
        break

show_score()
