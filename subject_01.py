from rx import Observable, Observer
from rx.subjects import Subject

AA = Subject()

aa = AA.filter(lambda s: s == 'A') \
    .map(lambda s: s.lower()).publish()

aa.subscribe(lambda a: print(a) )
AA.subscribe(lambda a: print("{}".format(2)))

aa.connect()
Observable.from_("A,B,C,D,D,E,F,G,H".split(','))\
    .subscribe(AA.on_next)


for s in "A,B,C,D,D,E,F,G,H":
    AA.on_next(s)