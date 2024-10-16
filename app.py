from todo import Todo
class App:
    def __init__(self):
        self.running = False
        self.todos = []
        
    def initialize(self):
        # Testing todos
        # todo1 = Todo("Todo 1", "Todo 1 Description", self)
        # self.todos.append(todo1)
        # todo2 = Todo("Todo 2", "Todo 2 Description", self)
        # self.todos.append(todo2)
        # todo3 = Todo("Todo 3", "Todo 3 Description", self)
        # self.todos.append(todo3)

        # todo4 = Todo("Clean the dishes", "Dishes are piling up", self)
        # self.todos.append(todo4)
        # todo5 = Todo("Do Dishes", "Testing the lower case", self)
        # self.todos.append(todo5)
        # todo6 = Todo("Help neighbors", "They need help", self)
        # self.todos.append(todo6)
        
        # self.print_todos()
        
        self.display_app_menu()
        choice = input("Choose your option (1 or 2): ")
        
        match choice:
            case "1":
                self.running = True
                self.run()
            
            case "2":
                print("Quitting application")
    
    def update_todo(self, id):
        pass
    
    def remove_todo(self, id):
        pass
    
    def clear_todos(self):
        self.todos.clear()
    
    def save_todos(self):
        pass
    
    def search_todos(self):
        search_string = input("\nPlease enter your search terms: ")
        search_terms = search_string.split()
        results = []
        
        for term in search_terms:
            term = term.lower()

        for todo in self.todos:
            if term in todo.name.lower() or term in todo.description.lower() or term in str(todo.id):
                results.append(todo)
        
        print("\n====== Search Results ======")
        for result in results:
            print(result)
        print("============================")
            
    
    def print_todos(self):
        for todo in self.todos:
            print(todo)
            
    
    def run(self):
        while (self.running):
            self.display_main_menu()
            choice = input("Choose your option (1, 2, 3, 4, 5, or 6): ")
            
            match choice:
                case "1":
                    self.display_create_menu()
                    
                case "2":
                    self.find_todo()
                
                case "4":
                    self.print_todos()
                
                case "6":
                    self.running = False
    
    def display_app_menu(self):
        print("===========================================================")
        print("Todo App in Python (console version) written by Dan Collins")
        print("===========================================================\n\n")
        
        print("//Todo App")
        print("What would you like to do?")
        print("1. Manage Todos")
        print("2. Quit Application")
        
    def display_main_menu(self):
        print("\nWhat would you like to do?")
        print("1. Create a Todo")
        print("2. Update a Todo By ID")
        print("3. Search for Todo")
        print("4. Remove a Todo By ID")
        print("5. List all Todos")
        print("6. Quit Application")
    
    def display_create_menu(self):
        print("\nPlease Enter a name and description for your todo.")
        title = input("Name: ")
        desc = input("Description: ")
        self.todos.append(Todo(title, desc, self))