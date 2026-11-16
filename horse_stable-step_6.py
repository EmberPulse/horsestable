# === Stage 6: Связанная сущность ===
# Project: HorseStable
from horse_stable.horse import Horse


class Training:
    def __init__(self, name, duration, horse_id):
        self.name = name
        self.duration = duration
        self.horse_id = horse_id

    def add(self, horses):
        if self.horse_id not in horses:
            raise ValueError(f"Лошадь {self.horse_id} не найдена")
        horses[self.horse_id].last_training = self.name
        return horses[self.horse_id]
