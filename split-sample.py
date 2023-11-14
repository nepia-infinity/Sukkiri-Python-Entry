from janome.tokenizer import Tokenizer

text = "PCの調子が悪いです。共有PCをお借りすることは可能でしょうか？"
tokens = Tokenizer().tokenize(text)

for token in tokens:
    if '名詞' in token.part_of_speech:
        # 単語のみを抽出する
        # print(token.surface)
        print(token)

    
    