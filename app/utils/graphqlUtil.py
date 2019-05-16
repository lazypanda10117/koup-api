from graphql_relay.node.node import from_global_id
import app.utils.json as json


def input_to_dictionary(input_dict):
    dictionary = {}
    for key in input_dict:
        # Convert GraphQL global id to database id
        if key == 'id':
            input_dict[key] = int(from_global_id(input_dict[key])[1])
        dictionary[key] = input_dict[key]
    return dictionary


def serialize(obj, filter_list=None):
    filter_list = [] if filter_list is None else filter_list
    return {
        key: val
        for key, val in json.loads(json.dumps(obj)).items()
        if key not in filter_list
    }
