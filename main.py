import semopy

data = semopy.examples.political_democracy.get_data()
mod = semopy.examples.political_democracy.get_model()
m = semopy.Model(mod)
m.fit(data)
g = semopy.semplot(m, "out/pd.png")
