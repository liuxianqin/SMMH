import math
from ._global import EPSILON
from ._global import is_zero
from ._global import is_equal

class Vector:

    def __init__(self, lst):
        self._values =list(lst)  #不可更改

    @classmethod
    def zero(cls, dim):
        """返回dim维的零向量"""
        return cls([0]*dim)

    def norm(self):
        """返回向量的模"""
        # mo = 0
        # for value in self._values:
        #     mo += value**2
        # return mo**0.5
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        # return Vector([e/self.norm() for e in self])
        # return 1/self.norm()*Vector([e for e in self])
        # return 1/self.norm()*Vector(self._values)
        if is_zero(self.norm()):
            raise ZeroDivisionError("Normalize erroe: norm is zero.")
        return self/self.norm()

    def __add__(self, other):
        assert len(self) == len(other), \
            "ERROR: Lenth of vectors must be same."
        return Vector([a + b for a,b in zip(self, other)])
    def __sub__(self, other):
        assert len(self) == len(other), \
            "ERROR: Lenth of vectors must be same"
        return Vector([a-b for a,b in zip(self,other)])
    def __mul__(self, k):
        #数量乘法
        return Vector(k*item for item in self)

    def dot(self,other):
        assert len(self)==len(other),"ERROR : Lenth of vectors mest be same"
        return sum(a*b for a,b in zip(self,other))

    @classmethod
    def classdot(cls,Vec1,Vec2):
        assert len(Vec1) == len(Vec2), "length of vectors must be same"
        return sum(a*b for a,b in zip(Vec1,Vec2))

    def __truediv__(self, k):
        return 1/k*self

    def __rmul__(self, k):
        return self*k
    def __pos__(self):
        return 1*self
    def __neg__(self):
        return -1*self



    def __len__(self):
        """返回向量长度"""
        return len(self._values)

    def __iter__(self):
        return self._values.__iter__()

    def __getitem__(self, index):
        return self._values[index]

    def __repr__(self):
        #系统调用
        return "Vector({})".format(self._values)

    def __str__(self):
        #用户调用
        return "({})".format(", ".join(str(e) for e in self._values))

    def __eq__(self, other):
        other_list= other.listback()
        if(len(other) != len(self._values)):
            return False
        return all(is_equal(x,y)  for x,y in zip(self._values,other_list))


    def __neq__(self,other):
        return not(self == other)

    #返回底层列表
    def listback(self):
        return self._values[:]   #不可修改 加上副本


