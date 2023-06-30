from typing import List

import model
import db
import re


def check_date_format(date):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern, date):
        return True
    else:
        return False


TITLE_LIMIT = 60
TEXT_LIMIT = 120


class LogicException(Exception):
    pass


class EventLogic:
    def __init__(self):
        self._event_db = db.EventDB()


    @staticmethod
    def _validate_note(event: model.Event):
        if event is None:
            raise LogicException("note is None")
        if event.title is None or len(event.title) > TITLE_LIMIT:
            raise LogicException(f"title length > MAX: {TITLE_LIMIT}")
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text length > MAX: {TEXT_LIMIT}")
        if not check_date_format(event.date):
            raise LogicException(f"Invalid date format. Use YYYY-MM-DD")
        event_db = db.EventDB()
        if event_db.check_date_in_db(event.date):
            raise LogicException(f"The event date already exists in the database")

    def create(self, event: model.Event) -> str:
        self._validate_note(event)
        try:
            return self._event_db.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Event]:
        try:
            return self._event_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._event_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: model.Event):
        self._validate_note(event)
        try:
            return self._event_db.update(_id, event)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._event_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")