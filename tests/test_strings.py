import random
import unittest

from app.strings import both_ends
from app.strings import donuts
from app.strings import fix_start
from app.strings import mix_up
from app.strings import verbing
from app.strings import not_bad
from app.strings import front_back


class DonutsTest(unittest.TestCase):
    def setUp(self) -> None:
        """Set up all tests with random integer."""
        self.count = random.randrange(15)

    def test_donuts_return_type(self):
        """Ensure donuts return type is a string."""
        results = donuts(self.count)
        self.assertIsInstance(results, str)

    def test_donuts_under_threshold(self):
        """Ensure donuts is correct below threshold."""
        results = donuts(5)
        self.assertEquals(results, 'Number of donuts: 5')

    def test_donuts_under_threshold2(self):
        """Ensure donuts is correct below threshold."""
        results = donuts(9)
        self.assertEquals(results, 'Number of donuts: 9')

    def test_donuts_above_threshold(self):
        """Ensure donuts is correct above threshold."""
        results = donuts(15)
        self.assertEquals(results, 'Number of donuts: many')

    def test_donuts_above_threshold2(self):
        """Ensure donuts is correct above threshold."""
        results = donuts(23)
        self.assertEquals(results, 'Number of donuts: many')

    def test_donuts_at_threshold(self):
        """Ensure donuts is correct at threshold."""
        results = donuts(10)
        self.assertEquals(results, 'Number of donuts: many')


class BothEndsTest(unittest.TestCase):
    def setUp(self) -> None:
        """Set up all tests with random string."""
        self.example = 'Shrek'

    def test_both_ends_return_type(self):
        """Ensure both_ends return type is a string."""
        results = both_ends(self.example)
        self.assertIsInstance(results, str)

    def test_both_ends_above_threshold(self):
        """Ensure both_ends is correct above threshold."""
        results = both_ends('let')
        self.assertEquals(results, 'leet')

    def test_both_ends_above_threshold2(self):
        """Ensure both_ends is correct above threshold."""
        results = both_ends('Cigna')
        self.assertEquals(results, 'Cina')

    def test_both_ends_under_threshold(self):
        """Ensure both_ends is correct above threshold."""
        results = both_ends('q')
        self.assertEquals(results, '')

    def test_both_ends_under_threshold2(self):
        """Ensure both_ends is correct above threshold."""
        results = both_ends('f')
        self.assertEquals(results, '')

    def test_both_ends_at_threshold(self):
        """Ensure both_ends is correct at threshold."""
        results = both_ends('at')
        self.assertEquals(results, 'atat')


class FixStartTest(unittest.TestCase):
    def setUp(self) -> None:
        """Set up all tests with random string."""
        self.example = 'Shrek'

    def test_fix_start_return_type(self):
        """Ensure both_ends return type is a string."""
        results = fix_start(self.example)
        self.assertIsInstance(results, str)

    def test_fix_start_test_criteria1(self):
        """Ensure fix_start is performing as expected."""
        results = fix_start('tattle')
        self.assertEquals(results, 'ta**le')

    def test_fix_start_test_criteria2(self):
        """Ensure fix_start is performing as expected."""
        results = fix_start('pop')
        self.assertEquals(results, 'po*')

    def test_fix_start_test_non_criteria(self):
        """Ensure fix_start is performing as expected."""
        result = fix_start('mississippi')
        self.assertEquals(result, 'mississippi')

    def test_fix_start_test_non_criteria2(self):
        """Ensure fix_start is performing as expected."""
        result = fix_start('glass')
        self.assertEquals(result, 'glass')


class MixUpTest(unittest.TestCase):
    def setUp(self) -> None:
        """Set up all tests with random string."""
        self.example = 'Shrek'

    def test_mix_up_return_type(self):
        """Ensure mix_up return type is a string."""
        results = mix_up(self.example, self.example)
        self.assertIsInstance(results, str)

    def test_mix_up_criteria1(self):
        """Ensure mix_up performs correctly."""
        results = mix_up('mite', 'kitten')
        self.assertEquals(results, 'kite mitten')

    def test_mix_up_criteria2(self):
        """Ensure mix_up performs correctly."""
        results = mix_up('dot', 'hog')
        self.assertEquals(results, 'hot dog')

    def test_mix_up_criteria3(self):
        """Ensure mix_up performs correctly."""
        results = mix_up('brave', 'height')
        self.assertEquals(results, 'heave bright')

    def test_mix_up_criteria4(self):
        """Ensure mix_up performs correctly."""
        results = mix_up('stsert', 'deorm')
        self.assertEquals(results, 'desert storm')

    def test_mix_up_criteria5(self):
        """Ensure mix_up performs correctly."""
        results = mix_up('greed', 'blow')
        self.assertEquals(results, 'bleed grow')


class VerbingTest(unittest.TestCase):
    def setUp(self) -> None:
        """Set up all tests with random string."""
        self.example = 'Shrek'

    def test_verbing_return_type(self):
        """Ensure verbing return type is a string."""
        results = verbing(self.example)
        self.assertIsInstance(results, str)

    def test_verbing_below_threshold(self):
        """Ensure verbing performs correctly below threshold."""
        results = verbing('at')
        self.assertEquals(results, 'at')

    def test_verbing_below_threshold2(self):
        """Ensure verbing performs correctly below threshold."""
        results = verbing('I')
        self.assertEquals(results, 'I')

    def test_verbing_at_threshold(self):
        """Ensure verbing performs correctly below threshold."""
        results = verbing('the')
        self.assertEquals(results, 'theing')

    def test_verbing_above_threshold(self):
        """Ensure verbing performs correctly below threshold."""
        results = verbing('fight')
        self.assertEquals(results, 'fighting')

    def test_verbing_above_threshold_with_ing(self):
        """Ensure verbing performs correctly below threshold."""
        results = verbing('spring')
        self.assertEquals(results, 'springly')


class NotBadTest(unittest.TestCase):
    def setUp(self) -> None:
        """Set up all tests with random string."""
        self.example = 'Shrek'

    def test_not_bad_return_type(self):
        """Ensure not_bad return type is a string."""
        results = not_bad(self.example)
        self.assertIsInstance(results, str)

    def test_not_bad_criteria1(self):
        """Ensure not_bad performs correctly."""
        results = not_bad('This show is not that bad!')
        self.assertEquals(results, 'This show is good!')

    def test_not_bad_criteria2(self):
        """Ensure not_bad performs correctly."""
        results = not_bad('His attitude is bad!')
        self.assertEquals(results, 'His attitude is bad!')

    def test_not_bad_criteria3(self):
        """Ensure not_bad performs correctly."""
        results = not_bad('He is not funny!')
        self.assertEquals(results, 'He is not funny!')

    def test_not_bad_criteria4(self):
        """Ensure not_bad performs correctly."""
        results = not_bad('His sister is bad, not him!')
        self.assertEquals(results, 'His sister is bad, not him!')


class FrontBackTest(unittest.TestCase):
    def setUp(self) -> None:
        """Set up all tests with random string."""
        self.example = 'Shrek'

    def test_front_back_return_type(self):
        """Ensure front_back return type is a string."""
        results = front_back(self.example, self.example)
        print(results)
        self.assertIsInstance(results, str)

    def test_front_back_criteria1(self):
        """Ensure front_back performs correctly."""
        results = front_back('abcde', 'fghi')
        self.assertEquals(results, 'abcfgdehi')

    def test_front_back_criteria2(self):
        """Ensure front_back performs correctly."""
        results = front_back('ending', 'early')
        self.assertEquals(results, 'endearingly')

    def test_front_back_criteria3(self):
        """Ensure front_back performs correctly."""
        results = front_back('reti', 'moon')
        self.assertEquals(results, 'remotion')

    def test_front_back_criteria4(self):
        """Ensure front_back performs correctly."""
        results = front_back('hole', 'mess')
        self.assertEquals(results, 'remotion')


if __name__ == '__main__':
    unittest.main()
