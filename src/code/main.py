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
        length_list = len(self.list)
        middle_index = (length_list - 1) // 2
        counter = 0
        while counter < middle_index:
            counter += 1
        return self.list[counter]

    def time_loops(self):
        for_loop = self.for_loop()
        while_loop = self.while_loop()

        

if __name__ == "__main__":
    experiment = Experiment()
    print(experiment.for_loop())
    print(experiment.while_loop())