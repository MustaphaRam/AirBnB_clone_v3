#!/usr/bin/python3
"""This is the city class"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
import models
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    if storage_type == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade='all, delete, delete-orphan',
                            backref="cities")
    else:
        state_id = ''
        name = ''

    if storage_type != 'db':
        @property
        def places(self):
            """
            getter for places
            :return: list of places in that city
            """
            all_places = models.storage.all("Place")

            result = []

            for obj in all_places.values():
                if str(obj.city_id) == str(self.id):
                    result.append(obj)

            return result
