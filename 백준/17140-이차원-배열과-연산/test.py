f = open("/Users/daewoongko/Algo/백준/17140-이차원-배열과-연산/test.txt", "w")
st = ""

r = range(1, 102)
for i in r:
    st += "{} ".format(i)
    if i == len(r):
        st += "{}".format(i)
f.write(st)
f.write(st)
f.write(st)
f.close()
