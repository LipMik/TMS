some_dict = (lambda **kwargs: {kwargs * 2: couple for kwargs, couple in kwargs.items()})(a=1, b=2, c=3)

print(some_dict)
