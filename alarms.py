class Alarms:
    def __init__(self, counters, timers, steps):
        safe_number = min(len(counters), len(timers), len(steps)) + 1
        self.max_counters = counters[:safe_number]
        self.max_timers = timers[:safe_number]
        self.steps = steps[:safe_number]
        self.counters = [0] * (safe_number - 1)
        self.timers = [0] * (safe_number - 1)

    def tick(self):
        for i in range(0, len(self.counters)):
            self.timers[i] += 1
            if self.timers[i] >= self.max_timers[i]:
                self.timers[i] = 0
                self.counters[i] += self.steps[i]
                if self.counters[i] >= self.max_counters[i]:
                    self.counters[i] = 0
        return self.counters
