# -*- coding: cp1251 -*-

def search_element(data, tag):
    result = None
    if tag in data:
        return data[tag]
    for key, value in data.items():
        if isinstance(value, dict):
            result = search_element(value, tag)
            if result:
                return result
    return result


site = {

    'html': {

        'head': {

            'title': '��� ����'

        },

        'body': {

            'h2': '����� ����� ��� ���������',

            'div': '���, ��������, �����-�� ����',

            'p': '� ��� ����� ����� �����'

        }

    }

} 

search_key = input("������� ����: ")

value = search_element(site, search_key)
if value:
    print("��������:", value)
else:
    print("������ ����� � ��������� ����� ���.")
