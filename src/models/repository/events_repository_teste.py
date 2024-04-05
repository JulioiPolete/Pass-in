import pytest

from .events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()



def test_insert_event():
    event = {
        "uuid": "meu-uuid-e-nois232",
        "title": "meu title232",
        "slug": "meu-slug-aqui!232",
        "maximum_attendees": 20,
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)



def test_get_event_by_id():
    event_id = "meu-uuid-e-nois23343545456453"
    events_repository = EventsRepository()
    response = events_repository.get_eventy_by_id(event_id)
    print(response)
    print(response.title)
    