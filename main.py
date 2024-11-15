# pip install faker
from faker import Faker

# Создаем экземпляр Faker
fake = Faker('ru_RU')  # Можно выбрать другой язык, например 'en_US'

# Генерируем фейковые данные
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.middle_name()
full_name = f"{last_name} {first_name} {middle_name}"
date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
address = fake.address()
phone_number = fake.phone_number()
hobby = fake.word(ext_word_list=['чтение', 'музыка', 'спорт', 'путешествия', 'кулинария', 'фотография', 'искусство', 'танцы']) # Вписано мало, вы можете сами добавить свой список

# Выводим сгенерированные данные
print(f"ФИО: {full_name}")
print(f"Дата рождения: {date_of_birth}")
print(f"Адрес проживания: {address}")
print(f"Номер телефона: {phone_number}")
print(f"Хобби: {hobby}")
