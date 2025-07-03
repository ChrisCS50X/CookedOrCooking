class Solution:
    ''' 
    Problem : Alice has a string word = "a". You are given a positive integer k. 
    Now Bob will ask Alice to perform the following operation forever:
    Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
    For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
    
    Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

    Example 1:

    Input: k = 5

    Output: "b"

    Explanation:

    Initially, word = "a". We need to do the operation three times:

    Generated string is "b", word becomes "ab".
    Generated string is "bc", word becomes "abbc".
    Generated string is "bccd", word becomes "abbcbccd".

    '''

    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < k:
            for character in word:
                word += chr(ord(character) + 1)

        print(word)

        return word[k - 1]


def main():
    solution = Solution()

    test_cases = [5,10]

    print("Testing kthCharacter function:")
    print("-" * 30)

    for k in test_cases:
        result = solution.kthCharacter(k)
        print(f"k = {k}: {result}")
        print()


if __name__ == "__main__":
    main()
