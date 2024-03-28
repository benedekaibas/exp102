import timeit


class Experiment:
    def __init__(self) -> None:
        pass
        self.list = list 
    
    def for_loop(self):
        list = [1,2,3,4,5]

        for item in list:
            item = len(list) / sum(list)
        return item


if __name__ == "__main__":
    experiment = Experiment()
    print(experiment.for_loop())
    