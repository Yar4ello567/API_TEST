from dataclasses import dataclass
from random import randint
from typing import Dict, List, Union


@dataclass
class EntityData:
    addition: Dict[str, Union[str, int]]
    important_numbers: List[int]
    title: str
    verified: bool = True


class DataGenerator:
    @staticmethod
    def generate_entity_data() -> EntityData:
        title = ''.join(chr(randint(97, 122)) for _ in range(randint(4, 10)))
        return EntityData(
            addition={
                'additional_info': 'Дополнительные сведения',
                'additional_number': randint(0, 10)
            },
            important_numbers=[randint(0, 99) for _ in range(randint(1, 3))],
            title=title
        )
