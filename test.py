import os
dir = os.getcwd()

listfile = []
for r, d, f in os.walk(f"{dir}\data"):
    for file in f:

        if file.endswith(".csv"):
            listfile.append(os.path.join(r, file))

for file in listfile:
    print(file.split("\\")[-1])