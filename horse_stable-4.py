# === Stage 4: Редактирование записей ===
# Project: HorseStable
def edit_horse(stable, horse_id, changes):
    allowed_fields = {'age', 'breed', 'status'}
    for key in changes:
        if key not in allowed_fields:
            raise ValueError(f"Поле '{key}' нельзя изменить")
    for horse in stable:
        if horse['id'] == horse_id:
            for key, value in changes.items():
                if key in allowed_fields:
                    horse[key] = value
            return True
    return False
