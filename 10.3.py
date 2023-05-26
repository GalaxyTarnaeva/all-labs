with open('en-ru.txt', 'r', encoding="utf-8") as f:  # на чтение, чтобы русские буквы не сломались
    ru_en = {}  # словарь
    for line in f.readlines():
        words = line.strip().split(" - ")  # в массив все, кроме "-", стрип удаляет ненужные символы
        if len(words) == 2:  # проверка, нет ли внутри чего-то, кроме англи и рус слова
            ru_words = words[1].split(", ")  # удаляем запятые между переводами
            for i in ru_words:  # разделяем 2 русских слова в отдельные части
                if i not in ru_en:  # если слов нет в словаре
                    ru_en[i] = []  # делаем слово ключом, чтобы поместить туда значение перевода
            ru_en[i].append(words[0])  # добавили англ слово к русскому
with open('ru-en.txt', 'w') as f:  # запись
    for i in sorted(ru_en):  # по алфавиту
        en_words = ", ".join(sorted(ru_en[i]))  # сохраняем через запятые
        f.write(f"{i} - {en_words}\n")  # рус = англ