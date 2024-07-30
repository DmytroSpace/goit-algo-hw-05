class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)
                    return True
        return False

if __name__ == '__main__':
                                                    # Тестуємо нашу хеш-таблицю:
    H = HashTable(10)
    
                                                    # Додаємо пісні
    H.insert("Bohemian Rhapsody", "1975")
    H.insert("Don't Stop Me Now", "1978")
    H.insert("We Will Rock You", "1977")
    H.insert("Another One Bites the Dust", "1980")

                                                    # Отримуємо пісні
    print(H.get("Bohemian Rhapsody"))               # Виведе: 1975
    print(H.get("Don't Stop Me Now"))               # Виведе: 1978
    print(H.get("We Will Rock You"))                # Виведе: 1977
    print(H.get("Another One Bites the Dust"))      # Виведе: 1980

                                                    # Видаляємо пісні за допомогою методу delete
    H.delete("Bohemian Rhapsody")
    H.delete("We Will Rock You")

                                                    # Перевіряємо видалення
    print(H.get("Bohemian Rhapsody"))               # Виведе: None
    print(H.get("We Will Rock You"))                # Виведе: None

                                                    # Перевіряємо таблицю
    print(H.table)                                  # Виведе хеш-таблицю без "Bohemian Rhapsody" і "We Will Rock You"
                                                    # тобто вміст з 4 буде мати тільки 2 назви  "Another One Bites the Dust" та "Don't Stop Me Now"