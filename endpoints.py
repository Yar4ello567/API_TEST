class Endpoints:
    BASE_URL = '/api'
    CREATE = f'{BASE_URL}/create'
    DELETE = f'{BASE_URL}/delete/{{id}}'
    GET = f'{BASE_URL}/get/{{id}}'
    GET_ALL = f'{BASE_URL}/getAll'
    PATCH = f'{BASE_URL}/patch/{{id}}'
