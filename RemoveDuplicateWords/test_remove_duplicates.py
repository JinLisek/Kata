from remove_duplicates import remove_duplicate_words


class TestRemoveDuplicates:
    def test_given_empty_string_should_return_empty_string(self):
        assert remove_duplicate_words("") == ""

    def test_given_single_word_should_return_the_word(self):
        assert remove_duplicate_words("word") == "word"

    def test_given_two_unique_words_should_return_both_words(self):
        unique_words = "unique words"
        assert remove_duplicate_words(unique_words) == unique_words

    def test_given_two_duplicated_words_should_return_only_one_word(self):
        assert remove_duplicate_words("duplicate duplicate") == "duplicate"

    def test_given_two_unconcurrent_duplicates_should_remove_second_occurence(self):
        assert remove_duplicate_words("duplicate word duplicate") == "duplicate word"

    def test_given_two_pairs_of_duplicates_should_return_only_first_occurence_from_each_pair(
        self,
    ):
        assert (
            remove_duplicate_words("duplicate word word duplicate") == "duplicate word"
        )
