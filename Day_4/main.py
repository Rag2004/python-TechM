# Assignment on Sequences in Python

# 1. Define a sequence. What types of sequences exist in Python?
# A sequence is an ordered collection of elements.
# Types of sequences: Strings, Lists, and Tuples.

# 2. Difference between Strings, Lists, and Tuples
# - Strings: Immutable, e.g., "Hello"
# - Lists: Mutable, e.g., [1, 2, 3]
# - Tuples: Immutable, e.g., (1, 2, 3)

# 3. Indexing Example
text = "Python"
print(text[0])  # Output: 'P'
print(text[-1]) # Output: 'n'

# 4. Accessing the last character of a string
print(text[-1])  # Output: 'n'

# 5. Accessing the third element of a list
numbers = [10, 20, 30, 40, 50]
print(numbers[2])  # Output: 30

# 6. Length of list [1, [2, 3], 4]
print(len([1, [2, 3], 4]))  # Output: 3

# 7. Slicing Example
print(numbers[1:4])  # Output: [20, 30, 40]

# 8. Reverse a string using slicing
print(text[::-1])  # Output: 'nohtyP'

# 9. List concatenation and repetition
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # Output: [1, 2, 3, 4]
print([0] * 3)  # Output: [0, 0, 0]

# 10. Counting occurrences in a list
my_list = [1, 2, 2, 3, 2, 4]
print(my_list.count(2))  # Output: 3

# 11. Tuple Slicing
my_tuple = (1, 2, 3)
print(my_tuple[1:])  # Output: (2, 3)

# 12. Difference between append() and extend()
lst = [1, 2]
lst.append([3, 4])
print(lst)  # Output: [1, 2, [3, 4]]

lst = [1, 2]
lst.extend([3, 4])
print(lst)  # Output: [1, 2, 3, 4]

# 13. Splitting a sentence into words
sentence = "Learn Python, step by step!"
words = sentence.split()
print(words)  # Output: ['Learn', 'Python,', 'step', 'by', 'step!']

# 14. Joining a list into a string
words = ['Python', 'is', 'fun']
print('_'.join(words))  # Output: "Python is fun"

# 15. Finding the index of the first occurrence of 2
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.index(2))  # Output: 1

# 16. Checking if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True

# 17. Longest word length in a sentence
def longest_word_length(sentence):
    words = sentence.split()
    return max(len(word) for word in words)

print(longest_word_length("Python is amazing"))  # Output: 7

# 18. Nested list indexing
nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])  # Output: 6

# 19. Convert list of characters to a string
chars = ['H', 'e', 'l', 'l', 'o']
print(''.join(chars))  # Output: "Hello"

# 20. Removing duplicates from a list
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# 21. Sorting a list of tuples by the second element
def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_by_second_element([(1, 3), (2, 2), (3, 1)]))  # Output: [(3, 1), (2, 2), (1, 3)]

# 22. Flattening a nested list
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

print(flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]

# 23. Rotating a list to the right by k steps
def rotate_right(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]

# 24. Checking if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  # Output: True

# 25. Splitting a list into chunks
def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

print(chunk_list([1, 2, 3, 4, 5], 2))  # Output: [[1, 2], [3, 4], [5]]


#25  
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0  # Pointers for list1 and list2
    
    # Merge both lists until one is exhausted
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Add remaining elements from list1 (if any)
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Add remaining elements from list2 (if any)
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Example usage:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
