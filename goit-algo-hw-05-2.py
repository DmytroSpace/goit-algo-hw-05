def binary_search_upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:                                         # Виконуємо цикл, поки початковий індекс не перевищить кінцевий
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:                                       # Якщо середнє значення менше шуканого - зсуваємо початковий індекс вправо
            low = mid + 1
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            return f"Кількість ітерацій: {iterations}, результат пошуку: {arr[mid]}"

    if low < len(arr):                                          # Якщо початковий індекс не перевищує довжину масиву 
        upper_bound = arr[low]                                  # оновлюємо верхню межу найближчим більшим значенням
    if upper_bound is None:
        return f"Кількість ітерацій: {iterations}, шукане число не входить в заданий список"
    return f"Кількість ітерацій: {iterations}, результат пошуку: {upper_bound}"
  

arr = [0.1, 12.2, 21.9, 32.9, 56.7, 66.0, 88.8, 99.9]            # заданий відсортований список чисел

result = binary_search_upper_bound(arr, 25)
print(result)                                                    # результат пошуку має бути: 32.9

result = binary_search_upper_bound(arr, 0)
print(result)                                                    # результат пошуку має бути: 0.1

result = binary_search_upper_bound(arr, 100)
print(result)                                                    # шукане число не входить в заданий список

result = binary_search_upper_bound(arr, 99)
print(result)                                                    # результат пошуку має бути: 99.9