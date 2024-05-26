class Person:
    def __init__(self, name, person_id):
        self._name = name
        self._person_id = person_id

    @property
    def name(self):
        return self._name

    @property
    def person_id(self):
        return self._person_id
