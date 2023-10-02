import enum
from typing import Callable, Union

from rithmic.tools.pyrithmic_exceptions import CallbackIdNotFoundException


class CallbackId(enum.Enum):
    LAST_TRADE = 150
    # Callback for Last Trade processed in TICKER plant, argument is a dictionary of tick data

    PERIODIC_TICK_DATA_SYNCING = 901
    # Callback for Periodic Syncing in TICKER plant, argument is a pandas DataFrame containing latest tick data

    RITHMIC_NOTIFICATIONS = 351
    # Callback to process notifications that stream from Rithmic

    EXCHANGE_NOTIFICATIONS = 352
    # Callback to process notifications that stream from the Exchange


VALID_CALLBACK_IDS = [e.value for e in CallbackId]


class CallbackManager:
    def __init__(self):
        self.callback_mapping = dict()

    def register_callback(self, callback_id: CallbackId, func: Callable):
        """
        Set a callback to be run on an async call in the interfaces

        :param callback_id: (CallbackId) valid callback id to attach func/method to
        :param func: (Callable) func/method to process callback
        :return: None
        """
        if callback_id.value not in VALID_CALLBACK_IDS:
            valid_str = ', '.join([str(i) for i in VALID_CALLBACK_IDS])
            raise CallbackIdNotFoundException(f'Callback ID {callback_id} is not found, valid ids: {valid_str}')
        self.callback_mapping[callback_id] = func

    def register_callbacks(self, callback_mapping: dict):
        """
        Convenience method to map multiple callbacks, provide dict of ID to callback func/method

        :param callback_mapping: (dict) of callbacks to set
        :return: None
        """
        for callback_id, fn in callback_mapping.items():
            self.register_callback(callback_id, fn)

    def get_callback_by_callback_id(self, callback_id: CallbackId) -> Union[Callable, None]:
        return self.callback_mapping.get(callback_id)

    def get_callback_by_template_id(self, template_id: int) -> Union[Callable, None]:
        try:
            callback_id = CallbackId(template_id)
        except ValueError as e:
            return
        return self.callback_mapping.get(callback_id)

    def callback_id_registered(self, callback_id: int) -> bool:
        return callback_id in self.callback_mapping
