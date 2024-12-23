import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.task5.src.task5 import american_election


class TestAmericanPresidents(unittest.TestCase):
    def test_should_mini_planning(self):
        # given
        test_cases = [
            (["Biden 500", "Trump 400", "Biden 200", "Trump 100"], [["Biden", 700], ["Trump", 500]]),
            (["Obama 1000", "Trump 200", "Obama 500", "Trump 300"], [["Obama", 1500], ["Trump", 500]]),
            (["Clinton 800", "Bush 600", "Clinton 400", "Bush 200"], [["Bush", 800], ["Clinton", 1200]]),
            (["Kennedy 1000", "Johnson 500", "Kennedy 200", "Johnson 300"], [["Johnson", 800], ["Kennedy", 1200]]),
            (["Lincoln 100", "Washington 200", "Lincoln 300"], [["Lincoln", 400], ["Washington", 200]]),
        ]

        # when
        result = [american_election(data) for data, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


if __name__ == "__main__":
    unittest.main()
