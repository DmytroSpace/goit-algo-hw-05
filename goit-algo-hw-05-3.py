import timeit
import re

# Алгоритм Рабіна-Карпа (Rabin-Karp)
def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

# Алгоритм Рабіна-Карпа (Rabin-Karp)
def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)  # Хеш підрядка
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)  # Хеш поточного фрагмента
    h_multiplier = pow(base, substring_length - 1) % modulus
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1

# Алгоритм Боєра-Мура (Boyer-Moore)
def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

# Алгоритм Боєра-Мура (Boyer-Moore)
def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

# Алгоритм Кнута-Морріса-Пратта (KMP)
def compute_lps(pattern):
    """Обчислити LPS масив для алгоритму Кнута-Морріса-Пратта."""
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

# Алгоритм Кнута-Морріса-Пратта (KMP)
def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)  # Отримати LPS масив
    i = j = 0
    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1

# Алгоритм регулярних виразів (Regex)
def regex_search(main_string, pattern):
    try:
        match = re.search(re.escape(pattern), main_string)  # Використовуємо re.escape для безпечного пошуку
        if match:
            return match.start()
        else:
            return -1
    except re.error as e:
        print(f"Помилка регулярного виразу: {e}")
        return -1

# Читання файлу з можливістю обробки різних кодувань
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Пробуємо UTF-8
            return file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='cp1251') as file:  # Якщо не вдалося, пробуємо CP1251
            return file.read()

# Вимірювання часу виконання функцій пошуку
def measure_search_time(func, text, pattern):
    setup_code = f'from __main__ import {func.__name__}'  # Імпорт функції
    stmt = f"{func.__name__}(text, pattern)"  # Команда для виконання
    return timeit.timeit(stmt, setup=setup_code, globals={'text': text, 'pattern': pattern}, number=10)

if __name__ == '__main__':
    text1 = read_file("article1.txt")  # Зчитування тексту з файлу
    text2 = read_file("article2.txt")  # Зчитування тексту з іншого файлу
    existing_substring = "хеш-таблиці"  # Підрядок, що існує в тексті
    fake_substring = "конкринош чаупель"  # Фейковий підрядок для тестування

    for i, text in enumerate([text1, text2]):
        print(f"\nСтаття №{i+1}")
        results = []
        for pattern in [existing_substring, fake_substring]:
            for search_func in [boyer_moore_search, kmp_search, rabin_karp_search, regex_search]:
                search_time = measure_search_time(search_func, text, pattern)
                results.append((search_func.__name__, pattern, search_time))

        print(f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час (секунди)':<15}")
        print('-' * 75)
        for result in results:
            print(f"{result[0]:<30} | {result[1]:<30} | {result[2]:<15.5f}")
