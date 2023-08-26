"""Defines type of car and last_service and 
determines if car needs service according to only date """
from abc import ABC, abstractmethod


class Car(ABC):
    """defines car model and last service date"""
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        """gives status of car needing service""" 
