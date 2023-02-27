import pathlib
import tomllib
from dataclasses import dataclass
from uuid import UUID

__all__ = (
    'Config',
    'load_config',
)


@dataclass(frozen=True, slots=True)
class Config:
    auth_base_url: str
    office_manager_base_url: str
    username: str
    password: str
    role_id: int
    department_uuid: UUID


def load_config(file_path: str | pathlib.Path) -> Config:
    with open(file_path, 'rb') as file:
        raw_config = tomllib.load(file)

    return Config(
        auth_base_url=raw_config['base_url']['auth'],
        office_manager_base_url=raw_config['base_url']['office_manager'],
        username=raw_config['auth_credentials']['username'],
        password=raw_config['auth_credentials']['password'],
        role_id=raw_config['auth_credentials']['role_id'],
        department_uuid=UUID(raw_config['auth_credentials']['department_uuid']),
    )
