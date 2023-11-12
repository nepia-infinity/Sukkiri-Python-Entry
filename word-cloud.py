import nlplot

npt = nlplot.NLPlot('青巻紙赤巻紙黄巻紙', target_col='words')
nlp.wordcloud(
    max_words=100,
    max_font_size=250,
    colormap='tab20_r',
)
