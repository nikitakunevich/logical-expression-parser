from main import parse
def test():
    obj_parens = {
        'type': 'node',
        'op': 'AND',
        'left': {
            'type': 'leaf',
            'op': '=',
            'id': 'Пол',
            'literal': "М"
        },
        'right': {            
            'type': 'node',
            'op': 'OR',
            'left': {
                'type': 'leaf',
                'op': '>',
                'id': 'Возраст',
                'literal': 25
            },
            'right': {
                'type': 'leaf',
                'op': '>',
                'id': 'Стаж',
                'literal': 0.5
            }
        }
    }
    obj_simple = {
        'type': 'node',
        'op': 'OR',
        'left': {            
            'type': 'node',
            'op': 'AND',
            'left': {
                'type': 'leaf',
                'op': '=',
                'id': 'Пол',
                'literal': "М"
            },
            'right': {
                'type': 'leaf',
                'op': '>',
                'id': 'Возраст',
                'literal': 25
            }
        },
        'right': {
            'type': 'leaf',
            'op': '>',
            'id': 'Стаж',
            'literal': 0.5
        },
    }

    obj_double_parens = {
        'type': 'node',
        'op': 'AND',
        'left': {
            'type': 'leaf',
            'op': '=',
            'id': 'Пол',
            'literal': "М"
        },
        'right': {            
            'type': 'node',
            'op': 'OR',
            'left': {
                'type': 'leaf',
                'op': '>',
                'id': 'Возраст',
                'literal': 25
            },
            'right': {
                'type': 'node',
                'op': 'AND',
                'left': {
                    'type': 'leaf',
                    'op': '>',
                    'id': 'Стаж',
                    'literal': 0.5
                },
                'right': {
                    'type': 'leaf',
                    'op': '!=',
                    'id': 'Должность',
                    'literal': "Руководитель"
                }
            }
        }
    }
    obj_additional_parens = {
        'type': 'node',
        'op': 'AND',
        'left': {
            'type': 'leaf',
            'op': '=',
            'id': 'Пол',
            'literal': "М"
        },
        'right': {
            'type': 'leaf',
            'op': '>',
            'id': 'Возраст',
            'literal': 25
        }
    }

    obj_one = {
        'type':'leaf',
        'op':'=',
        'id':'Пол',
        'literal':'М'
    }

    assert parse('Пол="М" AND (Возраст>25 OR Стаж>.5)') == obj_parens
    assert parse('Пол="М" AND (Возраст>25 OR (Стаж>.5 AND Должность!="Руководитель"))') == obj_double_parens
    assert parse('Пол="М" AND (Возраст>25)') == obj_additional_parens
    assert parse('Пол="М"') == obj_one

    try:
        parse('')
    except Exception:
        assert(True)
    else:
        assert(False)

    try:
        parse('AND')
    except Exception:
        assert(True)
    else:
        assert(False)