import requests
from typing import Optional
import json

from main2 import test_func

URL = 'https://api.pushshift.io/reddit/comment/search/'
UNDEFINED = 'undefined'
FILE_NAME = '../comments.json'


def get_response(url: str) -> Optional[requests.Response]:
    try:
        return requests.get(url)
    except Exception:
        print(f'Can not handle GET request to {URL}')


def handle_response(response: Optional[requests.Response]) -> None:
    def save_to_file(payload: dict, file_name: str) -> None:
        with open(file_name, 'w+') as f:
            if 'data' not in payload and isinstance(payload['data'], list):
                return

            json.dump(
                [{item.get('retrieved_on', UNDEFINED): item.get('body', UNDEFINED)} for item in payload['data']],
                f,
                indent=4
            )

    if not response:
        print('Empty response')
    elif not response.ok:
        print('Status is not 200')

    try:
        payload = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        print(f'Can not parse to JSON: {response.text}')
        return

    save_to_file(payload, FILE_NAME)


if __name__ == '__main__':
    response = get_response(URL)
    handle_response(response)
    test_func()
