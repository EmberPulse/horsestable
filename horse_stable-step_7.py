# === Stage 7: Генерация идентификаторов ===
# Project: HorseStable
import string
import secrets


PROJECT_PREFIX = "hsid"


def _generate_unique_id(prefix: str, length: int = 8) -> str:
    alphabet = string.ascii_lowercase + string.digits
    while True:
        candidate = f"{prefix}-{secrets.token_hex(length // 2)}"
        if not _is_unique(candidate):
            continue
        return candidate


def _is_unique(candidate: str) -> bool:
    for identifier in _iter_existing_identifiers():
        if identifier == candidate:
            return False
    return True


def _iter_existing_identifiers():
    from horse_stable.horses import horses
    for horse in horses:
        yield horse.id


def generate_horse_id() -> str:
    return _generate_unique_id(PROJECT_PREFIX)
