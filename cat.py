import json
import sys

#handle argument exceptions
if len(sys.argv) < 3:
    raise  Exception('参数数量必须大于2！')



# accept argument list
notebook_path_lst = sys.argv[1:]

cells_lst = []
target_notebook ={}

# read nootebook path list
for path in notebook_path_lst:
    with open (path) as notebook:
        notebook_str = notebook.read()
        notebook_json = json.loads(notebook_str)
        cells = notebook_json['cells']
        cells_lst += cells

notebook_path_1 = sys.argv[1]
notebook_1 = open(notebook_path_1)
notebook_1_str = notebook_1.read()
notebook_1_json = json.loads(notebook_1_str)
del notebook_1_json['cells']


target_notebook['cells'] = cells_lst
target_notebook.update(notebook_1_json)
target_str = json.dumps(target_notebook)
with open ('target_notebook.ipynb','w') as target:
    target.write(target_str)


#del nootebooks_1_json['cells']


# cat two nootebooks
#target_cells = cells_1 + cells_2


#target_notebook['cells'] = target_cells
#target_notebook.update(nootebooks_1_json)





def main():
    pass

if __name__ == '__main__':
    main()