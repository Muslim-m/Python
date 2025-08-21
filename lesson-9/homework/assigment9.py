#1.Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


radius1 = Circle(
    int(input("Enter value of radius to find area and perimeter of a circle:"))
)
print("Area of a circle is", radius1.area())
print("Perimeter of a circle is", radius1.perimeter())
#2.Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
from datetime import datetime
class Person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    def find_age(self):
        today=datetime.now()
        age=today.year-self.date_of_birth.year
        return age
    def __str__(self):
        current_year=datetime.now().year
        return f"Age of {self.name} in {self.country} in {current_year} is {self.find_age()}"
info=Person("Ali","USA","1925-04-09")
print(info)
#3.Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self,num1,num2):
        return num1+num2
    def subtract(self,num1,num2):
        return num1-num2
    def mutiply(self,num1,num2):
        return num1*num2
    def divide(self,num1,num2):
        if num2==0:
            return "Error:Division by Zero"
        return num1/num2
cal=Calculator()
print("Add:",cal.add(10,5))
print("Subtract:",cal.subtract(20,10))
print("Mutiply:",cal.mutiply(10,30))
print("Divide:",cal.divide(44,8))
#4.Write a Python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like Circle, Triangle, and Square.
import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area() method ")
    def perimeter(self):
        raise  NotImplementedError("Subclass must implement perimeter() method")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4*self.side

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a+self.b+self.c
circle=Circle(5)
square=Square(20)
triangle=Triangle(3,4,5)
print("Circle -> Area:", round(circle.area(), 2), "Perimeter:", round(circle.perimeter(), 2))
print("Square -> Area:", square.area(), "Perimeter:", square.perimeter())
print("Triangle -> Area:", round(triangle.area(), 2), "Perimeter:", triangle.perimeter())
#5.Write a Python program to create a class representing a binary search tree.
# Include methods for inserting and searching for elements in the binary tree.
class Node:
    """Class representing a node in the BST"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree class"""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST"""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:  # Go to left subtree
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:  # Go to right subtree
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def search(self, key):
        """Search for a key in the BST"""
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None:
            return False
        if key == current.key:
            return True
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)


# -----------------------
# Example usage
# -----------------------
bst = BinarySearchTree()

# Insert elements
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

# Search for elements
print(bst.search(30))  # True
print(bst.search(90))  # False
#6.Write a Python program to create a class representing a stack data structure.
# Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        "Add an item to the stack"
        self.items.append(item)
    def pop(self):
        "Remove and return the top item for the stack"
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"
    def peek(self):
        "Return the top element without removing it "
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"
    def is_empty(self):
        "Check if the stack is empty"
        return len(self.items)==0
    def size(self):
        "Return the number of elements in the stack"
        return len(self.items)

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(70)

print("The top emelemt:",stack.peek())
print("Poped element:",stack.pop())
print("Stack size",stack.size())
print("Is stack empty?",stack.is_empty())
#7.Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.
# Node class: represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # store the data
        self.next = None  # pointer to the next node


# LinkedList class: represents the linked list structure
class LinkedList:
    def __init__(self):
        self.head = None  # initially empty list

    # Method to insert a node at the end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:  # if list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # traverse to the last node
                current = current.next
            current.next = new_node

    # Method to delete a node by value
    def delete(self, data):
        current = self.head

        # Case 1: List is empty
        if not current:
            print("List is empty, nothing to delete.")
            return

        # Case 2: Head node needs to be deleted
        if current.data == data:
            self.head = current.next
            current = None
            return

        # Case 3: Node to delete is in the middle or end
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        # Data not found
        if not current:
            print(f"Node with value {data} not found.")
            return

        # Unlink the node
        prev.next = current.next
        current = None

    # Method to display the linked list
    def display(self):
        if not self.head:
            print("Linked list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # end of list


# Example usage
if __name__ == "__main__":
    ll = LinkedList()

    # Insert elements
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)

    # Display list
    print("Linked List after insertion:")
    ll.display()

    # Delete an element
    ll.delete(20)
    print("\nLinked List after deleting 20:")
    ll.display()

    # Try deleting something not in the list
    ll.delete(50)
#8.Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        # Dictionary to store items: {item_name: [price, quantity]}
        self.items = {}

    # Add item to cart
    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name][1] += quantity  # increase quantity
        else:
            self.items[name] = [price, quantity]
        print(f"Added {quantity} x {name}(s) to cart.")

    # Remove item from cart
    def remove_item(self, name, quantity=1):
        if name in self.items:
            if self.items[name][1] > quantity:
                self.items[name][1] -= quantity
                print(f"Removed {quantity} x {name}(s) from cart.")
            else:
                del self.items[name]
                print(f"Removed all {name}(s) from cart.")
        else:
            print(f"{name} not found in cart.")

    # Calculate total price
    def calculate_total(self):
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total

    # Display cart contents
    def display_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("\nShopping Cart:")
            for name, (price, quantity) in self.items.items():
                print(f"{name} - ${price} x {quantity} = ${price * quantity}")
            print(f"Total: ${self.calculate_total()}")


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()

    cart.add_item("Apple", 2, 3)  # 3 apples at $2 each
    cart.add_item("Banana", 1, 5)  # 5 bananas at $1 each
    cart.add_item("Milk", 4, 2)  # 2 milk bottles at $4 each

    cart.display_cart()

    cart.remove_item("Banana", 2)  # remove 2 bananas
    cart.display_cart()

    print("\nFinal Total:", cart.calculate_total())
#9Write a Python program to create a class representing a stack data structure.
# Include methods for pushing, popping, and displaying elements.
class Stack:
    def __init__(self):
        self.stack = []  # internal list to store elements

    # Push element onto stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto stack.")

    # Pop element from stack
    def pop(self):
        if not self.is_empty():
            removed_item = self.stack.pop()
            print(f"Popped {removed_item} from stack.")
            return removed_item
        else:
            print("Stack is empty. Cannot pop.")

    # Display stack elements
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top -> bottom):")
            for item in reversed(self.stack):
                print(item)

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0


# Example usage
if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    s.display()

    s.pop()
    s.display()

    s.pop()
    s.pop()
    s.pop()  # Trying to pop from empty stack

#10. Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        self.queue = []  # internal list to store elements

    # Add element to the end (enqueue)
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item}.")

    # Remove element from the front (dequeue)
    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue.pop(0)
            print(f"Dequeued {removed_item}.")
            return removed_item
        else:
            print("Queue is empty. Cannot dequeue.")

    # Display queue elements
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements (front -> rear):")
            for item in self.queue:
                print(item, end=" ")
            print()

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0


# Example usage
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.display()

    q.dequeue()
    q.display()

    q.dequeue()
    q.dequeue()
    q.dequeue()  # Trying to dequeue from empty queue
#11.Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # {account_number: {"name": str, "balance": float}}

    # Create new account
    def create_account(self, account_number, customer_name, balance=0):
        if account_number in self.accounts:
            print(f"Account {account_number} already exists.")
        else:
            self.accounts[account_number] = {"name": customer_name, "balance": balance}
            print(f"Account created for {customer_name} with account number {account_number}.")

    # Deposit money
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print(f"Deposited ${amount} to account {account_number}.")
        else:
            print(f"Account {account_number} not found.")

    # Withdraw money
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f"Withdrew ${amount} from account {account_number}.")
            else:
                print("Insufficient funds.")
        else:
            print(f"Account {account_number} not found.")

    # Check balance
    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]["balance"]
            print(f"Account {account_number} balance: ${balance}")
            return balance
        else:
            print(f"Account {account_number} not found.")

    # Display all accounts
    def display_accounts(self):
        if not self.accounts:
            print("No accounts in the bank.")
        else:
            print(f"\n{self.name} - Customer Accounts:")
            for acc_num, info in self.accounts.items():
                print(f"Account: {acc_num}, Name: {info['name']}, Balance: ${info['balance']}")


# Example usage
if __name__ == "__main__":
    bank = Bank("OpenAI Bank")

    bank.create_account(101, "Alice", 500)
    bank.create_account(102, "Bob", 1000)

    bank.deposit(101, 200)
    bank.withdraw(102, 300)

    bank.check_balance(101)
    bank.check_balance(102)

    bank.display_accounts()






