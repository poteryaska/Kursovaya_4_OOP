from abc import ABC, abstractmethod

class Job(ABC):
    @abstractmethod
    def connect_api(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
