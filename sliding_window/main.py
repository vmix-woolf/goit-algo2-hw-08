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
