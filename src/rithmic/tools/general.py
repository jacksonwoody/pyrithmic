from operator import itemgetter


def dict_destructure(input_dict, keys: list):
    missing_keys = [k for k in keys if k not in input_dict.keys()]
    if len(missing_keys) > 0:
        raise KeyError('Not all keys present')
    return itemgetter(*keys)(input_dict)
