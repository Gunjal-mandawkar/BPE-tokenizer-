from tokenizer import BPETokenizer

if __name__ == "__main__":
    tokenizer = BPETokenizer()
    # corpus = tokenizer.read_file("alice.txt")
    # print("Before merge:", corpus)
    # stats = tokenizer.get_stats(corpus)
    # best_pair =  stats.most_common(1)[0][0]
    # print("Pair frequencies:", stats.most_common(5))

    # new_corpus = tokenizer.merge_pair(best_pair, corpus)
    # print("After merge:", new_corpus)
    corpus = tokenizer.train("alice.txt", 10)
    
    encoded = tokenizer.encode("strawberry")
    print("Encoded:", encoded)

    decoded = tokenizer.decode(encoded)
    print("Decoded:", decoded)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("Original text:\n")
        f.write("strawberry" + "\n\n")

        f.write("Final merges (in order):\n")
        for merge in tokenizer.merge:
            f.write(str(merge) + "\n")

        f.write("\nVocab:\n")
        for token, idx in tokenizer.vocab.items():
            f.write(f"{token}: {idx}\n")

        f.write("\nEncoded:\n")
        f.write(str(encoded) + "\n")

        f.write("\nDecoded:\n")
        f.write(decoded + "\n")