class ElectionResults:
  
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        self.file = open(self.filename, 'r')
        self.all_lines = self.file.readlines()

    def states1(self):
        all_names1 = []
        for line1 in self.all_lines:
            columns1 = line1.split(',')
            all_names1.append(columns1[3])
        return all_names1[3:]

    def states2(self):
        all_names2 = []
        for line2 in self.all_lines:
            columns2 = line2.split(',')
            all_names2.append(columns2[5])
        return all_names2[5:]

    def state_count1(self):
        return len(self.states1())
