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
    
    def searching_method(self):
        length_list = len(self.list)
        middle_index = (length_list - 1) // 2
        counter = 0
        if counter != length_list:
            return self.list[middle_index]
        else:
            return 0

if __name__ == "__main__":
    experiment = Experiment()

    start_time = timeit.default_timer()
    print(experiment.for_loop())
    end_time = timeit.default_timer()
    print("Execution time for for_loop: ", end_time - start_time)

    start_time = timeit.default_timer()
    print(experiment.while_loop())
    end_time = timeit.default_timer()
    print("Execution time for while_loop: ", end_time - start_time)

    start_time = timeit.default_timer()
    print(experiment.searching_method())
    end_time = timeit.default_timer()
    print("Execution time for searching method: ", end_time - start_time)