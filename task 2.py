class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity  # Вместимость кэша
        self.cache_dict = {}  # Словарь для хранения элементов кэша

    @property
    def cache(self):
        least_recently_used = next(iter(self.cache_dict))
        # Получение ключа самого старого элемента
        return (least_recently_used, self.cache_dict[least_recently_used])
        # Возвращение кортежа (ключ, значение)

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        # Распаковка нового элемента
        if key in self.cache_dict:
            # Если ключ уже есть в кэше
            del self.cache_dict[key]
            # Удаляем элемент, чтобы обновить его положение
        elif len(self.cache_dict) == self.capacity:
            # Если превышено ограничение вместимости кэша
            del self.cache_dict[next(iter(self.cache_dict))]
            # Удаляем самый старый элемент
        self.cache_dict[key] = value
        # Добавляем новый элемент в кэш

    def get(self, key):
        if key in self.cache_dict:
            # Если ключ есть в кэше
            value = self.cache_dict[key]
            # Получаем значение
            del self.cache_dict[key]
            # Удаляем элемент
            self.cache_dict[key] = value
            # Добавляем элемент обратно в кэш
            return value
            # Возвращаем значение

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            # Перебираем элементы кэша
            print(f"{key} : {value}")
            # Выводим ключ и значение


# Пример использования
cache = LRUCache(3)

cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

cache.print_cache()
print(cache.get("key2"))

cache.cache = ("key4", "value4")

cache.print_cache()