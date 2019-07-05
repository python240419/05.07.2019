>>> a = {'b': 1, 'a': 2}
>>> a
{'b': 1, 'a': 2}
>>> a.pop('b')
1
>>> a
{'a': 2}
>>> a = {1 : 'itay'}
>>> a
{1: 'itay'}
>>> a[1]
'itay'
>>> a[2] = 'dana'
>>> a
{1: 'itay', 2: 'dana'}
>>> del a[2]
>>> a
{1: 'itay'}
>>> a[3] = 'ranny'
>>> a
{1: 'itay', 3: 'ranny'}
>>> a[3] = 'edi'
>>> a
{1: 'itay', 3: 'edi'}
>>> a.pop(3)
'edi'
>>> a
{1: 'itay'}
