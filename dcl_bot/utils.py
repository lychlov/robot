def parse_tuple(items):
    result = ''
    if items:
        for item in items:
            for word in item:
                result = result + str(word) + '|'
            result = result[:-1] + '\n'
        return result
    else:
        return '无数据'
