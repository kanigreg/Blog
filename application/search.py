from flask import current_app


def add_to_index(index, model):
    """
    Функция добавления индексиремого текста в движок поиска
    :param index: индекс записи
    :param model: модель данных, должна реализовывать поле __searchable__
    """
    if not current_app.elasticsearch:
        return
    payload = {}
    for feild in model.__searchable__:
        payload[feild] = getattr(model, feild)
    current_app.elasticsearch.index(index=index, doc_type=index, id=model.id, body=payload)


def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, doc_type=index, id=model.id)


def search(index, query, page, per_page):
    if not current_app.elasticsearch:
        return [], 0
    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page}
    )
    ids = [int(hit['_id']) for hit in search['hits']['hits']]

    return ids, search['hits']['total']['value']
