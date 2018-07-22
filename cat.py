import json
# read nootebooks
nootebooks_1 = open('1!!!.ipynb')
nootebooks_1_str = nootebooks_1.read()
nootebooks_1_json = json.loads(nootebooks_1_str)

print(nootebooks_1)

cells_1 = nootebooks_1_json['cells']

nootebooks_2 = open('2!!!.ipynb')
nootebooks_2_str = nootebooks_2.read()
nootebooks_2_json = json.loads(nootebooks_2_str)

print(nootebooks_2)

cells_2 = nootebooks_2_json['cells']

# cat two nootebooks
target_cells = cells_1 + cells_2

target_json = json.dumps(target_cells)
target = open('target_notebook,ipynb','w')
target.write(target_json)

