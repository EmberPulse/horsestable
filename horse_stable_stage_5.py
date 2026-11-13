# === Stage 5: Удаление и восстановление ===
# Project: HorseStable
import datetime


class Horse:
    def __init__(self, name, age, breed, status):
        self.id = None
        self.name = name
        self.age = age
        self.breed = breed
        self.status = status
        self.deleted = False
        self.deleted_at = None
        self.deleted_reason = None

    def soft_delete(self, reason):
        self.deleted = True
        self.deleted_at = datetime.datetime.now().isoformat()
        self.deleted_reason = reason

    def restore(self):
        if not self.deleted:
            raise ValueError('horse is not deleted')
        self.deleted = False
        self.deleted_at = None
        self.deleted_reason = None

    def delete(self, reason):
        self.soft_delete(reason)


class HorseStable:
    def __init__(self):
        self._horses = {}

    def add_horse(self, name, age, breed, status):
        horse = Horse(name, age, breed, status)
        horse.id = len(self._horses) + 1
        self._horses[horse.id] = horse
        return horse

    def get_horse(self, horse_id):
        return self._horses.get(horse_id)

    def list_active_horses(self):
        return [h for h in self._horses.values() if not h.deleted]

    def list_deleted_horses(self):
        return [h for h in self._horses.values() if h.deleted]

    def delete_horse(self, horse_id, reason='user request'):
        horse = self.get_horse(horse_id)
        if horse is None:
            raise KeyError(f'no horse with id {horse_id}')
        horse.delete(reason)
        return horse

    def restore_horse(self, horse_id):
        horse = self.get_horse(horse_id)
        if horse is None:
            raise KeyError(f'no horse with id {horse_id}')
        horse.restore()
        return horse

    def remove_horse_permanently(self, horse_id):
        horse = self.get_horse(horse_id)
        if horse is None:
            raise KeyError(f'no horse with id {horse_id}')
        del self._horses[horse_id]
        return horse


if __name__ == '__main__':
    stable = HorseStable()
    stallion = stable.add_horse('Богдан', 5, 'Ахалтекинский', 'healthy')
    print('added:', stallion.id, stallion.name)

    stable.delete_horse(stallion.id, reason='sold out')
    print('active after delete:', [h.name for h in stable.list_active_horses()])
    print('deleted:', [h.name for h in stable.list_deleted_horses()])

    stable.restore_horse(stallion.id)
    print('active after restore:', [h.name for h in stable.list_active_horses()])

    stable.remove_horse_permanently(stallion.id)
    print('active after permanent remove:', [h.name for h in stable.list_active_horses()])
    print('stable still has records:', len(stable._horses))
