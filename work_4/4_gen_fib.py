def fibgen(f0, f1):
    while True:
        f0, f1 = f1, f1 + f0
        yield f0
