from abc import ABC, abstractmethod


class LiveFeedInterface(ABC):
    @abstractmethod
    def get_feed_of_instrument(self, correlation_id: str, mode: int, token_list: dict):
       """
         Method to get the live feed of an instrument.
       """
    pass