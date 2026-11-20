# === Stage 8: Фильтрация записей ===
# Project: HorseStable
from datetime import date


def filter_horses_by_age(horses, min_age=None, max_age=None):
    """Фильтрация лошадей по возрасту (в годах)."""
    result = []
    for horse in horses:
        if min_age is not None and horse["age"] < min_age:
            continue
        if max_age is not None and horse["age"] > max_age:
            continue
        result.append(horse)
    return result


def filter_horses_by_date_range(horses, start_date=None, end_date=None):
    """Фильтрация лошадей по диапазону дат рождения.

    Поле "age" в записях лошади — это строка в формате "ГГГГ-ММ-ДД".
    """
    result = []
    for horse in horses:
        birth = date.fromisoformat(horse["age"])
        if start_date is not None and birth < start_date:
            continue
        if end_date is not None and birth > end_date:
            continue
        result.append(horse)
    return result


def filter_horses(horses, min_age=None, max_age=None, start_date=None, end_date=None):
    """Комбинированная фильтрация лошадей по возрасту и диапазону дат рождения."""
    filtered = filter_horses_by_age(horses, min_age, max_age)
    return filter_horses_by_date_range(filtered, start_date, end_date)
