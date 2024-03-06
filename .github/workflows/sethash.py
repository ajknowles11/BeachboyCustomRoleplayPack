import sys

# arg 1 is filename, arg 2 is new hash

fin = open(sys.argv[1], "r")

lines = fin.readlines()

line_num = -1
for k,line in enumerate(lines):
    if line.find("resource-pack-sha1=") != -1:
        line_num = k

if line_num == -1:
    raise Exception("missing resource-pack-sha1 line")

lines[line_num] = "resource-pack-sha1=" + sys.argv[2] + '\n'

fin.close

fout = open(sys.argv[1], "w")
fout.writelines(lines)
fout.close()
