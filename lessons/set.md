# Set

| [README](../README.md) | [Queue](queue.md) | [Set](set.md) | [Binary Tree](binaryTree.md) |
| ---------------------- | ----------------- | ------------- | ---------------------------- |

## Introduction

In Python, sets are exactly like lists except for the fact that their elements are immutable which means you cannot change or mutate an element of a set once declared. However, you can add/remove elements from the set.

Another characteristic of a set is that it may include elements of different types. This means you can have a group of numbers, strings, and even tuples, all in the same set.

Not all data structures worry about the order of the data. The set data structure is an example of one for which order is not important. Sets also cannot contain any duplicate values. With the knowledge that there will be no duplicates and that the order of the values don't matter to us allows us to store the information in a set to make it very efficient to determine if data is in the set. Sets have a Big O Notaion of O(1)

## Update and Remove

We already know that sets are mutable. This means you can add/remove elements in a set.

We can use the update(x) function to add x to our set.

```python
my_set.update(value)
```

The remove(x) function removes the element x from a set. It returns a KeyError if x is not part of the set:

```python
my_set.remove(value)
```

There are a couple of other ways to remove an element(s) from a set:

-  The discard(x) method removes x from the set but doesn't raise any error if x is not present in the set.

```python
my_set.discard(value)
```

-  The pop() method removes and returns a random element from the set.

```python
my_set.pop()
```

-  The clear() method removes all elements from a set.

```python
my_set.clear()
```

## Union

The union() method returns a set that contains all items from the original set, and all items from the specified set(s).

You can specify how many sets you want, separated by commas. It does not have to be a set; it can be any iterable object. If an item is present in more than one set, the result will contain only one appearance of this item.

```python
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result) # {"e", "b", "f", "d", "a", "c"}
```

## Intersection

The intersection() method returns a set that contains the similarity between two or more sets.

Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.

```python
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result) # {"c"}
```

## Example

Here are three sets that hold a string.

```python
x = {"a", "b", "c", "d", "e"}
y = {"c", "d", "e", "f", "g"}
z = {"e", "f", "g", "h", "i"}
```

Lets find the intersection between the sets.

```python
result = x.intersection(y, z)
print(result)  # {"e"}
```

Now lets add "f" and try again

```python
x.add("f")

result = x.intersection(y, z)
print(result)  # {"e", "f"}
```

## Problem to Solve

You will write code that will take a string and find all the unique characters and add them to a set.

[Set start](../practice_problems/set_start.py)

Once you solve the problem check the solution to compare your answer.

[Set solution](../practice_problems/set_solution.py)
