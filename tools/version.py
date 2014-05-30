import os, subprocess

with open('hashes.txt', 'r') as f:
    for line in f:
        line_lst = line.split(' ')
        pkg = line_lst[0].strip()
        commit = line_lst[-1].strip()
        try:
            os.chdir("./" + pkg)
            print(pkg)
            print(commit)
            print(subprocess.check_output("git checkout " + commit, shell=True))
            print(subprocess.check_output("git status", shell=True))
        except OSError:
            print("No such package as " + pkg)
        os.chdir("../")

