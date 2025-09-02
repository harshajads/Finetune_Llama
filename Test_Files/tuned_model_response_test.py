from FineTuner import *
from Level_generator import *


f = FineTuner()
l = create_level(4)
prompt = get_prompt(l)
print(prompt)

map = f.load_map_from_finetuned_model(prompt)
print(map)