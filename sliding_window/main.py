import time
from collections import deque
from typing import Dict


class SlidingWindowRateLimiter:
    def __init__(self, window_size: int = 10, max_requests: int = 1):
        """
        Ініціалізує rate limiter з заданим розміром вікна та лімітом запитів.
        """
        self.window_size = window_size
        self.max_requests = max_requests
        self.user_requests: Dict[str, deque] = {}

    def _cleanup_window(self, user_id: str, current_time: float) -> None:
        """
        Видаляє застарілі повідомлення з часовго вікна користувача.
        Якщо після очищення вікно порожнє — користувач видаляється.
        """
        if user_id not in self.user_requests:
            return

        window = self.user_requests[user_id]

        while window and current_time - window[0] > self.window_size:
            window.popleft()

        if not window:
            del self.user_requests[user_id]

    def can_send_message(self, user_id: str) -> bool:
        """
        Перевіряє, чи може користувач відправити повідомлення
        у поточному часовому вікні.
        """
        current_time = time.time()

        self._cleanup_window(user_id, current_time)

        if user_id not in self.user_requests:
            return True

        return len(self.user_requests[user_id]) < self.max_requests

    def record_message(self, user_id: str) -> bool:
        """
        Записує нове повідомлення користувача,
        якщо ліміт не перевищено.
        """
        current_time = time.time()

        if not self.can_send_message(user_id):
            return False

        if user_id not in self.user_requests:
            self.user_requests[user_id] = deque()

        self.user_requests[user_id].append(current_time)
        return True

    def time_until_next_allowed(self, user_id: str) -> float:
        """
        Повертає час очікування (у секундах)
        до можливості відправлення наступного повідомлення.
        """
        current_time = time.time()

        self._cleanup_window(user_id, current_time)

        if user_id not in self.user_requests:
            return 0.0

        window = self.user_requests[user_id]

        if len(window) < self.max_requests:
            return 0.0

        # Час до звільнення першого повідомлення у вікні
        oldest_timestamp = window[0]
        wait_time = self.window_size - (current_time - oldest_timestamp)

        return max(0.0, wait_time)


import random
import time


def test_rate_limiter():
    # Створюємо rate limiter: вікно 10 секунд, 1 повідомлення
    limiter = SlidingWindowRateLimiter(window_size=10, max_requests=1)

    # Симулюємо потік повідомлень від користувачів
    print("\n=== Симуляція потоку повідомлень ===")
    for message_id in range(1, 11):
        user_id = message_id % 5 + 1

        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))

        print(
            f"Повідомлення {message_id:2d} | Користувач {user_id} | "
            f"{'✓' if result else f'× (очікування {wait_time:.1f}с)'}"
        )

        time.sleep(random.uniform(0.1, 1.0))

    print("\nОчікуємо 4 секунди...")
    time.sleep(4)

    print("\n=== Нова серія повідомлень після очікування ===")
    for message_id in range(11, 21):
        user_id = message_id % 5 + 1

        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))

        print(
            f"Повідомлення {message_id:2d} | Користувач {user_id} | "
            f"{'✓' if result else f'× (очікування {wait_time:.1f}с)'}"
        )

        time.sleep(random.uniform(0.1, 1.0))


if __name__ == "__main__":
    test_rate_limiter()
