def max_version(list):
    if list == []:
        return list
    return max(list, key=lambda x: x.wts)
