import TodoFile

def new_entry():
    return(input("The format for adding an item:\
    Rating: integer\
    Lifespan: [yyyy-mm-dd]\
    Category: string\
    Description: string\
    Extra information: string\
    Solution: string (hardcoded x)\
    ******\
    Shortcuts: -r, -d, -c, -d, -e, -s\
    Default input order: Category, Description, Importance\
    Override defaults with shortcuts.\
    Enter task:"))