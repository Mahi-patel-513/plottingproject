import matplotlib.pyplot as plt

y_views = [534,689,258,401,724,689,4045]
f_views = [123,342,700,304,405,650,6543]
t_views = [202,209,176,415,824,389,3987]
days = range(1,8)

plt.plot(days, y_views, label = 'Youtube Views', marker = 'o', markerfacecolor = 'b')
plt.plot(days, f_views, label = 'Facebook Views', marker = 'o', markerfacecolor = 'orange')
plt.plot(days, t_views, label = 'Twitter Views', marker = 'o', markerfacecolor = 'g')

#plt.plot(days, views, label = 'Youtube views', color = 'b', marker = 'o', markerfacecolor = 'r', linestyle = '-.')
plt.xlabel('Day')
plt.ylabel('Views')
plt.legend(loc = 'upper right')
plt.grid(True, linewidth = 1, linestyle = '-.')
#plt.xlim(1,5)
#plt.ylim(100,900)
plt.title('Daily views for marketing channels')
plt.show()
