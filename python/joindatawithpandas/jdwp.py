sequel table:
1. id
2. title
3. sequel

merge a table to itself to see the sequel between sequel (right table) and the id (left table)


original_sequels = sequels.merge(sequels, left_on='sequel', right='id', suffixes=('_org','_seq'))

print(original_sequels[,['title_org','title_seq']].head())

<<<<< self merge with left join

original_sequels = sequels.merge(sequels, left_on='sequel', right='id', how='left', suffixes=('_org','_seq'))

self merge
1. hierarchical relationships
2. sequential relationships
3. graph data

>>>>Samples

# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', suffixes=('_dir','_crew'))

# Create a Boolean index to select the appropriate
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
     (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

print(direct_crews.head())

>>>>>sample >> left join

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings,on="id", how="left")

# Print the first few rows of movies_ratings
print(movies_ratings.head())


>>>>Sample >>> merge on self

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']
titles_diff = orig_seq[['title_org','title_seq','diff']]
print(titles_diff.sort_values(by=['title_org','diff']).head())

