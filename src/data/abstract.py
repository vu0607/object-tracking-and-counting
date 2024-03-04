from abc import abstractmethod
from omegaconf import OmegaConf

class DataModule:
    def __init__(self, cfg_path: str):
        self._config = self._load_config(cfg_path)

    @staticmethod
    def _load_config(cfg_path: str):
        return OmegaConf.load(cfg_path)

    @abstractmethod
    def train_iter(self, *args, **kwargs):
        pass

    @abstractmethod
    def val_iter(self, *args, **kwargs):
        pass

    @abstractmethod
    def test_iter(self, *args, **kwargs):
        pass