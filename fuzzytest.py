from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print(fuzz.token_set_ratio('คาร์เนชั่น ครีมเทียมข้นหวาน 388 ก.', 'คาร์เนชัน ครีมเทียมข้นหวานชนิดพร่องไขมัน 388กรัม'))