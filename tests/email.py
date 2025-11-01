import datetime
import pprint

# 1. Создайте словарь email, который содержит поля:
# "subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).

email = {
    "subject": "  Quarterly Report  ",
    "from": "  Alice.Cooper@Company.ru ",
    "to": "   bob_smith@Gmail.com   ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
}

# 2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и
# запишите её в email["date"].
send_date = datetime.datetime.now()
email["date"] = send_date.strftime("%Y-%m-%d")

# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].
email["from"] = email["from"].strip().casefold()
email["to"] = email["to"].strip().casefold()

# 4. Извлеките логин и домен отправителя в две переменные login и domain.
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]

# 5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"]
short_body_text = email["body"][:10]
email["short_body"] = short_body_text + "..."

# 6. Список персональных доменов
personal_domain = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
    "company.ru",
]
# Список корпоративных доменов с условием отсутствия дублей - сначала создаем сет. Затем превращаем его в лист
corporate_domain = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
]

personal_domain_set = set(personal_domain)
corporate_domain_set = set(corporate_domain)
personal_domain = list(personal_domain_set)
corporate_domain = list(corporate_domain_set)

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
# ни один домен не должен входить в оба списка одновременно.
if personal_domain_set & corporate_domain_set:
    print("Найдено пересечение!")
else:
    print("Домены уникальны!")

# 8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки
# вхождения домена отправителя в список корпоративных доменов.
is_corporate = domain in corporate_domain

# 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
# Сохраните в email["clean_body"].
clean_body = email["body"].replace("\n", " ").replace("\t", " ")
email["clean_body"] = clean_body

# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}

sent_text = (
    f"Кому: {email['to']}, от {email['from']} Тема: {email['subject']}, "
    f'дата {email['date']} {email["clean_body"]}'
)
email["sent_text"] = sent_text

# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону
len_sent_text = len(email["sent_text"])
pages = (len(email["sent_text"]) + 499) // 500

# 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty, is_body_empty в котором будет храниться
# что тема письма содержит данные
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].
masked_from = login[:2] + "***@" + domain
email["masked_from"] = masked_from

# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru"
for i in range(0, personal_domain.count("list.ru")):
    personal_domain.remove("list.ru")
personal_domain.remove("bk.ru")

text_result = "Ключевые результаты"
text_result.center(20, "-")
print(text_result)
pprint.pprint(email)
print(f"Логин: {login}")
print(f"Домен: {domain}")
print(personal_domain)
print(corporate_domain)
print(f"Количество страниц для печати = {pages}")
print(f"Домен входит в список корпоративных доменов: {is_corporate}")
print(f'Пустая тема письма: {is_subject_empty}, пустое тело письма: {is_body_empty}')
