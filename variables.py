"""Объект описания: персонаж игры."""

from re import fullmatch

name: str = 'Илья-Муромец'
health: float = 1000.0
level: int = 4
parameters: dict[str, int] = {
    'сила': 23,
    'ловкость': 16,
    'выносливость': 30,
    'интеллект': 15,
    'удача': 10,
}
inventory: list[str] = [
    'Меч-кладенец',
    'Кольчуга воронёная',
    'Шлем с бармицей',
    'Сапоги кожаные',
]
horse: bool = False
companions: set[str] = {
    'Добрыня Никитич',
    'Алёша Попович',
}

for var_name, var_value in globals().copy().items():
    if not fullmatch(r'_+?\w+?_+?', var_name):
        class_name = type(var_value).__name__
        if class_name not in ('type', 'module', 'function',):
            print(f'{var_name}: {class_name} = {var_value}')
