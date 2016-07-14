import csv
with open('wdi.csv', 'rb') as f:
    reader = csv.reader(f)
    wid_data = list(reader)
	
	
gdp_cap = []
life_exp = []
pop=[]
col=[]
for r in w:
     gdp_cap.append(r[0]); life_exp.append(r[1]); pop.append(r[2]); col.append(r[3])

gdp_cap = map(float,gdp_cap); life_exp = map(float,life_exp); pop = map(float, pop);


plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])


plt.grid(True)

plt.show()
