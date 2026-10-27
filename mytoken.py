from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: str

    def __str__(self):
        return f"{self.type} : {self.value}"

    def __repr__(self):
        return self.__str__()