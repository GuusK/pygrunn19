import time
from datetime import datetime
from typing import List, Any

from simple_farm.farm import Cow, Bull, Animal

# not supported in python3.5
# note the hints/warnings from PyCharm
name: str = 'Hello PyGrunn'
time: float = time.time()

lst1: List[int] = [1, 2, 3]
lst2: List[Any] = [1, '2', 3.0]

datetime: datetime = datetime.strptime('2019-05-10 14:45:00', '%Y-%m-%d %H:%M:%S')

bertus = Bull('Bertus')
bertha: Cow = Cow('Bertha', 38, 25)
generalist: Animal = Bull('Scott')
specialist: Bull = Animal('Sterling')
