import timeit
import csv


class Experiment:
    def __init__(self) -> None:
        pass
    
    def for_loop(self):
        file_path = "numbers.txt"
        with open(file_path, "r", encoding = "utf-8") as fh:
            reader = csv.reader(fh)
        return reader


if __name__ == "__main__":
    experiment = Experiment()
    print(experiment.for_loop())