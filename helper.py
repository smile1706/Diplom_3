import requests

import curl


class UserMethods:
    @staticmethod
    def register_user(register_body):
        response = requests.post(f'{curl.register_endpoint}', json=register_body)
        return response

    @staticmethod
    def delete_user(auth_header):
        response = requests.delete(f'{curl.delete_endpoint}', headers=auth_header)
        return response
