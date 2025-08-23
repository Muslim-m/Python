#1.Define Task Class:
#Create a Task class with attributes such as task title, description, due date, and status.
#Define Task Class:
#Create a Task class with attributes such as task title, description, due date, and status.
class Task:
    def __init__(self,title,description,due_data,status="Pending"):
        self.title=title
        self.description=description
        self.due_data=due_data
        self.status=status
    def mark_completed(self):
        self.status="Completed"
    def update_description(self, new_description):
        self.description=new_description
    def __str__(self):
        return f"Title:{self.title}, Status:{self.status} ,Due:{self.due_data}, Description:{self.description}"
task1=Task("Python homework","Finish assigment!","2025-08-30")
task2=Task("Gym","Push yourself","2025-08-25")
print(task1)
print(task2)
task1.mark_completed()
print(task1)
#2.Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks

class ToDolist:
    def __init__(self):
        self.tasks=[]
    def add_task(self,task):
        self.tasks.append([task,False])

    def mark_task(self,index):
        if 0<=index-1<len(self.tasks):
            self.tasks[index-1][1]=True

    def all_task(self):
        for task in self.tasks:
            if task[1]:
                print(task[0],"-Done")
            else:
                print(task[0],"-Not Done")
    def incompleted_task(self):
        for task in self.tasks:
            if not task[1]:
                print(task[0],"-Not Done")

p1=ToDolist()
p1.add_task("Do homework")
p1.add_task("Wash your dishes")
p1.add_task("Keep tidy your your bedroom")
p1.add_task("Watch Python videos in Youtube")
print(p1.tasks)
p1.mark_task(1)
p1.mark_task(2)
print(p1.tasks)
print("All tasks")
p1.all_task()
print("All incomplete tasks")
p1.incompleted_task()

#4Create Main Program:
# Develop a simple CLI to interact with the ToDoList.
# Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.

class ToDoList:
    def __init__(self):
        # This will store tasks as [task_name, completed_status]
        # Example: ["Do homework", False]
        self.tasks = []

    def add_task(self, task):
        # Add a new task with status "not completed" (False)
        self.tasks.append([task, False])

    def mark_complete(self, index):
        # Mark a task as complete using its index in the list
        if 0 <= index < len(self.tasks):  # check if index is valid
            self.tasks[index][1] = True

    def list_all(self):
        # Show all tasks with their status
        for task in self.tasks:
            if task[1]:  # if completed
                print(task[0], "- Done")
            else:  # if not completed
                print(task[0], "- Not Done")

    def list_incomplete(self):
        # Show only the tasks that are not completed
        for task in self.tasks:
            if not task[1]:
                print(task[0], "- Not Done")


def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
            print("Task added!")

        elif choice == "2":
            todo.list_all()
            if todo.tasks:  # only ask if there are tasks
                try:
                    index = int(input("Enter task number: "))
                    todo.mark_complete(index)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "3":
            print("\nAll Tasks:")
            todo.list_all()

        elif choice == "4":
            print("\nIncomplete Tasks:")
            todo.list_incomplete()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

#5 Assuming your ToDoList class is already defined
# Create a ToDoList instance
my_todo = ToDoList()

# ---------------------------
# Test 1: Add Tasks
# ---------------------------
my_todo.add_task("Do homework")
my_todo.add_task("Clean room")
my_todo.add_task("Read a book")

print("All tasks after adding:")
my_todo.list_all()
# Expected:
# 0. Do homework - Not Done
# 1. Clean room - Not Done
# 2. Read a book - Not Done

# ---------------------------
# Test 2: Mark Task as Complete
# ---------------------------
my_todo.mark_complete(0)  # Mark "Do homework" as done
my_todo.mark_complete(2)  # Mark "Read a book" as done

print("\nAll tasks after marking some complete:")
my_todo.list_all()
# Expected:
# 0. Do homework - Done
# 1. Clean room - Not Done
# 2. Read a book - Done

# ---------------------------
# Test 3: List Only Incomplete Tasks
# ---------------------------
print("\nIncomplete tasks:")
my_todo.list_incomplete()
# Expected:
# 1. Clean room - Not Done

# ---------------------------
# Test 4: Invalid Mark Complete
# ---------------------------
my_todo.mark_complete(5)  # Index out of range
# Expected: "Invalid task number!"

                                        #Homework 2. Simple Blog System
#1.Define Post Class:
#Create a Post class with attributes like title, content, and author.
class Post:
    def __init__(self,title,content,author):
        self.title=title
        self.content=content
        self.author=author
    def display_post(self):
        return f"Title:{self.title}\n Author:{self.author}\n Content:{self.content}"
p1=Post("My First Blog","This is the content of my first blog","Abrorbek")
print(p1.display_post())

# 2.Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# Define Blog class (manages many posts)
class Blog:
    def __init__(self):
        self.posts = []  # empty list to hold Post objects

    def add_post(self, post):
        # add new post into blog
        self.posts.append(post)

    def list_all_posts(self):
        # print every post stored in blog
        for item in self.posts:
            print(f"Title: {item.title}\nAuthor: {item.author}\nContent: {item.content}\n")

    def display_posts_by_author(self, author_name):
        # print only posts written by specific author
        found = False
        for post in self.posts:
            if post.author == author_name:
                print(f"Title: {post.title}\nAuthor: {post.author}\nContent: {post.content}\n")
                found = True
        if not found:
            print(f"No posts found by author '{author_name}'.")


# ---------------- Example Usage ----------------
l = Blog()

# Create Post objects
p1 = Post("Just choose Maab", "Power BI", "Sherzod Ibragimov")
p2 = Post("Find job by MAAB", "SQL", "Abrorbek")

# Add posts to the blog
l.add_post(p1)
l.add_post(p2)

print(" All posts in the blog:")
l.list_all_posts()

print("Posts by 'Muslimbek':")
l.display_posts_by_author("Muslimbek")

print(" Posts by 'Abrorbek':")
l.display_posts_by_author("Abrorbek")







# 3.Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("\n📌 No posts available yet.\n")
        else:
            for i, post in enumerate(self.posts, start=1):
                print(f"\nPost #{i}")
                print(f"Title: {post.title}")
                print(f"Author: {post.author}")
                print(f"Content: {post.content}\n")

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(f"\nTitle: {post.title}")
                print(f"Author: {post.author}")
                print(f"Content: {post.content}\n")
                found = True
        if not found:
            print(f"\n❌ No posts found by author '{author_name}'.\n")
l = Blog()

# Create Post objects
p1 = Post("Just choose Maab", "Power BI", "Sherzod Ibragimov")
p2 = Post("Find job by MAAB", "SQL", "Abrorbek")

# Add posts to the blog
l.add_post(p1)
l.add_post(p2)

print("📌 All posts in the blog:")
l.list_all_posts()

print("📌 Posts by 'Muslimbek':")
l.display_posts_by_author("Muslimbek")

print("📌 Posts by 'Abrorbek':")
l.display_posts_by_author("Abrorbek")

def main():
    blog = Blog()

    while True:
        print("\n=== Blog System Menu ===")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("\nEnter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("\n✅ Post added successfully!\n")

        elif choice == "2":
            print("\n📌 All Posts:")
            blog.list_all_posts()

        elif choice == "3":
            author_name = input("\nEnter author name: ")
            print(f"\n📌 Posts by {author_name}:")
            blog.display_posts_by_author(author_name)

        elif choice == "4":
            print("\n👋 Exiting Blog System. Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 4.\n")


# Run the program
if __name__ == "__main__":
    main()


# 4.Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.

# ---------------- Blog System ---------------- #

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class Blog:
    def __init__(self):
        self.posts = []  # will store Post objects

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("\n📌 No posts available yet.\n")
        else:
            for i, post in enumerate(self.posts, start=1):
                print(f"\nPost #{i}")
                print(f"Title: {post.title}")
                print(f"Author: {post.author}")
                print(f"Content: {post.content}\n")

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(f"\nTitle: {post.title}")
                print(f"Author: {post.author}")
                print(f"Content: {post.content}\n")
                found = True
        if not found:
            print(f"\n❌ No posts found by author '{author_name}'.\n")

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"\n🗑️ Post '{title}' deleted successfully!\n")
                return
        print(f"\n❌ No post found with title '{title}'.\n")

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                print(f"\nEditing Post: {post.title}")
                new_title = input("Enter new title (leave blank to keep current): ")
                new_content = input("Enter new content (leave blank to keep current): ")
                new_author = input("Enter new author (leave blank to keep current): ")

                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                if new_author:
                    post.author = new_author

                print("\n✏️ Post updated successfully!\n")
                return
        print(f"\n❌ No post found with title '{title}'.\n")

    def display_latest_posts(self, n=3):
        if not self.posts:
            print("\n📌 No posts available yet.\n")
        else:
            print(f"\n📌 Latest {n} Posts:\n")
            for post in self.posts[-n:][::-1]:  # take last n, reverse for newest first
                print(f"Title: {post.title}")
                print(f"Author: {post.author}")
                print(f"Content: {post.content}\n")


# ---------------- CLI Main Program ---------------- #

def main():
    blog = Blog()

    while True:
        print("\n=== Blog System Menu ===")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("\nEnter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("\n✅ Post added successfully!\n")

        elif choice == "2":
            print("\n📌 All Posts:")
            blog.list_all_posts()

        elif choice == "3":
            author_name = input("\nEnter author name: ")
            print(f"\n📌 Posts by {author_name}:")
            blog.display_posts_by_author(author_name)

        elif choice == "4":
            title = input("\nEnter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("\nEnter the title of the post to edit: ")
            blog.edit_post(title)

        elif choice == "6":
            n = input("\nHow many latest posts do you want to see? (default 3): ")
            n = int(n) if n.strip().isdigit() else 3
            blog.display_latest_posts(n)

        elif choice == "7":
            print("\n👋 Exiting Blog System. Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 7.\n")


# Run the program
if __name__ == "__main__":
    main()

#5.Test the Application:
# Create instances of posts and test the functionality of your Blog system.

    blog = Blog()

    # Create some posts
    p1 = Post("Python Basics", "Python is easy to learn.", "Alice")
    p2 = Post("OOP in Python", "Classes and objects explained.", "Bob")
    p3 = Post("Advanced Python", "Decorators and generators.", "Alice")
    p4 = Post("Data Science", "Pandas and NumPy are powerful.", "Charlie")

    # Add posts to the blog
    blog.add_post(p1)
    blog.add_post(p2)
    blog.add_post(p3)
    blog.add_post(p4)

    # 1. List all posts
    print("=== Test 1: List All Posts ===")
    blog.list_all_posts()

    # 2. Display posts by Alice
    print("=== Test 2: Display Posts by Alice ===")
    blog.display_posts_by_author("Alice")

    # 3. Edit Bob's post
    print("=== Test 3: Edit Post 'OOP in Python' ===")
    # Simulate editing (instead of input, we directly update attributes here)
    p2.title = "OOP in Python - Updated"
    p2.content = "Updated content about OOP in Python."
    print("✅ Post edited.\n")
    blog.list_all_posts()

    # 4. Delete a post (Charlie’s Data Science post)
    print("=== Test 4: Delete 'Data Science' Post ===")
    blog.delete_post("Data Science")
    blog.list_all_posts()

    # 5. Display latest 2 posts
    print("=== Test 5: Display Latest 2 Posts ===")
    blog.display_latest_posts(2)


                                #Homework 3. Simple Banking System
 #1.Define Account Class:
# Create an Account class with attributes like account number, account holder name, and balance.

class Account:
    def __init__(self,number, account_holder_name,balance):
        self.number=number
        self.name=account_holder_name
        self.balance=balance
    def display(self):
        print(f"Account Number: {self.number}")
        print(f"Holder Name: {self.name}")
        print(f"Balance: {self.balance}")
p1=Account(101,'Muslimbek',1_000_000)
p2=Account(103,'Abrorbek',7_000_000)
p1.display()
p2.display()

#2.Define Bank Class:
# Create a Bank class that manages a list of accounts.
# Include methods to add an account, check balance, deposit money, and withdraw money.
# Account Class
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def display_account(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance}")


# Bank Class
class Bank:
    def __init__(self):
        self.accounts = []  # list to hold all Account objects

    def add_account(self, account):
        self.accounts.append(account)
        print(f"✅ Account added for {account.holder_name} (#{account.account_number})")

    def find_account(self, account_number):
        # helper method to search account by number
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def check_balance(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print(f"💰 Balance for {acc.holder_name} (#{acc.account_number}): {acc.balance}")
        else:
            print("❌ Account not found!")

    def deposit(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.balance += amount
            print(f"✅ Deposited {amount}. New balance: {acc.balance}")
        else:
            print("❌ Account not found!")

    def withdraw(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            if acc.balance >= amount:
                acc.balance -= amount
                print(f"✅ Withdrawn {amount}. New balance: {acc.balance}")
            else:
                print("⚠️ Insufficient balance!")
        else:
            print("❌ Account not found!")

#3. Create Main Program:
# Develop a CLI to interact with the Banking system.
# Include options to add accounts, check balance, deposit money, and withdraw money.
# ---------------- Account Class ---------------- #
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def display_account(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance}")


# ---------------- Bank Class ---------------- #
class Bank:
    def __init__(self):
        self.accounts = []  # list to hold all accounts

    def add_account(self, account):
        self.accounts.append(account)
        print(f"✅ Account added for {account.holder_name} (#{account.account_number})")

    def find_account(self, account_number):
        # search for account by account number
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def check_balance(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print(f"💰 Balance for {acc.holder_name} (#{acc.account_number}): {acc.balance}")
        else:
            print("❌ Account not found!")

    def deposit(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.balance += amount
            print(f"✅ Deposited {amount}. New balance: {acc.balance}")
        else:
            print("❌ Account not found!")

    def withdraw(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            if acc.balance >= amount:
                acc.balance -= amount
                print(f"✅ Withdrawn {amount}. New balance: {acc.balance}")
            else:
                print("⚠️ Insufficient balance!")
        else:
            print("❌ Account not found!")


# ---------------- CLI Main Program ---------------- #
def main():
    bank = Bank()

    while True:
        print("\n=== Banking System Menu ===")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            acc_number = int(input("Enter account number: "))
            holder = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            account = Account(acc_number, holder, balance)
            bank.add_account(account)

        elif choice == "2":
            acc_number = int(input("Enter account number: "))
            bank.check_balance(acc_number)

        elif choice == "3":
            acc_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(acc_number, amount)

        elif choice == "4":
            acc_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(acc_number, amount)

        elif choice == "5":
            print("👋 Exiting Banking System. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()
#4.Enhance Banking System:
# Add functionality to transfer money between accounts, display account details, and handle account overdrafts.

# ---------------- Account Class ---------------- #
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def display_account(self):
        print("\n📄 Account Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name:   {self.holder_name}")
        print(f"Balance:       {self.balance}")


# ---------------- Bank Class ---------------- #
class Bank:
    def __init__(self):
        self.accounts = []  # list of accounts

    def add_account(self, account):
        self.accounts.append(account)
        print(f"✅ Account added for {account.holder_name} (#{account.account_number})")

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def check_balance(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print(f"💰 Balance for {acc.holder_name} (#{acc.account_number}): {acc.balance}")
        else:
            print("❌ Account not found!")

    def deposit(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.balance += amount
            print(f"✅ Deposited {amount}. New balance: {acc.balance}")
        else:
            print("❌ Account not found!")

    def withdraw(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            if acc.balance >= amount:
                acc.balance -= amount
                print(f"✅ Withdrawn {amount}. New balance: {acc.balance}")
            else:
                print("⚠️ Insufficient balance! Overdraft not allowed.")
        else:
            print("❌ Account not found!")

    def transfer(self, from_acc_num, to_acc_num, amount):
        sender = self.find_account(from_acc_num)
        receiver = self.find_account(to_acc_num)

        if sender and receiver:
            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                print(f"✅ Transferred {amount} from {sender.holder_name} → {receiver.holder_name}")
                print(f"   New Balance - {sender.holder_name}: {sender.balance}, {receiver.holder_name}: {receiver.balance}")
            else:
                print("⚠️ Transfer failed: Insufficient balance for transfer!")
        else:
            print("❌ One or both accounts not found!")

    def display_account_details(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            acc.display_account()
        else:
            print("❌ Account not found!")


# ---------------- CLI Main Program ---------------- #
def main():
    bank = Bank()

    while True:
        print("\n=== Banking System Menu ===")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            acc_number = int(input("Enter account number: "))
            holder = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            account = Account(acc_number, holder, balance)
            bank.add_account(account)

        elif choice == "2":
            acc_number = int(input("Enter account number: "))
            bank.check_balance(acc_number)

        elif choice == "3":
            acc_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(acc_number, amount)

        elif choice == "4":
            acc_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(acc_number, amount)

        elif choice == "5":
            from_acc = int(input("Enter sender account number: "))
            to_acc = int(input("Enter receiver account number: "))
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == "6":
            acc_number = int(input("Enter account number: "))
            bank.display_account_details(acc_number)

        elif choice == "7":
            print("👋 Exiting Banking System. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 7.")


# Run the program
if __name__ == "__main__":
    main()

#5.Test the Application:
# Create instances of accounts and test the functionality of your Banking system.


bank = Bank()

# Create some accounts
acc1 = Account(101, "Alice", 5000)
acc2 = Account(102, "Bob", 3000)
acc3 = Account(103, "Charlie", 1000)

# Add accounts to bank
bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)

print("\n--- Initial Account Details ---")
bank.display_account_details(101)
bank.display_account_details(102)
bank.display_account_details(103)

# Deposit money
print("\n--- Deposit Test ---")
bank.deposit(101, 2000)   # Alice +2000
bank.check_balance(101)

# Withdraw money
print("\n--- Withdraw Test ---")
bank.withdraw(102, 500)   # Bob -500
bank.check_balance(102)

# Transfer money
print("\n--- Transfer Test ---")
bank.transfer(101, 103, 1500)  # Alice → Charlie
bank.check_balance(101)
bank.check_balance(103)

# Overdraft test
print("\n--- Overdraft Test ---")
bank.withdraw(103, 5000)  # Charlie doesn't have enough

# Display final account details
print("\n--- Final Account Details ---")
bank.display_account_details(101)
bank.display_account_details(102)
bank.display_account_details(103)

