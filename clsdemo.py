class Test(object):
    @classmethod
    def test(cls,**kwargs):
        self=cls(**kwargs)
        print(self)
Test.test()