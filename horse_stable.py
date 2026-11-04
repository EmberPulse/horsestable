# === Stage 1: Каркас модуля ===
# Project: HorseStable
from dataclasses import dataclass, field
from enum import Enum


class Статус(Enum):
    ЗДОРОВ = "здоров"
    БОЛЕН = "болен"
    ТРЕНИРОВКА = "в тренировке"


@dataclass
class Лошадь:
    кличка: str
    возраст: int
    порода: str
    статус: Статус = Статус.ЗДОРОВ
    здоровье: float = field(default=100.0)
    выносливость: float = field(default=100.0)


def create_demo_horses() -> list[Лошадь]:
    return [
        Лошадь("Булат", 5, "Ахалтекинский", Статус.ЗДОРОВ),
        Лошадь("Заря", 3, "Англо-арабская", Статус.ТРЕНИРОВКА),
        Лошадь("Тень", 7, "Трактур", Статус.БОЛЕН),
    ]


def print_horses(horses: list[Лошадь]) -> None:
    print("=== Конюшня HorseStable ===")
    for horse in horses:
        print(f"{horse.кличка} | возраст: {horse.возраст} | "
              f"порода: {horse.порода} | статус: {horse.статус.value} | "
              f"здоровье: {horse.здоровье:.0f} | выносливость: {horse.выносливость:.0f}")


def main() -> None:
    horses = create_demo_horses()
    print_horses(horses)


if __name__ == "__main__":
    main()
