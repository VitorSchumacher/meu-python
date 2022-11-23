class A():
    def m1(self):
        print("oi")

class B(A):
    def m2(self):
        print("B")

class C(A):
    def m2(self):
        print("C")

class D(C,B):
    def m3(self):
        print("D")


if __name__ == "__main__":
    algo = D()
    algo.m1()