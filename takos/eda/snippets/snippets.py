# dataframeのカラムについて、そのユニークごとのカウントを可視化する方法
country = df_train.country.value_counts().to_frame().reset_index().rename(columns = {'index':'country', 'country':'count'})

fig, ax = plt.subplots()
ax = sns.barplot(data = country.head(20), x = 'country', y = 'count')
ax.set_ylabel('No of Records')
ax.set_xlabel('Country')
plt.xticks(rotation = 90)
plt.show()
