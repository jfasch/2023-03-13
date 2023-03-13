def transform(data):
    filt = ((data['category'] == 'unknown') | (data['category'] == 'card-unknown'))
    return data.loc[filt]
