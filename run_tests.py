import importlib.util
import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parent


def load_tests_from_file(path):
    relative = path.relative_to(ROOT)
    module_name = "test_" + "_".join(relative.with_suffix("").parts)
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return unittest.defaultTestLoader.loadTestsFromModule(module)


def main():
    suite = unittest.TestSuite()
    for test_file in sorted(ROOT.glob("lab*/task*/tests/test_*.py")):
        suite.addTests(load_tests_from_file(test_file))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
