import json


def response_data_to_dict(response):
    str_data = str(response.data, encoding='utf-8')
    dict_data = json.loads(str_data)
    return dict_data['data']


def extract_field_by_attribute(dict, field, attribute):
    if attribute in dict:
        return f'{field}：{dict[attribute].strip()}\n'
    return ''
