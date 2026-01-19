import random


def make_queries(n, q, hot_pool=30, p_hot=0.95, p_update=0.03):
    """
    Генерує список запитів для тестування.
    Більшість Range-запитів звертаються до «гарячих» діапазонів.
    """
    hot_ranges = [
        (random.randint(0, n // 2), random.randint(n // 2, n - 1))
        for _ in range(hot_pool)
    ]

    queries = []

    for _ in range(q):
        if random.random() < p_update:
            # Update-запит
            index = random.randint(0, n - 1)
            value = random.randint(1, 100)
            queries.append(("Update", index, value))
        else:
            # Range-запит
            if random.random() < p_hot:
                left, right = random.choice(hot_ranges)
            else:
                left = random.randint(0, n - 1)
                right = random.randint(left, n - 1)
            queries.append(("Range", left, right))

    return queries
