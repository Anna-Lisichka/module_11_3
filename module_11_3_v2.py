import inspect

def introspection_info(obj):
    return {'type': obj.__class__.__name__, 'attributes': [i for i in dir(obj) if not callable(getattr(obj, i))],
            'methods': [i for i in dir(obj) if callable(getattr(obj, i))],
            'module':introspection_info.__module__}



if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)

