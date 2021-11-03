import json

def delete(d, value, target1, target2):
    #This function deletes a node/edge and moves the subtree on the upper level
    if value==target1 or value==target2:
        d=d[value]
    return d

def search_and_delete(d, target1,target2):
    #This function explores the tree of nested dicts and lists looking for the nodes/edges and deletes them.
    #Tree is traversed in depth-first order
    if isinstance(d,str):
        #If d is a string, then it's a leaf of the tree
        return d
    if isinstance(d,list):
        #List is traversed in order to explore the tree. No delete func is called since a list has no keys to delete
        for element in d:
            i=d.index(element)
            element=search_and_delete(element, target1 ,target2)
            d[i]=element
    elif isinstance(d, dict):
        #Dict is traversed in order to explore the tree, then a delete function is called.
        for key in d.keys():
            d[key]=search_and_delete(d[key], target1, target2)
            d=delete(d, key, target1, target2)
    return d

if __name__=="__main__":
    while(True):
        print("Please insert the name of the file to be parsed:")
        input_filename = input()
        if not input_filename.endswith(".json"):
            print(f"{input_filename} is not a .json file")
            continue
        try:
            fpin = open(input_filename, "r", encoding="utf-8")
        except:
            print(f"Error while opening {input_filename}")
        else:
            break
    print(f"The file {input_filename} is accepted as a valid input file")
    basename=input_filename.split(".")[0]
    output_filename = basename + "_parsed.json"
    d=json.load(fpin)                                                        #json -> dict
    d=search_and_delete(d, "node", "edges")

    #the following lines adapt the output to the structure in the output file provided for comparison
    if "data" in d.keys():
        d=d["data"][basename]

    fpout = open(output_filename, "w", encoding="utf-8")
    fpout.write(json.dumps(d))
    print(f"The parsed file ({output_filename}) is completed")
