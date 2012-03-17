import sys
sys.path.append("../..")
import unittest

TEST_MODULES = [
        'thunder.test.model_test',
    ]

def all():
    try:
        return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)
    except AttributeError, e:
        if "'module' object has no attribute 'model_test'" in str(e):
            for m in TEST_MODULES:
                __import__(m, globals(), locals())
        raise

if __name__ == '__main__':
    import tornado.testing
    try:
        tornado.testing.main()
    except KeyboardInterrupt:
        pass #exit
