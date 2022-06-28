ALL_PARAMS = ['spec', 'findDateGte', 'findDateLte', 'createdAtGte', 'createdAtLte', 'count'] 

def parse_query_params(params):
    query_params = []
    # if 'find' in params:
        #     query_params.append(('find', params['find']))  # noqa: E501
    if 'findDateGte' in params:
        query_params.append(('find[dateString][$gte]', params['findDateGte']))  # noqa: E501
    if 'findDateLte' in params:
        query_params.append(('find[dateString][$lte]', params['findDateLte']))  # noqa: E501
    if 'createdAtGte' in params:
        query_params.append(('find[created_at][$gte]', params['createdAtGte']))  # noqa: E501
    if 'createdAtLte' in params:
        query_params.append(('find[created_at][$lte]', params['createdAtLte']))  # noqa: E501
    if 'count' in params:
        query_params.append(('count', params['count']))  # noqa: E501

    print("QUERY PARAMS: {}".format(query_params))
    return query_params
