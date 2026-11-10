# === Stage 3: Хранилище в памяти ===
# Project: HorseStable
from typing import List, Optional


class Horse:
    def __init__(self, name: str, age: int, breed: str, status: str = "healthy"):
        self.name = name
        self.age = age
        self.breed = breed
        self.status = status
        self.id = self._generate_id()

    def _generate_id(self) -> int:
        return self._stable._next_id()

    def __repr__(self) -> str:
        return f"Horse(id={self.id}, name={self.name!r}, age={self.age}, breed={self.breed!r}, status={self.status!r})"


class InMemoryHorseStore:
    def __init__(self):
        self._horses: dict[int, Horse] = {}
        self._next_id = 1

    def add(self, name: str, age: int, breed: str, status: str = "healthy") -> Horse:
        horse = Horse(name, age, breed, status)
        self._horses[horse.id] = horse
        return horse

    def get(self, horse_id: int) -> Optional[Horse]:
        return self._horses.get(horse_id)

    def list(self) -> List[Horse]:
        return list(self._horses.values())


if __name__ == "__main__":
    store = InMemoryHorseStore()

    pegasus = store.add("Перегон", 5, "Ахалтекинская")
    thunder = store.add("Гром", 3, "Арабская")
    mist = store.add("Туман", 4, "Тракененская")

    print("В конюшне:")
    for horse in store.list():
        print("  ", horse)

    print("\nПерегон:", store.get(pegasus.id))
    print("Гром:", store.get(thunder.id))
    print("Отсутствует (id=999):", store.get(999))

    print("\nПосле добавления Бурого:")
    brown = store.add("Бурый", 6, "Симентальская")
    for horse in store.list():
        print("  ", horse)

    print("\nПоследний id:", brown.id)
