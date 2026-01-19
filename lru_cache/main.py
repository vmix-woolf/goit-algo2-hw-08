import random
import time
from queries import make_queries
from lru_cache import LRUCache



def range_sum_no_cache(array, left, right):
    """
    Обчислює суму елементів масиву без кешування.
    """
    return sum(array[left:right + 1])


def update_no_cache(array, index, value):
    """
    Оновлює значення елемента масиву без кешування.
    """
    array[index] = value


def run_no_cache(array, queries):
    """
    Виконує всі запити без використання кешу
    та повертає час виконання.
    """
    start = time.perf_counter()

    for query in queries:
        if query[0] == "Range":
            _, left, right = query
            range_sum_no_cache(array, left, right)
        else:
            _, index, value = query
            update_no_cache(array, index, value)

    return time.perf_counter() - start


def main():
    N = 100_000
    Q = 50_000

    base_array = [random.randint(1, 100) for _ in range(N)]
    queries = make_queries(N, Q)

    # Без кешу
    t_no_cache = run_no_cache(base_array.copy(), queries)

    # З кешем
    t_with_cache = run_with_cache(base_array.copy(), queries)

    print(f"Без кешу :  {t_no_cache:.2f} c")
    print(f"LRU-кеш  :  {t_with_cache:.2f} c")
    print(f"(прискорення ×{t_no_cache / t_with_cache:.1f})")



def range_sum_with_cache(array, left, right, cache):
    """
    Обчислює суму елементів масиву з використанням LRU-кешу.
    """
    key = (left, right)

    cached_value = cache.get(key)
    if cached_value != -1:
        return cached_value

    total = sum(array[left:right + 1])
    cache.put(key, total)
    return total


def run_with_cache(array, queries):
    """
    Виконує всі запити з використанням LRU-кешу
    та повертає час виконання.
    """
    cache = LRUCache(capacity=1000)

    start = time.perf_counter()

    for query in queries:
        if query[0] == "Range":
            _, left, right = query
            range_sum_with_cache(array, left, right, cache)
        else:
            _, index, value = query
            # Update поки що без інвалідації кешу
            array[index] = value

    return time.perf_counter() - start


if __name__ == "__main__":
    main()
