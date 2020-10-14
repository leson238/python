import time


class Bucket:
    def __init__(self, max_requests, refill_period, refill_amount):
        self.max_requests = max_requests
        self.refill_period = refill_period
        self.refill_amount = refill_amount
        self.reset()

    def _refill_count(self):
        return int((time.time() - self.last_update) / self.refill_period)

    def reset(self):
        self.value = self.max_requests
        self.last_update = time.time()

    def _clamp(self):
        return min(self.max_requests, self.value + self._refill_count() * self.refill_amount)

    def reducer(self, tokens):
        refill_count = self._refill_count()
        self.value += refill_count * self.refill_amount
        self.last_update += refill_count * self.refill_period

        if self.value >= self.max_requests:
            self.reset()
        if tokens > self.value:
            return False
        self.value -= tokens
        return True
