from todo import Todo
class App:
    def __init__(self):
        self.running = False
        self.todos = []
    
    def initialize(self):
        todo1 = Todo("Todo 1", "Todo 1 Description")
        todo2 = Todo("Todo 2", "Todo 2 Description")
        todo3 = Todo("Todo 3", "Todo 3 Description")
        todo4 = Todo("Todo 4", "Todo 4 Description")
        
        self.todos.append(todo1)
        self.todos.append(todo2)
        self.todos.append(todo3)
        self.todos.append(todo4)
        
        self.print_todos()
        
        print("===========================================================")
        print("Todo App in Python (console version) written by Dan Collins")
        print("===========================================================\n\n")
        
        print("//Todo App")
        print("What would you like to do?")
        print("1. Manage Todos")
        print("2. Quit Application")
        choice = input("Choose your option (1 or 2): ")
        
        match choice:
            case "1":
                self.run()
            
            case "2":
                print("Quitting application")
    
    def add_todo(self):
        pass
    
    def remove_todo(self):
        pass
    
    def clear_todos(self):
        self.todos.clear()
    
    def save_todos(self):
        pass
    
    def read_todos(self):
        pass
    
    def print_todos(self):
        for todo in self.todos:
            print(todo)
    
    def run(self):
        self.running = True
        if (self.running):
            self.display_main_menu()
            choice = input("Choose your option (1, 2, 3, 4, 5): ")
            
            match choice:
                case "5":
                    self.running = False
    
    def display_main_menu(self):
        print("\nWhat would you like to do?")
        print("1. Create a Todo")
        print("2. Update a Todo")
        print("3. Remove a Todo")
        print("4. List all Todos")
        print("5. Quit Application")
    
    def display_create_menu(self):
        pass