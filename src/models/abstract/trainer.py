from abc import ABC, abstractmethod


class ModuleTrainer(ABC):
    def __init__(self,
                 device: str,
                 cfg_path: str,
                 ):
        self._device = device
        self._config = self._load_config(cfg_path)
        self._model = self._load_model()

    @abstractmethod
    def _load_config(self, *args, **kwargs):
        pass

    @abstractmethod
    def _load_model(self, *args, **kwargs):
        pass

    @abstractmethod
    def _load_dataloader(self, *args, **kwargs):
        pass

    @abstractmethod
    def _load_optimizer(self, *args, **kwargs):
        pass

    @abstractmethod
    def train(self, *args, **kwargs):
        pass

    @abstractmethod
    def eval(self, *args, **kwargs):
        pass
