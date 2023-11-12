from janome.tokenizer import Tokenizer

text = "テープを出す機械はどこにありますか？"
tokens = Tokenizer().tokenize(text)

for token in tokens:
    if '名詞' in token.part_of_speech:
        # 単語のみを抽出する
        print(token.surface)

    
    