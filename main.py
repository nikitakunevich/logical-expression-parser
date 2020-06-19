from parser import ExpressionParser
from lark.lexer import Token
from lark.tree import Tree
from lark import LarkError

def recursively_transform(node, out_node):
    out_node['type'] = node.data
    out_node['op'] = str(node.children[1])
    if node.data == 'leaf':
        out_node['id'] = str(node.children[0])
        literal_token = node.children[2].children[0]
        literal_val = str(literal_token)
        if literal_token.type == 'STRING':
            literal_val = literal_val[1:-1]
        elif literal_token.type == 'DECIMAL':
            literal_val = float(literal_val)
        elif literal_token.type == 'INT':
            literal_val = int(literal_val)
        out_node['literal'] = literal_val
    else:
        out_node['left'] = {}
        recursively_transform(node.children[0], out_node['left'])
        out_node['right'] = {}
        recursively_transform(node.children[2], out_node['right'])
    return

def parse(query: str) -> dict:
    """ Парсит логический запрос в дерево операций
    @param query: логический запрос вида 'Пол="М" AND (Возраст>25 OR Стаж>5)'.
        Поддерживаемые операции сравнения: = != > < >= <=
        Поддерживаемые логические операции: AND OR, приоритет одинаковый, группировка скобками
        Поддерживаемые типы литералов: int float str (двойные кавычки внутри строки не допускаются)
    @return: словарь, содержащий дерево операций (см. ассерты)
        Поддерживаемые типы узлов (type):
        leaf - узел, представляющий операцию сравнения
        node - узел, представляющий логическую операцию, имеет два подузла - left, right
    """
    tree = ExpressionParser.parse(query)
    out_dict = {}
    recursively_transform(tree, out_dict)
    return out_dict

if __name__ == '__main__':
    from test import test
    test()