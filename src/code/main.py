import timeit


class Experiment:
    def __init__(self) -> None:
        pass
    
    def open_file(self):
        file_path = "numbers.txt"
        numbers = []
        with open(file_path, "r", encoding = "utf-8") as fh:
            for line in fh:
                if " – " in line:
                    number, _ = line.split(" – ")
                    numbers.append(int(number.strip()))
        return numbers



if __name__ == "__main__":
    experiment = Experiment()
    print(experiment.open_file())
    