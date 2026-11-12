# Library Manager

A small Python program for a campus library that lends books, magazines and DVDs.
Members can borrow and return items, late fees depend on the item type, and invalid
actions raise clear errors instead of crashing.

Run it with `python3 main.py` (on Windows, `python main.py`). Needs Python 3.12+, no external packages.
The full output of the final run is in `output.txt`.

## Files

- `models.py`: the abstract `LibraryItem`, its children `Book`, `Magazine` and `DVD`, and `Member`.
- `main.py`: a demo that runs every feature.

## Reflection

**1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?**

`LibraryItem` is only a general idea of "an item". On its own it doesn't know what late fee to
charge, so it shouldn't be possible to create one. Marking `late_fee()` with `@abstractmethod`
forces every child class to write its own version. If `DVD` forgot to, Python would refuse to
create a DVD at all: `DVD(...)` raises `TypeError: Can't instantiate abstract class DVD ...`.
The mistake shows up as soon as you create the object, not later when a fee is calculated.

**2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?**

It raises `AttributeError: 'Magazine' object has no attribute '__available'`. Inside a class,
Python renames an attribute with two leading underscores (name mangling), so `__available`
is really stored as `_LibraryItem__available`. The original name doesn't exist outside the
class. We use `is_available()` because the class should control its own data: other code
can read the value through a method but can't change it by accident, and only
`mark_borrowed()` and `mark_returned()` can change it.

**3. What is the difference between LibraryItem.total_items and self.title?**

`total_items` is a class attribute. There is one copy stored on the class, shared by every
item, which is why it counts all the items created (3 in the demo). `self.title` is an
instance attribute. Each object has its own copy, so the book's title and the DVD's title
are different values.
