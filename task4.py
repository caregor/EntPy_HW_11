# ------------------------------------------- 4 -----------------------------
"""
📌 Доработаем класс Архив из задачи 2.
📌 Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive:
    """Документация архива данных """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_arhiv = []

        cls._instance.list_arhiv.append([args])

        return cls._instance

    def __init__(self, text: str, number: int):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.list_arhiv}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


spam = Archive("ночной страж", 65)
print(f'{spam.text =}, {spam.number =}')

spam_3 = Archive("дневной дозор", 1555)
print(f'{spam.text =}, {spam.number =}')

print(f'{spam.list_arhiv = }')

print(spam)
print(f"{spam=}")
