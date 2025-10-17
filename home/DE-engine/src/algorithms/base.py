import abc
import json

class AlgorithmInterface(metaclass=abc.ABCMeta):
    def __init__(self, parameters, infrastructure):
        """
        parameters: JSON string with algorithm input parameters (metrics)
        infrastructure: JSON string with optional infrastructure info
        """
        self.__parameters = json.loads(parameters)
        self.__infrastructure = json.loads(infrastructure)

    def get_input_parameters(self):
        return self.__parameters

    def get_infrastructure_parameters(self):
        return self.__infrastructure

    @abc.abstractmethod
    def launch(self):
        """
        Execute the algorithm logic.
        Must return a dict with results.
        """
        pass
