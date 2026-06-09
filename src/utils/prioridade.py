from enum import Enum

class Prioridade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

    # Permite comparar prioridades usando "<".
    def __lt__(self, outro):
        if self.__class__ is outro.__class__:
            return self.value < outro.value
        return NotImplemented

    # Permite comparar prioridades usando "<=".
    def __le__(self, outro):
        if self.__class__ is outro.__class__:
            return self.value <= outro.value
        return NotImplemented