from typing import Optional
import allure
from pydantic import BaseModel

from Entity.entity_model import Entity
from endpoints import Endpoints
from helpers import ResponseValidator
from request_handler import BaseRequestHandler  # Убедитесь, что файл в корне проекта


class EntityRequestHandler(BaseRequestHandler):
    @allure.step('Отправляем запрос добавления сущности')
    def create_entity(self, entity: Entity) -> int:
        response = self._send_request(
            'POST',
            Endpoints.CREATE,
            entity.model_dump_json()
        )
        return int(response.json())

    @allure.step('Отправляем запрос удаления сущности')
    def delete_entity(self, entity_id: int) -> None:
        response = self._send_request(
            'DELETE',
            Endpoints.DELETE.format(id=entity_id),
            expected_codes=[200, 204]  # Принимаем оба статуса
        )

    @allure.step('Отправляем запрос получения сущности')
    def get_entity(self, entity_id: int) -> Optional[Entity]:
        try:
            response = self._send_request(
                'GET',
                Endpoints.GET.format(id=entity_id),
                expected_codes=[200, 404]  # Ожидаем либо сущность, либо 404 если не найдена
            )
            if response.status_code == 404:
                return None
            return ResponseValidator.validate_response(Entity, response.json())
        except ValueError as e:
            allure.attach(str(e), "Ошибка при получении сущности")
            return None

    @allure.step('Отправляем запрос получения списка всех сущностей')
    def get_all_entities(self) -> list[Entity]:
        response = self._send_request('GET', Endpoints.GET_ALL)
        data = response.json()
        return [ResponseValidator.validate_response(Entity, entity) for entity in data['entity']]

    @allure.step('Отправляем запрос изменения сущности')
    def patch_entity(self, entity_id: int, entity: Entity) -> None:
        response = self._send_request(
            'PATCH',
            Endpoints.PATCH.format(id=entity_id),
            entity.model_dump_json(),
            expected_codes=[200, 204]
        )
