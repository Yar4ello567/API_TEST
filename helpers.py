import allure
from pydantic import ValidationError, BaseModel
from typing import Type, Optional
import json


class ResponseValidator:
    @staticmethod
    @allure.step('Проверить статус код ответа')
    def check_status_code(response, expected_codes: list[int] = [200]) -> None:
        assert response.status_code in expected_codes, (
            f'Ожидался статус код из {expected_codes}, получен {response.status_code}'
        )

    @staticmethod
    @allure.step('Валидировать ответ по модели')
    def validate_response(model: Type[BaseModel], response_data: dict) -> Optional[BaseModel]:
        try:
            return model.model_validate(response_data)
        except ValidationError as e:
            allure.attach(json.dumps(response_data, indent=2), 'Невалидный ответ')
            allure.attach(str(e), 'Ошибка валидации')
            return None

    @staticmethod
    @allure.step('Парсить JSON ответ')
    def parse_response(response) -> dict:
        try:
            return response.json()
        except ValueError as e:
            allure.attach(response.text, 'Текст ответа')
            raise ValueError(f'Ошибка парсинга JSON: {e}')
