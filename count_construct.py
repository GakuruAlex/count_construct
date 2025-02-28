from typing import List
def count_construct(target_word: str, word_bank: List[str]) -> int:
    count: int = 0
    if target_word == "":
        return 1
    for word in word_bank:
        if target_word.startswith(word):
            new_target_word: str = target_word[len(word):]
            count += count_construct(target_word=new_target_word, word_bank=word_bank)
    return count

def main()-> None:
    target_word: str = 'abcdef'
    word_bank: List[str] = ['ab', 'abc', 'cd', 'def', 'abcd']
    count: int = count_construct(target_word=target_word, word_bank=word_bank)
    print(f"Number of ways to construct {target_word} by concatenating str(s) in {word_bank} is {count}")

if __name__ =="__main__":
    main()