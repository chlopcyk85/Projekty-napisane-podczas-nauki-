import csv
import pickle
import json
import sys


class Reader:
    def __init__(self, file_input, file_output, changes):
        self.file_input = file_input
        self.file_output = file_output
        self.changes = changes
        self.data = []

    def file_reader(self):
        try:
            with open(self.file_input, "r") as file:
                if self.file_input.endswith(".csv"):
                    reader = csv.reader(file, delimiter=";")
                    self.data = [row for row in reader]
                elif self.file_input.endswith(".txt"):
                    self.data = [row for row in file.readlines()]
                elif self.file_input.endswith(".json"):
                    self.data = json.load(file)
                elif self.file_input.endswith(".pickle"):
                    self.data = pickle.load(file)
        except FileNotFoundError:
            print(f"Nie znaleziono pliku wejściowego {self.file_input}")
            sys.exit(1)

    def new_changes(self):
        try:
            for change in self.changes:
                x, y, value = change.split(",")
                x, y = int(x), int(y)
                self.data[x][y] = value
        except (ValueError, IndexError, TypeError):
            print("Złe argumenty, dane nie zostały zmienione!")
            sys.exit(1)

    def file_writer(self):
        try:
            with open(self.file_output, "w", newline="") as file:
                if self.file_output.endswith(".csv"):
                    writer = csv.writer(file)
                    writer.writerows(row for row in self.data)
                elif self.file_output.endswith(".txt"):
                    file.writelines('\n'.join(self.data))
                elif self.file_output.endswith(".json"):
                    json.dump(self.data, file)
                elif self.file_output.endswith(".pickle"):
                    pickle.dump(self.data, file)
        except TypeError:
            print("Podano złe argumenty do zapisu pliku")

    def main(self):
        self.file_reader()
        self.new_changes()
        self.file_writer()


class ReaderInh(Reader):
    def __str__(self):
        return self.data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Nieprawidłowa ilość argumentów, dane nie zostały zmienione")
        sys.exit(1)


file_input = sys.argv[1]
file_output = sys.argv[2]
changes = sys.argv[3:]

ReaderProcess = ReaderInh(file_input, file_output, changes)
ReaderProcess.main()


[print(row) for row in ReaderProcess.data]
