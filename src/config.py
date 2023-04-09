import pathlib
import tomllib
from dataclasses import dataclass

__all__ = (
    'Config',
    'read_toml_config_string',
    'read_toml_config_file',
)


@dataclass(frozen=True, slots=True)
class Config:
    auth_base_url: str
    office_manager_base_url: str
    country_code: str
    remember_login: bool


def read_toml_config_string(config_string: str) -> Config:
    raw_config = tomllib.loads(config_string)
    return Config(
        auth_base_url=raw_config['auth_base_url'],
        office_manager_base_url=raw_config['office_manager_base_url'],
        country_code=raw_config['country_code'],
        remember_login=raw_config['remember_login'],
    )


def read_toml_config_file(file_path: pathlib.Path) -> Config:
    config_string = file_path.read_text(encoding='utf-8')
    return read_toml_config_string(config_string)
