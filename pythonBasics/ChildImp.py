from pythonBasics.OopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def get_complete_data(self):
        return self.num2 + self.num + self.summation()


obj = ChildImpl()
print(obj.get_complete_data())
