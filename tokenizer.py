from collections import Counter
class BPETokenizer:
    def __init__(self):
        self.vocab = {}
        self.id2token ={}
        self.merge = []

    def read_file(self,file_path):
        with open(file_path,"r", encoding="utf-8") as f:
            text = f.read()

        text = text.lower().strip()
        words = text.split()
        corpus = [" ".join(list(w)+ ["</w>"]) for w in words ]

       

        return corpus
    
    def get_stats(self, corpus):
        pairs = Counter()
        for word in corpus:
            symbols = word.split()
            for i in range(len(symbols)-1):
                pair = (symbols[i],symbols[i+1])
                pairs[pair]+=1
        return pairs

    def merge_pair(self, pair, corpus):
        first,second = pair
        new_token = first+second
        new_corpus = []

        for word in corpus:
            symbols = word.split()
            i=0
            merged_word =[]
            while i<len(symbols):
                if i< len(symbols) -1 and symbols[i] == first and symbols[i+1] == second:
                    merged_word.append(new_token)
                    i +=2
                else:
                    merged_word.append(symbols[i])
                    i += 1
            new_corpus.append(" ".join(merged_word))
        return new_corpus

    def train(self, file_path, vocab_size=50):
        corpus = self.read_file(file_path)

        for i in range(vocab_size):
            stats = self.get_stats(corpus)
            if not stats :
                break
            best_pair = stats.most_common(1)[0][0]
            corpus = self.merge_pair(best_pair,corpus)
            self.merge.append(best_pair)
            print(f"Step {i+1}: merged {best_pair}")

            tokens = set()
            for word in corpus:
                for symbol in word.split():
                    tokens.add(symbol)
            
            self.vocab = {tok: idx for idx, tok in enumerate(sorted(tokens))}
            self.id2token = {idx: tok for tok, idx in self.vocab.items()}

            return corpus

    def encode(self, text):
        words = text.lower().strip().split()
        tokens = [" ".join(list(w)+ ["</w>"]) for w in words]

        for (first, second) in self.merge:
            new_tokens =[]
            for words in tokens:
                symbols = words.split()
                i=0
                merged_word =[]
                while i<len(symbols):
                    if i< len(symbols) -1 and symbols[i] == first and symbols[i+1] == second:
                        merged_word.append(first+second)
                        i += 2
                    else:
                        merged_word.append(symbols[i])
                        i+=1
                new_tokens.append(" ".join(merged_word))
                tokens = new_tokens

                ids = []
                for word in tokens:
                    for symbol in word.split():
                        if symbol in self.vocab:
                            ids.append(self.vocab[symbol])
                        else:
                
                            if symbol not in self.vocab:
                    
                                new_id = len(self.vocab)
                                self.vocab[symbol] = new_id
                                self.id2token[new_id] = symbol
                            ids.append(self.vocab[symbol])

                return ids

    def decode(self, ids):
        symbols = [self.id2token[i] for i in ids]
        text = "".join(symbols).replace("</w>"," ")
        return text.strip()






