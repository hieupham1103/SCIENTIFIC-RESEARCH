import os

list = os.listdir("./input")

print(list)

testCount = 0

for (dirpath, dirnames, filenames) in os.walk("./Input"):
    # print(f"{dirpath}/{filenames}")
    for test in filenames:
        print(f"{dirpath}/{test}")
        ext = test[len(test) - 3:]
        if (ext == "inp"):
            ext = "in"
        os.rename(f"{dirpath}/{test}", f"./output/{testCount}.{ext}")

    testCount += 1
