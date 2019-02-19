from rx import Observable, Observer


flores = Observable.from_(["Versicolor","Virginica","Setosa"])


class Observador(Observer):
    def on_next(self, value):
        print(value)

    def on_completed(self):
        print("Completed")

    def on_error(self, error):
        print("Error:{}".format(error))

flores.subscribe(Observador())

