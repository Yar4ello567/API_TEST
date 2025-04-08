import pytest
from dataclasses import asdict
from Entity.entity_model import Entity
from Services.Entity.data_generator import DataGenerator
from Services.Entity.entity_request import EntityRequestHandler

@pytest.fixture
def entity_api() -> EntityRequestHandler:
    return EntityRequestHandler()

@pytest.fixture
def entitymodel():
    return Entity

@pytest.fixture
def generate_data():
    def _generate_data():
        return asdict(DataGenerator.generate_entity_data())
    return _generate_data
