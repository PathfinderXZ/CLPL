from abc import ABC

class _Registry(ABC):
    @classmethod
    def registry(cls):
        return cls._registry

    @classmethod
    def re_lookup_registry(cls):
        if cls._re_registry:
            return cls._re_registry
        else:
            return cls._registry