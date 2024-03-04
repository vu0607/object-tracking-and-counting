from abc import ABC, abstractmethod

class ModulePredictor(ABC):
    def __init__(self,
                 device: str,
                 cfg_path: str,
                 save_log: bool = False,
                 has_postprocess: bool = False,
                 has_preprocess: bool = False,
                 ):
        self._device = device
        self._config = self._load_config(cfg_path)
        self._model = self._load_model()
        self._has_postprocess = has_postprocess
        self._has_preprocess = has_preprocess
        self._save_log = save_log

    @abstractmethod
    def _load_config(self, *args, **kwargs):
        pass

    @abstractmethod
    def _load_model(self, *args, **kwargs):
        pass

    @abstractmethod
    def _single_predict(self, single_input):
        pass

    @abstractmethod
    def _batch_predict(self, batch_input, batch_size: int):
        pass

    @abstractmethod
    def _post_processing(self, *args, **kwargs):
        pass

    @abstractmethod
    def _pre_processing(self, *args, **kwargs):
        pass