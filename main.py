# main.py
from models import LibraryItem, Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Monthly", 2, 42)
dvd = DVD("Inception", 3, 148)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
print("== 1. Borrowing ==")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Borrow-limit error and not-borrowed error
print("\n== 2. More error handling ==")
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: Bob's limit is 1
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.return_item(dvd)  # should fail: Alice never borrowed the DVD
except ValueError as e:
    print("Could not return:", e)

print("Alice has:", alice.borrowed_titles())
print("Bob has:", bob.borrowed_titles())

fee = alice.return_item(book, days_late=4)
print(f"Alice returned '{book.title}' 4 days late. Fee: Rs {fee}")
print("Alice has:", alice.borrowed_titles())

# 3. Polymorphism: one loop, no type checks
print("\n== 3. Polymorphism ==")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("\n== 4. Class attribute ==")
print("Total items created:", LibraryItem.total_items)

# 5. Encapsulation: the private attribute is hidden from outside the class
print("\n== 5. Encapsulation ==")
try:
    print(magazine.__available)
except AttributeError as e:
    print("Direct access failed:", e)
print("Using is_available() instead:", magazine.is_available())

# 6. Abstract class cannot be created directly
print("\n== 6. Abstract class ==")
try:
    LibraryItem("x", 1)
except TypeError as e:
    print("Could not create LibraryItem:", e)
