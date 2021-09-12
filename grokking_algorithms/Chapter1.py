def binary_search(source: list, search_key):
    sorted_source = sorted(source)
    low = 0
    high = len(sorted_source)-1
    search_count = 1
    while low <= high:
        mid = int((low+high)/2)
        print(f'Search count: {search_count}. Low: {low}, High: {high}, Mid: {mid}')
        
        guess = sorted_source[mid]
        if guess == search_key:
            return mid
        elif guess > search_key:
            high = mid-1
        else:
            low = mid + 1
        search_count += 1
    return None


if __name__ == '__main__':
    binary_search(list(range(129)), 222)