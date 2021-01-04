def readText(fileName):
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    with open(fileName, 'r', encoding='UTF-8') as f:
        while True:
            data = f.readline()
            if not data:
                break
            print(data)
        f.close()


def writeFile(fileName, content):
    with open(fileName, 'w', encoding='UTF-8') as f:
        f.write(content)
        f.close()


def copyFile(*, fileName, copyFile):
    try:
        with open(fileName, 'rb') as f:
            with open(copyFile, 'wb') as w:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    w.write(data)
    except IOError as e:
        print("exception", e)

    finally:
        print("finally exe")


if __name__ == '__main__':
    print("--")
else:
    print("文件模块初始化")
