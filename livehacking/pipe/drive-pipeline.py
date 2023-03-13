import sys
import pandas

csv_file = sys.argv[1]
filters = sys.argv[2:]
print('filters:', filters)

data = pandas.read_csv(csv_file, delimiter=';', encoding='iso-8859-1',
                       names=['account', 'info', 'time_booked', 'time_valuta', 'amount', 'unit'])

# interpret filters
for filter_file in filters:
    code_file = open(filter_file)
    code = code_file.read()
    # print(code, type(code))
    context = {}
    exec('import pandas as pd', context)
    exec('import numpy as np', context)

    exec(code, context)

    transform_function = context['transform']
    # print(transform_function)
    data = transform_function(data)

# pandas.options.display.max_colwidth = None
# pandas.options.display.max_columns = None
# pandas.options.display.max_rows = None
# pandas.options.display.width = None

#print(data[['info', 'amount']])
print(data)
