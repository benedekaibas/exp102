import timeit


class Experiment:
    def __init__(self) -> None:
        pass
        self.list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

    def for_loop(self):
        """Searching with for loop."""
        for item in self.list:
            length_list = len(self.list)
            item = (length_list - 1) // 2
        return self.list[item]

    def while_loop(self):
        """Searching with while loop."""
        while item in self.list:
            length_list = len(self.list)
            item = (length_list - 1) // 2
        return self.list[item]

if __name__ == "__main__":
    experiment = Experiment()
    print(experiment.for_loop())
    print(experiment.while_loop())