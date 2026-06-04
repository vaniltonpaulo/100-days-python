class Test:
    _passed = 0
    _failed = 0

    @classmethod
    def assert_equals(cls, actual, expected, msg=None):
        if actual == expected:
            cls._passed += 1
            print(f"  PASS")
        else:
            cls._failed += 1
            label = f" ({msg})" if msg else ""
            print(f"  FAIL{label}: expected {repr(expected)}, got {repr(actual)}")

    @classmethod
    def summary(cls):
        total = cls._passed + cls._failed
        print(f"\n{cls._passed}/{total} tests passed", end="")
        if cls._failed:
            print(f" | {cls._failed} failed")
        else:
            print(" ✓")
        cls._passed = 0
        cls._failed = 0
