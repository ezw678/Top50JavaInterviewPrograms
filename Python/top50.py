import math
import calendar
from collections import Counter, deque
from .tree_node import TreeNode, root
from .list_node import ListNode, head
import re
import numpy as np


"""Write a program which will print Fibonacci series, e.g. 1 1 2 3 5 8 13 ...
up to a given number."""


def fibonacci_series(n: int) -> list[int]:
    lst = []
    fb0, fb1, fb = 0, 1, -1

    lst.append(fb1)
    while fb <= n:
        fb = fb0 + fb1
        if fb <= n:
            lst.append(fb)
        else:
            break
        fb0, fb1 = fb1, fb

    return lst


# Write a program to check if a given number is prime or not.


def is_prime(n: int):
    for i in range(n // 2, 1, -1):
        if n % i == 0:
            return False

    return True


# Write a program to check if a given String is palindrome or not


def str_palindrome(s: str) -> bool:
    return s == s[::-1]


# Write a program to check if an integer is palindrome or not


def int_palindrome_1(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


# see function reverse_number_2 below
def int_palindrome_2(n: int) -> bool:
    return reverse_number_2(n) == n


"""A number is called an Armstrong number if it is equal to the cube of its every digit. 
For example, 153 is an Armstrong number because of 153= 1+ 125+27, which is equal 
to 1^3+5^3+3^3. You need to write a program to check if the given number is 
Armstrong number or not."""


def armstrong_number(n: int) -> bool:
    temp = n
    sm = 0
    while temp > 0:
        d = temp % 10
        sm += d**3
        temp //= 10

    return n == sm


# Write a program to find the factorial of a number


def factorial(n: int) -> int:
    if n == 1:
        return 1

    return n * factorial(n - 1)


# Write a program to reverse a string


def reverse_str(s: str) -> str:
    return s[::-1]


"""Write a program to remove duplicating from an array. Keep one copy 
of the duplicated numbers."""


def remove_dups_in_list_1(nums: list[int]) -> list[int]:
    return list(set(nums))


def remove_dups_in_list_2(nums: list[int]) -> list[int]:
    counter = Counter(nums)

    return list(counter.keys())


def remove_dups_in_list_3(nums: list[int]) -> list[int]:
    lst = []
    for n in nums:
        if not n in lst:
            lst.append(n)

    return lst


# Write a program to delete duplicated numbers entirely from an array


def del_dups_in_list_1(nums: list[int]) -> list[int]:
    return [x for x in nums if nums.count(x) == 1]


def del_dups_in_list_2(nums: list[int]) -> list[int]:
    counter = Counter(nums)

    return [item[0] for item in counter.items() if item[1] == 1]


# Write a program to print a pyramid pattern


def print_pattern(n: int) -> None:
    for i in range(n):
        for j in range(n - i):
            print(" ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print()


# Write a program to find duplicated characters in a string


def find_dup_chars_in_str_1(s: str) -> list[str]:
    dct = {}
    for c in s:
        if c not in dct.keys():
            dct[c] = 1
        else:
            dct[c] = dct[c] + 1

    return list([item[0] for item in dct.items() if item[1] > 1])


def find_dup_chars_in_str_2(s: str) -> list[str]:
    counter = Counter(s)
    return list([item[0] for item in counter.items() if item[1] > 1])


# Write a program to find the square root of a number without using build-in functions


def find_sqrt(n: float) -> float:
    if n < 0.0:
        return math.nan

    precision = 0.0000000000001
    if n < precision:
        return n

    low = 0.0
    hi = n if n >= 1 else 1
    r = math.floor(n)
    for i in range(1, r):
        sq = i * i
        if sq == n:
            return i
        elif sq > n:
            low = i - 1
            hi = i
            break

    while low < hi:
        mid = (hi + low) / 2
        sq = mid**2
        dif = abs(sq - n)
        if dif <= precision:
            return mid
        elif sq > n:
            hi = mid
        elif sq < n:
            low = mid

    return math.nan


# Reverse array in place


def reverse_array_in_place(nums: list[int]):
    l, r = 0, (ln := len(nums)) - 1

    if ln <= 1:
        return nums

    while l <= r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


# Reverse words of a sentence


def reverse_words_in_sentence(sentence: str) -> str:
    words = re.split(r"\s", sentence)
    return " ".join([w[::-1] for w in words])


# Write a program to find if a year is a leap year or not


def is_leap_year(yr: int) -> bool:
    return calendar.isleap(yr)


"""Write a program to find if an integer exist in a sorted list and its 
position if yes"""


def binary_search(nums: list[int], n: int) -> int:
    nums.sort()
    low = 0
    hi = len(nums) - 1

    return bs(nums, n, low, hi)


def bs(nums: list[int], n: int, low: int, hi: int) -> int:
    if low > hi:
        return -1

    mid = (low + hi) // 2
    if nums[mid] == n:
        return mid
    elif nums[mid] > n:
        return bs(nums, n, low, mid - 1)
    elif nums[mid] < n:
        return bs(nums, n, mid + 1, hi)


"""Write a program to check if two given String is Anagram of each other. 
Your function should return true if two Strings are Anagram, false otherwise. 
A string is said to be an anagram if it contains the same characters and same 
length, but in a different order, e.g. army and Mary are anagrams. You can 
ignore cases for this problem"""


def is_anagram(s1: str, s2: str) -> bool:
    if s1.lower() == s2.lower():
        return False

    return sorted(s1.lower()) == sorted(s2.lower())


# Write a program to reverse an integer number


def reverse_number_1(n: int) -> int:
    return int(str(n)[::-1]) if n >= 0 else int(str(n * (-1))[::-1]) * (-1)


def reverse_number_2(n: int) -> int:
    negative = False
    if n < 0:
        negative = True
        n = n * -1

    negative
    temp = n
    res = 0
    while temp > 0:
        d = temp % 10
        res = res * 10 + d
        temp //= 10

    if not negative:
        return res
    else:
        return res * -1


# Write a program to find the first non-repeated character in a string


def find_first_non_repeat_char_1(s: str) -> str:
    counter = Counter(s)
    for item in counter.items():
        if item[1] == 1:
            return item[0]

    return None


def find_first_non_repeat_char_2(s: str) -> str:
    for c in s:
        if s.count(c) == 1:
            return c

    return None


# Write a program to traverse a binary tree pre-order


def pre_order_traversal_recursive(node: TreeNode, lst: list[int]) -> None:
    if node:
        lst.append(node.data)
        pre_order_traversal_recursive(node.left, lst)
        pre_order_traversal_recursive(node.right, lst)


def pre_order_traversal(node: TreeNode) -> list[int]:
    stack = deque[TreeNode]()
    stack.append(node)

    lst = []
    while stack:
        temp = stack.pop()
        lst.append(temp.data)

        # if temp.right != None:
        if temp.right:
            stack.append(temp.right)

        if temp.left:
            stack.append(temp.left)

    return lst


# Write a program to traverse a binary tree in-order


def in_order_traversal_recursive(node: TreeNode, lst: list[int]) -> None:
    if node:
        in_order_traversal_recursive(node.left, lst)
        lst.append(node.data)
        in_order_traversal_recursive(node.right, lst)


def in_order_traversal(node: TreeNode) -> list[int]:
    stack = deque[TreeNode]()
    lst = []
    temp = node
    while temp or stack:
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            temp = stack.pop()
            lst.append(temp.data)
            temp = temp.right

    return lst


# Write a program to traverse a binary tree post-order


def post_order_traversal_recursive(node: TreeNode, lst: list[int]):
    if node:
        post_order_traversal_recursive(node.left, lst)
        post_order_traversal_recursive(node.right, lst)
        lst.append(node.data)


def post_order_traversal(node: TreeNode) -> list[int]:
    stack_temp = deque[TreeNode]()
    stack = deque[TreeNode]()
    stack_temp.append(node)
    lst = []
    while stack_temp:
        temp = stack_temp.pop()
        stack.append(temp)

        if temp.left:
            stack_temp.append(temp.left)

        if temp.right:
            stack_temp.append(temp.right)

    while stack:
        temp = stack.pop()
        lst.append(temp.data)

    return lst


# Write a program to traverse a binary tree breadth first


def print_all_nodes_breadth_first(node: TreeNode) -> None:
    queue = deque[TreeNode]()
    queue.append(node)

    while queue:
        temp = queue.popleft()
        if temp:
            print(temp.data, end=" ")
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    print()


# Write a program to print out all leaf nodes


def print_all_leaf_nodes(node: TreeNode):
    if node:
        if not node.left and not node.right:
            print(node.data, end=" ")
        else:
            print_all_leaf_nodes(node.left)
            print_all_leaf_nodes(node.right)


# Write a program to sort an array of integers using a quick sort algorithm


def quicksort_1(nums: list[int], left: int, right: int) -> None:
    if left < right:
        pivot_index = partition(nums, left, right)

        quicksort_1(nums, left, pivot_index - 1)
        quicksort_1(nums, pivot_index + 1, right)


def partition(nums: list[int], left: int, right: int) -> int:
    pivot_val = nums[right]

    j = left - 1
    for i in range(left, right):
        if nums[i] < pivot_val:
            j += 1
            if j < i:
                nums[j], nums[i] = nums[i], nums[j]

    j += 1
    if j < right:
        nums[j], nums[right] = nums[right], nums[j]

    return j


def quicksort_2(nums: list[int]) -> list[int]:
    if (ln := len(nums)) <= 1:
        return nums

    pivot = nums[ln // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quicksort_2(left) + middle + quicksort_2(right)


# Write a program to implement the insertion sort algorithm.


def insertion_sort(nums: list[int]) -> None:
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
            else:
                break


# Write a program to implement the bubble sort algorithm.


def bubble_sort(nums: list[int]) -> None:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


# Write a program to implement the merge sort algorithm.


def merge_sort(nums: list[int]) -> list[int]:
    if (ln := len(nums)) <= 1:
        return nums

    mid = ln // 2
    left_arr = nums[:mid]
    right_arr = nums[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    merge(nums, left_arr, right_arr)

    return nums.copy()


def merge(nums: list[int], left_arr: list[int], right_arr: list[int]):
    ln_left = len(left_arr)
    ln_right = len(right_arr)
    l = r = k = 0
    while l < ln_left and r < ln_right:
        if left_arr[l] == right_arr[r]:
            nums[k] = left_arr[l]
            k += 1
            nums[k] = left_arr[l]
            k += 1
            l += 1
            r += 1
        elif left_arr[l] < right_arr[r]:
            nums[k] = left_arr[l]
            k += 1
            l += 1
        else:
            nums[k] = right_arr[r]
            k += 1
            r += 1

    while l < ln_left:
        nums[k] = left_arr[l]
        k += 1
        l += 1

    while r < ln_right:
        nums[k] = right_arr[r]
        k += 1
        r += 1


# Write a program to print all permutations of a given string.


def str_permutation_1(word: str, l: int, r: int, strs: list[str]):
    if l == r:
        strs.append(word)
    else:
        for i in range(l, r + 1):
            word = swap_ltrs(word, l, i)
            str_permutation_1(word, l + 1, r, strs)
            word = swap_ltrs(word, l, i)


def swap_ltrs(word: str, l: int, r: int) -> str:
    ln = len(word)
    if l not in range(0, ln) or r not in range(0, ln):
        return word

    if l == r:
        return word

    return word[:l] + word[r] + word[l + 1 : r] + word[l] + word[r + 1 :]


def str_permutation_2(word: str, temp: str, strs: list[str]):
    ln = len(word)
    if ln == 0:
        strs.append(temp)
    else:
        for i in range(ln):
            str_permutation_2(word[:i] + word[i + 1 :], temp + word[i], strs)


# Add two matrices


def matrix_addition_1(a: list[list[int]], b: list[list[int]]):
    rows_a = len(a)
    cols_a = len(a[0])

    rows_b = len(b)
    cols_b = len(b[0])

    if rows_a != rows_b or cols_a != cols_b:
        return []

    for i in range(rows_a):
        for j in range(cols_a):
            a[i][j] += b[i][j]

    return a


def matrix_addition_2(a: list[list[int]], b: list[list[int]]):
    arr1 = np.array(a)
    arr2 = np.array(b)

    if arr1.shape != arr2.shape:
        return []

    return arr1 + arr2


# Multiply two matrices


def matrix_multiplication_1(a: list[list[int]], b: list[list[int]]):
    rows_a = len(a)
    cols_a = len(a[0])

    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        return []

    nm = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(rows_b):
                nm[i][j] += a[i][k] * b[k][j]

    return nm


def matrix_multiplication_2(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    rows_a = len(a)
    cols_a = len(a[0])

    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        return []

    return np.dot(a, b)


# Reverse a linked list


def reverse_linked_list(node: ListNode) -> ListNode:
    if node == None:
        return

    temp = node
    prior = None
    cur = None
    while temp:
        cur = temp
        temp = temp.next
        cur.next = prior
        prior = cur

    return cur


def reverse_linked_list_recursive(node: ListNode) -> ListNode:
    if node == None:
        return None

    new_head = None

    if node.next == None:
        return node

    new_head = reverse_linked_list_recursive(node.next)

    node.next.next = node
    node.next = None

    return new_head


# Find the length of the linked list


def find_linked_list_length_1(node: ListNode) -> int:
    if node == None:
        return 0

    temp = node
    count = 0
    while temp:
        count += 1
        temp = temp.next

    return count


def find_linked_list_length_2(node: ListNode) -> int:
    if node == None:
        return 0

    return 1 + find_linked_list_length_2(node.next)


# Check if a linked list has a loop


def is_linked_list_cyclical(node: ListNode) -> bool:
    if node == None:
        return False

    fast_node = node
    slow_node = node
    while fast_node.next != None and fast_node.next != None:
        fast_node = fast_node.next.next
        slow_node = slow_node.next
        if fast_node == slow_node:
            return True

    return False


# Find the start of loop in a linked list


def find_start_of_loop_in_linked_list(node: ListNode) -> int:
    if node == None:
        return 0

    fast_node = node
    slow_node = node

    is_cyclical = False
    while fast_node != None and fast_node.next != None:
        fast_node = fast_node.next.next
        slow_node = slow_node.next
        if fast_node == slow_node:
            is_cyclical = True
            slow_node = node
            break

    if not is_cyclical:
        return math.nan
    else:
        while fast_node != slow_node:
            fast_node = fast_node.next
            slow_node = slow_node.next
            if fast_node == slow_node:
                return slow_node.data

    return math.nan


# Find the middle element of a linked list


def find_middle_element_of_linked_list(node: ListNode) -> int:
    if node == None:
        return math.nan

    fast_node = node
    slow_node = node

    while True:
        if fast_node.next == None:
            return slow_node.data

        if fast_node.next.next == None:
            return slow_node.next.data

        fast_node = fast_node.next.next
        slow_node = slow_node.next

    return math.nan


# Find the 3rd element from the tail linked list


def find_3rd_elem_from_tail_of_linked_list(node: ListNode) -> int:
    if node == None or node.next == None or node.next.next == None:
        return -1

    fast_node = node.next.next
    slow_node = node

    while fast_node.next != None:
        fast_node = fast_node.next
        slow_node = slow_node.next

    return slow_node.data


# Convert a linked list to a binary tree


def convert_linked_list_to_binary_tree(node: ListNode) -> TreeNode:
    if node == None:
        return None

    temp = node
    root = TreeNode(temp.data)
    queue = deque[TreeNode]()
    queue.append(root)

    temp = temp.next
    while queue:
        parent = queue.popleft()
        if temp:
            left = TreeNode(temp.data)
            parent.add_left(left)
            queue.append(left)
            temp = temp.next

        if temp:
            right = TreeNode(temp.data)
            parent.add_right(right)
            queue.append(right)
            temp = temp.next

    return root


# Sort a linked list


def sort_linked_list(node: ListNode) -> None:
    if node == None:
        return

    nums = []
    while node:
        nums.append(node.data)
        node = node.next

    nums.sort()
    head = ListNode()
    cur = ListNode()
    for k, v in enumerate(nums):
        temp = ListNode(v)
        if k == 0:
            head = temp
            cur = head
        else:
            cur.next = temp
            cur = cur.next

    return head


# Check if two string rotation of each other


def check_str_rotation(s1: str, s2: str) -> bool:
    return s2 in s1 * 2 if len(s1) == len(s2) else False


def main():
    pass


if __name__ == "__main__":
    main()
