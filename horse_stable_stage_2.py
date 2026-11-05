# === Stage 2: Проверка полей ===
# Project: HorseStable
import re

VALID_STATUSES = {"домашняя", "на выгуле", "в тренировке", "на отпуске"}
AGE_PATTERNS = [
    (re.compile(r"(\d+)\s*(год|лет|годов|году|года)"), "лет"),
    (re.compile(r"(\d+)\s*(мес|месяцев|месяц|месяцу|месяца)"), "месяцев"),
    (re.compile(r"(\d+)\s*недель"), "недель"),
    (re.compile(r"(\d+)\s*дней"), "дней"),
]


def normalize_status(raw: str) -> str:
    key = raw.strip().lower()
    for candidate in VALID_STATUSES:
        if key == candidate or key in candidate:
            return candidate
    return raw.strip()


def normalize_age(raw: str) -> str:
    text = raw.strip()
    for pattern, unit in AGE_PATTERNS:
        match = pattern.search(text)
        if match:
            return f"{int(match.group(1))} {unit}"
    return text


def normalize_breed(raw: str) -> str:
    text = raw.strip()
    cleaned = re.sub(r"[^a-zа-яё\s]", "", text.lower())
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned or text


def validate_name(raw: str) -> str:
    text = raw.strip()
    if not text:
        raise ValueError("Кличка лошади не может быть пустой.")
    if len(text) > 40:
        raise ValueError("Кличка лошади не может превышать 40 символов.")
    return text


def validate_age(raw: str) -> str:
    normalized = normalize_age(raw)
    if not normalized or not re.match(r"^\d+\s*$", normalized):
        raise ValueError("Укажите возраст в цифрах, например: 5 лет.")
    if not re.search(r"\D", raw):
        raise ValueError("Укажите единицу измерения возраста, например: 5 лет.")
    return normalized


def validate_breed(raw: str) -> str:
    normalized = normalize_breed(raw)
    if not normalized:
        raise ValueError("Порода лошади не может быть пустой.")
    return normalized


def validate_status(raw: str) -> str:
    normalized = normalize_status(raw)
    if normalized not in VALID_STATUSES:
        raise ValueError(
            f"Неверный статус. Допустимые значения: {', '.join(VALID_STATUSES)}."
        )
    return normalized
