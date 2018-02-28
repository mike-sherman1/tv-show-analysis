import numpy as np
import pandas as pd

#Steps 2 and 3
states = []
shows = []
viewers = []
arr = np.genfromtxt('tv-data.txt', dtype='str', delimiter=',')
print(arr)

#Steps 5 and 6 (I am not sure if I did this in the way you wanted: my states came out in a different order)
states = list(set(arr[:,0])) #I used the set() function to remove duplicates
shows = list(set(arr[:,1]))
viewers = arr[:,2]
print(states)
print(shows)
print(viewers)

#Steps 7 and 8
states = np.asarray(states)
shows = np.asarray(shows)
viewers = np.asarray(viewers)
print(states)
print(shows)
print(viewers)

#Steps 9 through 12
states.sort(axis=0)
shows.sort(axis=0)
viewers = viewers.astype(int)
x = np.sum(viewers)
print(states)
print(shows)
print(viewers)
print("Total viewers: " + str(x))

#Step 13
show_raw_stats = pd.DataFrame(0, index=shows, columns=states)
show_agg_stats = pd.DataFrame(0, index=shows, columns=['Max', 'Min', 'Totals', 'Percent'])

#Step 14
for row in arr:
	show_raw_stats.ix[row[1]][row[0]] += int(row[2])
	
#Step 15
	show_agg_stats['Max'] = show_raw_stats.max(axis=1)
show_agg_stats['Min'] = show_raw_stats.min(axis=1)
show_agg_stats['Totals'] = show_raw_stats.sum(axis=1)
show_agg_stats['Percent'] = show_agg_stats['Totals']/show_agg_stats['Totals'].sum()*100

#Steps 16 and 17
print(show_raw_stats)
print(show_agg_stats)
print("The show with the highest percentage is Game of Thrones.")
print("The show with the lowest percentage is Orange is the New Black.")
print("My favorite show from this list is Suits.") 