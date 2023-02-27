import os
from uuid import UUID

from config import load_config, Config


def test_load_config():
    config_text = '''[base_url]
auth = "http://localhost:8000/"
office_manager = "http://localhost:7000/"

[auth_credentials]
username = "Benedict"
password = "Cumberbatch"
role_id = 1
department_uuid = "ffa50591-7448-4c88-95bf-ec4ebc8af56d"'''

    expected = Config(
        auth_base_url='http://localhost:8000/',
        office_manager_base_url='http://localhost:7000/',
        username='Benedict',
        password='Cumberbatch',
        role_id=1,
        department_uuid=UUID('ffa50591-7448-4c88-95bf-ec4ebc8af56d'),
    )

    try:
        with open('./test_config.toml', 'w') as file:
            file.write(config_text)
        assert load_config('./test_config.toml') == expected
    finally:
        os.remove('./test_config.toml')
