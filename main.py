# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

from unit import fileUnit


class PyClassTest:

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def printMsg(self):
        print(f"姓名： {self.name}，年龄：{self.age}，职业：{self.job}")


class PyExtendTest(PyClassTest):

    def __init__(self, name, age, job, link):
        PyClassTest.__init__(self, name, age, job)
        self.link = link

    def printMsg(self):
        PyClassTest.printMsg(self)
        print(f"link {self.link}")


if __name__ == '__main__':
    fileUnit.writeFile(fileName='Files/test2.txt', content='''我是谁，我是你爹\n我是谁，我是你爸爸\n还有多少人事\'jascola\'
成为黄天之士的祭品吧''')
    fileUnit.readText(fileName='Files/test2.txt')
    fileUnit.copyFile(fileName='Files/lukaliou.jpg', copyFile='Files/lukaliou2.jpg')

    classTest = PyClassTest('jascola', 10, '教师')
    classTest.printMsg()

    pyExtendTest = PyExtendTest('jascola', 20, '程序员', "www.baidu.com")
    pyExtendTest.printMsg()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
