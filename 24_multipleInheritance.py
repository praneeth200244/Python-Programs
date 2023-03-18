class Teacher:
    def __init__(self, name, qualification):
        self.name = name
        self.qualification = qualification

    def show(self):
        print(
            f"The name is {self.name} and qualification is {self.qualification}")


class Vlogger:
    def __init__(self, channelName):
        self.channelName = channelName

    def show(self):
        print(f"The name of the channel is {self.channelName}")
        Teacher.show(self)


class VloggerTeacher(Vlogger, Teacher):
    def __init__(self, name, qualification, channelName):
        Teacher.__init__(self, name, qualification)
        Vlogger.__init__(self, channelName)


vt = VloggerTeacher("Anush", "M.Sc", "ChemWithAnu")
vt.show()

print(VloggerTeacher.mro())
