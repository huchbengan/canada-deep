stop_words = ['on', 'in', 'and', 'of', 'a', 'an', 'between',
              'to', 'from', 'for', 'the', 'at', 'before', 'after',
              'by', 'under', 'above', 'with', 'into', 'within',
              'without', 'over', 'off','or']


def foo(a_title: str):
    original = a_title.title().strip()
    res = []
    for item in original.split():
        if item.lower() in stop_words:
            item = item.lower()
            res.append(item)
        else:
            res.append(item)
    res = ' '.join(res).strip()

    if len(res) == len(original):
        return res
    else:
        return '长度不一致', a_title


xx = foo('How to Identify, Treat, And Prevent Root Rot? ')

boo = [i for i in boo.split('\n') if i != '']
for i in boo:
    print(foo(i))
