from abc import ABC, abstractmethod
from teacher.items import TeachingItem


class PlanningContext(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def update(self, queried_item: TeachingItem, answer):
        pass
    
    
    
class EmptyPlanningContext(PlanningContext):
    def __init__(self):
        pass
    
    def update(self, queried_item: TeachingItem, answer):
    def update(self, queried_item: TeachingItem, answer, time: int):
        pass
    

class FixedHorizonContext(PlanningContext):    
    def __init__(self, horizon: int):
        assert isinstance(horizon, int), "horizon must be an integer"
        self.horizon = horizon
    
    def update(self, queried_item: TeachingItem, answer):
        self.horizon -= 1    def update(self, queried_item: TeachingItem, answer, time: int):
        self.horizon -= 1
