class Todo:
    def __init__(self, name, description):
        self.name = name
        self.description = description
              
    def __str__(self):
        return f"Todo Name: {self.name}\nTodo Description: {self.description}\n"
    
    def __repr__(self):
        return (
            f"Todo("
            f"{repr(self.name)}, "
            f"{repr(self.description)})"
        )