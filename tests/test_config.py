import pathlib
import textwrap

from config import read_toml_config_string, read_toml_config_file, Config

CONFIG_STRING = textwrap.dedent('''\
    auth_base_url = "https://auth.dodois.test"
    office_manager_base_url = "https://officemanager.dodois.test"
    country_code = "kg"
    remember_login = true
''')

EXPECTED_CONFIG = Config(
    auth_base_url='https://auth.dodois.test',
    office_manager_base_url='https://officemanager.dodois.test',
    country_code='kg',
    remember_login=True,
)


def test_toml_config_string_reader():
    assert read_toml_config_string(CONFIG_STRING) == EXPECTED_CONFIG


def test_toml_config_file_reader():
    file_path = pathlib.Path(__file__).parent / 'temp_config.toml'
    file_path.write_text(CONFIG_STRING)

    try:
        assert read_toml_config_file(file_path) == EXPECTED_CONFIG
    finally:
        file_path.unlink(missing_ok=True)
