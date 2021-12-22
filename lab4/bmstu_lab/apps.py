from dataclasses import dataclass
from typing import Optional

from django.apps import AppConfig


class BmstuLabConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bmstu_lab'


@dataclass
class CarModel:
    photo: str


@dataclass
class CarMark:
    name: str
    models: list[CarModel]


class Database:
    _Car_MARKS = {
        'Audi': CarMark(
            name='Audi',
            models=[
                CarModel(
                    photo='Audi/1.png',
                ),
                CarModel(
                    photo='Audi/2.png',
                ),
                CarModel(
                    photo='Audi/3.png',
                ),
            ]
        ),
        'Bugatti': CarMark(
            name='Bugatti',
            models=[
                CarModel(
                    photo='Bugatti/1.png',
                ),
                CarModel(
                    photo='Bugatti/2.png',
                ),
                CarModel(
                    photo='Bugatti/3.png',
                ),
            ]
        ),
        'Dodge': CarMark(
            name='Dodge',
            models=[
                CarModel(
                    photo='Dodge/1.png',
                ),
                CarModel(
                    photo='Dodge/2.png',
                ),
                CarModel(
                    photo='Dodge/3.png',
                ),
            ]
        ),
    }

    @classmethod
    def get_names(cls) -> list[str]:
        return [mark.name for mark in cls._Car_MARKS.values()]

    @classmethod
    def get_mark_by_name(cls, name: str) -> Optional[CarMark]:
        return cls._Car_MARKS.get(name)
