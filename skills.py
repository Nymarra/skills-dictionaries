"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    return list(set(words))


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    items1 = set(items1)
    items2 = set(items2)

    return list(items1 & items2)


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    phrase = phrase.split()
    word_counts = {}
    for word in phrase:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else: word_counts[word] = 1


    return word_counts


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # english to pirate dictionary
    ENG_TO_PIRATE = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "boy": "matey",
        "professor": "floul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
        "man": "matey"
    }

    # tokenizes input string into a list of words
    phrase = phrase.split()

    # loops through phrase and changes word to pirate counterpart
    for word in phrase:
        word_index = phrase.index(word)
        if word in ENG_TO_PIRATE:
            phrase[word_index] = ENG_TO_PIRATE[word]

    # converts list back to string
    phrase = " ".join(phrase)


    return phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """
    lengths = {}
    # builds a dictionary using the length of words as a key and a list of words that length as a value
    for word in words:
        key = len(word)
        if key in lengths:
            lengths[key].append(word)
        else:
            lengths[key] = [word]
    # builds a list of tuples for key-value pairs in the dictionary 'lengths'
    word_groups = lengths.items()

    return sorted(word_groups)




def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    # loops through list 'numbers', finds 0-pairs (and sorts them) and if they aren't already on the list, adds them
    zero_pairs = []
    for num_a in numbers:
        for num_b in numbers:
            if num_a + num_b == 0:
                pair = sorted([num_a, num_b])
                if pair not in zero_pairs:
                    zero_pairs.append(pair)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # NOTE FOR LESLIE
    # There has to be a better way to do this. I tried passing the individual pairs to a set t eliminate duplicates,
    # but I kept getting errors that lists aren't a 'hashable' type and therefore can't be individual items in a set.
    # As a result, the only way I could think of was yet another 'if statement'

    return sorted(zero_pairs)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    word_options = {}

    #loops through 'names' from the second word onwards
    for name in names[1:]:
        key = name[0]
        # evaluates of the first letter of 'name' being looped through is a key in the dictionary 'word_options'
        # if it exists, it appends 'name' to the current list that is a value for that key.
        # if it doesn't exist, it creates the key-value pair.
        if key in word_options:
            word_options[key].append(name)
        else:
            word_options[key] = [name]
    # assigns the first word in 'names' to be the first word in 'sentence'
    sentence = [names[0]]

    # loops through a sentence while it is creating itself to choose the next word
    for word in sentence:
        # picks the last letter of the last word in the sentence to serve as the first letter of the next word.
        starter = word[-1]

        if starter in word_options:
            value = word_options[starter]
            next_word = value[0]
            # checks if there is more than word that starts with the letter serving as a key, and removes either the
            # key or the value accordingly

            if len(value) > 1:
                value.remove(next_word)
            if len(value) == 1:
                del word_options[starter]

            sentence.append(next_word)

    return sentence


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
