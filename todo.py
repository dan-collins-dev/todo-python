class Todo:
    def __init__(self, name, description, parent):
        
        self.name = name
        self.description = description

        # Inner function to create a simple id for each todo
        def assign_id(self, _parent):
            if len(_parent.todos) == 0:
                print("test")
                return 1
            else:
                return len(_parent.todos) + 1
                
        self.id = assign_id(self, parent)

              
    def __str__(self):
        return f"\nTodo ID: {self.id}\nTodo Name: {self.name}\nTodo Description: {self.description}\n"
    
    def __repr__(self):
        return (
            f"Todo("
            f"{repr(self.id)}, "
            f"{repr(self.name)}, "
            f"{repr(self.description)})"
        )