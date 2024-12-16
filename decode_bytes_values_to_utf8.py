# convert bytes values in dataframe columns to UTF-8
def decode_bytes(val):
    if isinstance(val, bytes):
        return val.decode('utf-8')
    return val

data[col] = data[col].apply(decode_bytes)
