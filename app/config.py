import yaml
import logging


class Config(object):
    def __new__(cls):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init()
        return it
    
    def init(self):
        # Connect to config
        try:
            with open("/run/secrets/template_config.yaml", "r") as file:
                self._yaml = yaml.safe_load(file)
                logging.info("Secret loaded successfully")
        except Exception as e:
            logging.error("{} while loading a secret".format(e))
            self._yaml = dict()

    def get_value(self, key: str) -> any:
        """Выдает значение по ключу\n
        Если ключа не существует возвращает None"""
        if key in self._yaml:
            return self._yaml[key]
        else:
            return None