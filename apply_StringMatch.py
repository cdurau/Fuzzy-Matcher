# Application of StringMatch class, using default args
titlematch = StringMatch(source_titles, target_titles)
titlematch.tokenize()
match_df = titlematch.match()