def get_kwargs(**kwargs):
    return kwargs


a = f'{1} + 29'
print(
    get_kwargs(
        one=1,
        two='tow',
        some_one=a,
        is_true=False,
        dictionary={'name': 'Bob', 'age': eval(a)}
    )
)
