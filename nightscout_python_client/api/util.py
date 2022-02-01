ALL_PARAMS = ['spec', 'findDateGte', 'findDateLte', 'count'] 

def parse_query_params(params):
    query_params = []
    # if 'find' in params:
        #     query_params.append(('find', params['find']))  # noqa: E501
    if 'findDateGte' in params:
        query_params.append(('find[dateString][$gte]', params['findDateGte']))  # noqa: E501
    if 'findDateLte' in params:
        query_params.append(('find[dateString][$lte]', params['findDateLte']))  # noqa: E501
        # query_params.append(('find[date][$lt]', params['findDateLte']))  # noqa: E501
    if 'count' in params:
        query_params.append(('count', params['count']))  # noqa: E501

    print("QUERY PARAMS: {}".format(query_params))
    return query_params
