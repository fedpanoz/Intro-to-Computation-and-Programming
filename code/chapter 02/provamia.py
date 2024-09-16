
def two_sum(nums, target):
    hash_table = {}

    for index, value in enumerate(nums):
        if hash_table.get(target - value) is not None:
            print(value)
            return [hash_table.get(target - value), index]
        else:
            hash_table[value] = index

    return None