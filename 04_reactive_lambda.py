from rx import Observable, Observer


flores = Observable.from_(["Versicolor","Virginica","Setosa"])

flores.subscribe(on_next = lambda flor : print(flor))

