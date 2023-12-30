def parse(query: str) -> dict:
    if '?' not in query:
        return {}
    else:
        quepar = query.split('?')[1]
        if not quepar:
            return {}
        else:
            quepar = quepar.split('&')
            result = {}
            for param in quepar:
                key_value = param.split('=')
                if len(key_value) == 2:
                    key, value = key_value
                    result[key] = value
            return result

if __name__ == '__main__':
    print(parse('https://example.com/path/to/page?name=ferret&color=purple&size=small'))
    assert (parse('https://example.com/path/to/page?name=ferret&color=purple&size=small')
            == {'name': 'ferret', 'color': 'purple', 'size': 'small'})
    print(parse('https://example.com/path/to/page?'))
    assert parse('https://example.com/path/to/page?') == {}
    print(parse('https://example.com/path/to/page'))
    assert parse('https://example.com/path/to/page') == {}
    print(parse('https://example.com/path/to/page?name=ferret&color=purple&size=small&'))
    assert (parse('https://example.com/path/to/page?name=ferret&color=purple&size=small&')
            == {'name': 'ferret', 'color': 'purple', 'size': 'small'})
    print(parse('https://example.com/path/to/page?animal=cat&animal=dog'))
    assert parse('https://example.com/path/to/page?animal=cat&animal=dog') == {'animal': 'dog'}

def parse_cookie(query: str) -> dict:
    if not query:
        return {}
    else:
        cookie_params = query.split(';')
        result = {}
        for param in cookie_params:
            key_value = param.strip().split('=', 1)
            if len(key_value) == 2:
                key, value = key_value
                result[key] = value
        return result

if __name__ == '__main__':
    print(parse_cookie('name=Dima;age=28;country=USA'))
    assert (parse_cookie('name=Dima;age=28;country=USA') ==
            {'name': 'Dima', 'age': '28', 'country': 'USA'})
    print(parse_cookie('name=Dima;age=28;country=USA;'))
    assert (parse_cookie('name=Dima;age=28;country=USA;') ==
            {'name': 'Dima', 'age': '28', 'country': 'USA'})
    print(parse_cookie('name=Dima;age=28;country=USA;role=admin'))
    assert (parse_cookie('name=Dima;age=28;country=USA;role=admin') ==
            {'name': 'Dima', 'age': '28', 'country': 'USA', 'role': 'admin'})
    print(parse_cookie('name=Dima=User;age=28;'))
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    print(parse_cookie('invalid_cookie_data'))
    assert parse_cookie('invalid_cookie_data') == {}


