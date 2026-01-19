import random
import time
from queries import make_queries


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

    # Генеруємо масив
    array = [random.randint(1, 100) for _ in range(N)]

    # Генеруємо запити
    queries = make_queries(N, Q)

    # Запуск без кешу
    elapsed = run_no_cache(array, queries)

    print(f"Без кешу :  {elapsed:.2f} c")


if __name__ == "__main__":
    main()
