from stuff import category

def transform(data):
    data['category'] = data['info'].apply(category.categorize)
    return data
