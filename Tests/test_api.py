import allure
from random import choice


@allure.title('Проверить функциональность добавления сущности.')
@staticmethod
def test_create_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерируем cущество'):
        entity = entitymodel(**generate_data())

    id = int(entity_api.create_entity(entity))

    in_list = entity_api.get_entity(id)

    with allure.step('Смотрим если сущность есть в списке'):
        assert in_list, (
            'Существо не было создано.'
        )


@allure.title('Проверить функциональность удаления сущности.')
@staticmethod
def test_delete_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерируем cущество'):
        entity = entitymodel(**generate_data())

    id = int(entity_api.create_entity(entity))

    entity_api.delete_entity(id)

    in_list = entity_api.get_entity(id)
    with allure.step('Смотрим если сущность удалилась'):
        assert not in_list, (
            'Существо не удалилось.'
        )


@allure.title('Проверить функциональность получения сущности.')
@staticmethod
def test_get_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерируем cуществ'):
        entity = entitymodel(**generate_data())

    id = entity_api.create_entity(entity)

    in_list = entity_api.get_entity(id)

    with allure.step('Посмотрим если существо было получено'):
        assert in_list, (
            'Существо не было получено.'
        )


@allure.title('Проверить функциональность получения списка сущностей.')
@staticmethod
def test_get_entities(entity_api):
    entities = entity_api.get_all_entities()

    with allure.step('Посмотрим если был получен список существ.'):
        assert entities != [], (
            'Существо не было получено.'
        )


@allure.title('Проверить функциональность изменения сущности.')
@staticmethod
def test_patch_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерируем cуществ для изменения'):
        entity = entitymodel(**generate_data())

    id = choice(entity_api.get_all_entities()).id
    old_entity = entity_api.get_entity(id)

    entity_api.patch_entity(id, entity)

    new_entity = entity_api.get_entity(id)

    with allure.step('Смотрим если существо изменилось.'):
        assert new_entity.model_dump_json() != old_entity.model_dump_json(), (
            'Существо не изменено.'
        )