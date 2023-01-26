def count_by_twos(x):
    # Count by 2's
    result = [y for y in range(2, x+1, 2)]
    return result
print(count_by_twos(30))

def product_pairs_divisible_by_5(list1, list2):
    # Finding every pair of integers from list1 and list2 whose product is divisible by 5;
    # if no pairs, return "None Found"

    # NOT USING LIST COMPREHENSION
    result1 = []
    for x in list1:
        for y in list2:
            if (x * y) % 5 == 0:
                result1.append((x, y))
    print("None Found" if len(result1)==0 else result1, "Not using list comprehension")

    # USING LIST COMPREHENSION

    result2 = [ (x, y) for x in list1 for y in list2 if (x * y) % 5 == 0 ]
    print("None Found" if len(result2)==0 else result2, "Using list comprehension")

    return(result2, "Returning the list")
print(product_pairs_divisible_by_5([1,2,3], [5,6,7]))
# ([(1, 5), (2, 5), (3, 5)]
print(product_pairs_divisible_by_5([1,1,4], [4,6,7]))
# none found 



