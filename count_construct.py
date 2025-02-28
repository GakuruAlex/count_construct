from typing import List, Dict
def count_construct(target_word: str, word_bank: List[str]) -> int:
    """_Counts how many ways there are to construct a word by concatenating words from a list_

    Args:
        target_word (str): _Word to construct_
        word_bank (List[str]): _A list of words to use, a word maybe reused multiple times_

    Returns:
        int: _Number of times word can be constructed using various words in the str_
    """
    count: int = 0
    if target_word == "":
        return 1
    for word in word_bank:
        if target_word.startswith(word):
            new_target_word: str = target_word[len(word):]
            count += count_construct(target_word=new_target_word, word_bank=word_bank)
    return count

def count_construct_memo(target_word: str, word_bank: List[str], memo: Dict[str, int]={"": 1}):
    """_summary_

    Args:
        target_word (str): _description_
        word_bank (List[str]): _description_
        memo (_type_, optional): _description_. Defaults to {"": 1}.
    """
    count: int = 0

    if target_word in memo:
        return memo[target_word]
    for word in word_bank:
        if target_word.startswith(word):
            new_target_word: str = target_word.removeprefix(word)
            count += count_construct_memo(target_word=new_target_word, word_bank=word_bank, memo=memo)
            memo[target_word] = count
    memo[target_word] = count
    return memo[target_word]

def main()-> None:
    target_word: str = 'abcdef'
    word_bank: List[str] = ['ab', 'abc', 'cd', 'def', 'abcd']
    count: int = count_construct_memo(target_word=target_word, word_bank=word_bank)
    print(f"Number of ways to construct '{target_word}' by concatenating str(s) in {word_bank} is {count}")

    target_word: str = 'purple'
    word_bank: List[str] = ['purp', 'p', 'ur', 'le', 'purpl']
    count: int = count_construct(target_word=target_word, word_bank=word_bank) #Should yield 2
    print(f"Number of ways to construct '{target_word}' by concatenating str(s) in {word_bank} is {count}")

    target_word: str = 'enterapotentpot'
    word_bank: List[str] = ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']
    count: int = count_construct(target_word=target_word, word_bank=word_bank)
    print(f"Number of ways to construct {target_word} by concatenating str(s) in {word_bank} is {count}")

if __name__ =="__main__":
    main()