from rx import Observable,  Observer

Observable.interval(55) \
    .filter(lambda i : i%2 == 0) \
    .subscribe(lambda i : print(i))


input("Enter para terminar\n")
