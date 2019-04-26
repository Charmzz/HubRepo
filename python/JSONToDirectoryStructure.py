import os

def Create_FSObject(name, type, refPath):
    """If passed a folder-type calls mkdir if passed file-type calls """
    if type == "folder":
        try:
            os.mkdir(targ_directory+refPath)
            print("Created Directory:\t"+targ_directory+refPath)
        except:
            None
    elif type == "file":
        try:
            print("Created File: \t\t"+targ_directory+refPath)
            fil = open(targ_directory+refPath,"w+")
            fil.close()
        except:
            None

def Parse_JSON(text,refPath=""):
    """This function accepts a File System directory & file organization as a
    JSON format input and creates that directory structure at the $PWD or at 
    an optional PATH"""
    if isinstance(text, dict):
        recipe_data = text
    else:
        recipe_data = json.load(text)
    refPath = refPath + '/' + recipe_data['name']
    Create_FSObject(recipe_data['name'],recipe_data['type'],refPath)
    for member, data in recipe_data.items():
        if "children" in member:
            for key in data:
                Parse_JSON(key,refPath)
    return None

if __name__ == "__main__":
    import json
    import sys

    try:
        targ_directory = sys.argv[1]
    except IndexError:
        targ_directory = "."

    try:
        recipe = sys.argv[2]
    except IndexError:
#       recipe = tkFSDialog.openDialog("file")[0]
        print("JSON input file path required")
    print (targ_directory)
    print (recipe)

    with open (recipe,"r") as text:
        Parse_JSON(text)