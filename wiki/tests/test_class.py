import allure
import pytest

from wiki import wiki_parser


class TestClass:

    @allure.title("Wiki table test with popularity param {min_pop}")
    @pytest.mark.parametrize('min_pop', [100, 10 ** 7, 1.5 * (10 ** 7), 5 * 10 ** 7,
                                         10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
    def test_wiki_table(self, min_pop):
        errors = []
        x = wiki_parser.get_wiki_items()

        for item in x:
            if not item.popularity > min_pop:
                errors.append("""{0} has {1} unique visitors per month. (Expected more than {2})\n""".format(item.desc, item.popularity, min_pop))

        assert not errors, "Errors:\n{}".format("".join(errors))
