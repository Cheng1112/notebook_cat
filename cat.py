import json
import sys

# accept argument list
notebook_path_lst = sys.argv[1:]

cells_lst = []
target_notebook ={}

# read nootebook path list
for path in notebook_path_lst:
    notebook = open(path)
    notebook_str = notebook.read()
    notebook_json = json.loads(notebook_str)
    cells = notebook_json['cells']
    cells_lst += cells

target_notebook['cells'] = cells_lst
 

del nootebooks_1_json['cells']


# cat two nootebooks
target_cells = cells_1 + cells_2


#target_notebook['cells'] = target_cells
target_notebook.update(nootebooks_1_json)

target_str = json.dumps(target_notebook)
target = open('target_notebook.ipynb','w')
target.write(target_str)

def main():
    pass

if __name__ == '__main__':
    main()