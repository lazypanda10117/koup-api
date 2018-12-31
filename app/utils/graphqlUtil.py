from graphql_relay.node.node import from_global_id
import json


def input_to_dictionary(input):
    dictionary = {}
    for key in input:
        # Convert GraphQL global id to database id
        if key[-2:] == 'id':
            input[key] = int(from_global_id(input[key])[1])
        dictionary[key] = input[key]
    return dictionary


def dumps(obj):
    json.dumps(obj)
