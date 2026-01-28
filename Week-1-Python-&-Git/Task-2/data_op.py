def remove_duplicates_list(data):
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def remove_duplicates_set(data):
    return list(set(data))


def sort_data(data, reverse=False, key=None):
    return sorted(data, reverse=reverse, key=key)


def find_statistics(numbers):
    if not numbers:
        return {"error": "Empty list"}
    
    return {
        "max": max(numbers),
        "min": min(numbers),
        "average": sum(numbers) / len(numbers),
        "sum": sum(numbers),
        "count": len(numbers)
    }


def merge_sorted_lists(list1, list2):
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result


def find_nth_largest(numbers, n):
    if not numbers or n <= 0 or n > len(numbers):
        return None
    
    sorted_unique = sorted(set(numbers), reverse=True)
    return sorted_unique[n - 1] if n <= len(sorted_unique) else None


def group_by_property(data, key_func):
    groups = {}
    for item in data:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups


def frequency_count(data):
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return freq


def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))


def flatten_nested_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result


def squares_of_evens(numbers):
    return [x**2 for x in numbers if x % 2 == 0]


def filter_by_length(strings, min_length):
    return [s for s in strings if len(s) >= min_length]


def create_dict_from_lists(keys, values):
    return {k: v for k, v in zip(keys, values)}


def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def demonstrate_operations():
    print("="*60)
    print("DATA MANIPULATION DEMONSTRATIONS")
    print("="*60)
    
    print("\nRemove Duplicates:")
    data_with_dups = [1, 2, 3, 2, 4, 1, 5, 3]
    print(f"Original: {data_with_dups}")
    print(f"No duplicates (ordered): {remove_duplicates_list(data_with_dups)}")
    print(f"No duplicates (set): {remove_duplicates_set(data_with_dups)}")
    
    print("\nSorting:")
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {unsorted}")
    print(f"Ascending: {sort_data(unsorted)}")
    print(f"Descending: {sort_data(unsorted, reverse=True)}")
    
    print("\nStatistics:")
    numbers = [10, 20, 30, 40, 50]
    print(f"Numbers: {numbers}")
    print(f"Stats: {find_statistics(numbers)}")
    
    print("\nMerge Sorted Lists:")
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Merged: {merge_sorted_lists(list1, list2)}")
    
    print("\nNth Largest Element:")
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Numbers: {nums}")
    print(f"2nd largest: {find_nth_largest(nums, 2)}")
    print(f"3rd largest: {find_nth_largest(nums, 3)}")
    
    print("\nFrequency Count:")
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(f"Items: {items}")
    print(f"Frequency: {frequency_count(items)}")
    
    print("\nCommon Elements:")
    set1 = [1, 2, 3, 4, 5]
    set2 = [4, 5, 6, 7, 8]
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Common: {find_common_elements(set1, set2)}")
    
    print("\nFlatten Nested List:")
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"Nested: {nested}")
    print(f"Flattened: {flatten_nested_list(nested)}")
    
    print("\nList Comprehensions:")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Numbers: {nums}")
    print(f"Squares of evens: {squares_of_evens(nums)}")
    
    strings = ["hi", "hello", "hey", "goodbye"]
    print(f"\nStrings: {strings}")
    print(f"Length >= 4: {filter_by_length(strings, 4)}")
    
    print("\nMatrix Transpose:")
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(f"Original: {matrix}")
    print(f"Transposed: {transpose_matrix(matrix)}")
    
    print("\n" + "="*60)
    print("All demonstrations completed!")
    print("="*60)


if __name__ == "__main__":
    demonstrate_operations()
