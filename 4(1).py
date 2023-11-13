s = "a b c d e f g"
print(s)

r = s.split()
print(r)
print()


s = "aa.bb.cc.dd.ee.ff.gg"
r0 = s.split()
r1 = s.split(".")
r2 = s.split(sep='.')
print(r0)
print(r1)
print(r2)