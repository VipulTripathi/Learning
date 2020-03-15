from jsonFiles.data import data

class test:
    def runtest(self, details):
        for i in details:
            print(details[i],' - ', i)

t=test()
t.runtest(data)
