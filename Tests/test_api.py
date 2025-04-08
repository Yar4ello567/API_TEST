import allure
from random import choice


@allure.title('Проверить функциональность добавления сущности.')
def test_create_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерируем cущество'):
        entity = entitymodel(**generate_data())

    entity_id = entity_api.create_entity(entity)
    in_list = entity_api.get_entity(entity_id)

    with allure.step('Смотрим если сущность есть в списке'):
        assert in_list, 'Существо не было создано.'


@allure.title('Проверить функциональность удаления сущности.')
def test_delete_entity(entitymodel, entity_api, generate_data):
    entity = entitymodel(**generate_data())
    entity_id = entity_api.create_entity(entity)

    entity_api.delete_entity(entity_id)

    assert not entity_api.get_entity(entity_id), 'Существо не удалилось'


@allure.title('Проверить функциональность получения сущности.')
def test_get_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерируем cуществ'):
        entity = entitymodel(**generate_data())

    entity_id = entity_api.create_entity(entity)
    in_list = entity_api.get_entity(entity_id)

    with allure.step('Посмотрим если существо было получено'):
        assert in_list, 'Существо не было получено.'


@allure.title('Проверить функциональность получения списка сущностей.')
def test_get_entities(entity_api):
    entities = entity_api.get_all_entities()

    with allure.step('Посмотрим если был получен список существ.'):
        assert entities, 'Список сущностей пуст'


@allure.title('Проверить функциональность изменения сущности.')
def test_patch_entity(entitymodel, entity_api, generate_data):
    new_entity = entitymodel(**generate_data())
    all_entities = entity_api.get_all_entities()
    assert all_entities, 'Нет сущностей для изменения'

    entity_id = choice(all_entities).id
    entity_api.patch_entity(entity_id, new_entity)

    updated_entity = entity_api.get_entity(entity_id)
    assert updated_entity.title == new_entity.title, 'Название не изменилось'
