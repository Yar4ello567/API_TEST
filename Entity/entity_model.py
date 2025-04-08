from typing import Dict, List, Union, Optional

from pydantic import BaseModel


class Entity(BaseModel):
    """Модель объекта сущности"""
    id: Optional[int] = None
    addition: Dict[str, Union[str, int, Optional[int]]]
    important_numbers: List[int]
    title: str
    verified: bool
