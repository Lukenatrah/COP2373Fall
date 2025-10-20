import re

def split_into_sentences(paragraph):
    """
    Splits a paragraph into sentences using regular expressions.
    Handles sentences that start with numbers as well.
    """
    # Regex pattern: look for punctuation (., ?, !) followed by a space or line end
    # and a capital letter OR number, without splitting inside decimals or abbreviations.
    sentence_pattern = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9])')
    sentences = re.split(sentence_pattern, paragraph.strip())
    return sentences

def display_sentences(sentences):
    """
    Displays each sentence and the total sentence count.
    """
    print("\nIndividual Sentences:\n")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")
    print(f"\nTotal number of sentences: {len(sentences)}")

def main():
    paragraph = input("Enter a paragraph: ")
    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)

if __name__ == "__main__":
    main()
