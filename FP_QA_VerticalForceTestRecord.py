import matplotlib.pyplot as plt
import pandas as pd

#read the csv file and create pandas dataframe as 'df'
df =pd.read_csv('vertical_force_spotcheck_record.csv')

#convert date to datetime format
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

#add column for known load in Newtons
df['load_N']=df['mass_kg']*9.81

# Create columns for force outputs as percentage of known load
for column in df:
    #create 'percentage output' column for cols which contain 'FP' in column name
    if 'FP' in column:
        df[column+'_percent']=(df[column]/df['load_N'])*100 #percentage of known vertical load
        
'''
SET UP PLOT:  plot y, x , z force out percentages against date
'''
#create figure with 3 plots stacked vertically
fig, ax = plt.subplots(3, 1) 

#set overall figure title
fig.suptitle('Force Plates X,Y,Z Outputs as % of Static Vertical Load ')

#global figure settings
dashlinewidth=1
baselinewidth=0.5

colourFP1='blue' #colour each force plate's data appears on plots
colourFP2='green'
colourFP3='red'
colourFP4='gold'

markerstyle = 'o'
markersize = 3

#add baselines and dashed lines at +/- 2% of expected on each plot
ax[0].axhline(y = 100, linestyle = '-', color ='black', linewidth=baselinewidth)
ax[0].axhline(y = 102, linestyle = '--', color ='grey',linewidth=dashlinewidth)
ax[0].axhline(y = 98, linestyle = '--', color ='grey',linewidth=dashlinewidth)

for i in range (1,3):
    ax[i].axhline(y = 0, linestyle = '-', color ='black', linewidth=baselinewidth)
    ax[i].axhline(y = 2, linestyle = '--', color ='grey',linewidth=dashlinewidth)
    ax[i].axhline(y = -2, linestyle = '--', color ='grey',linewidth=dashlinewidth)

#set individual Y axis labels
ax[0].set_ylabel('Y out (%)')
ax[1].set_ylabel('X out (%)')
ax[2].set_ylabel('Z out (%)')

#set x axis label in bottom plot only as common to all plots
ax[2].set_xlabel('Test Date')

# add data to plot
x=df['date'] # x axis data, common to all plots

ax[0].plot(x,df['FP1y_percent'], marker = markerstyle, ms=markersize,color =colourFP1, label='Plate 1')#label = label to show on legend
ax[0].plot(x,df['FP2y_percent'], marker = markerstyle, ms=markersize,color =colourFP2, label='Plate 2')
ax[0].plot(x,df['FP3y_percent'], marker = markerstyle, ms=markersize,color =colourFP3, label='Plate 3')
ax[0].plot(x,df['FP4y_percent'], marker = markerstyle, ms=markersize,color =colourFP4, label='Plate 4')

ax[1].plot(x,df['FP1x_percent'], marker = markerstyle, ms=markersize,color =colourFP1)
ax[1].plot(x,df['FP2x_percent'], marker = markerstyle, ms=markersize,color =colourFP2)
ax[1].plot(x,df['FP3x_percent'], marker = markerstyle, ms=markersize,color =colourFP3)
ax[1].plot(x,df['FP4x_percent'], marker = markerstyle, ms=markersize,color =colourFP4)

ax[2].plot(x,df['FP1z_percent'], marker = markerstyle, ms=markersize,color =colourFP1)
ax[2].plot(x,df['FP2z_percent'], marker = markerstyle, ms=markersize,color =colourFP2)
ax[2].plot(x,df['FP3z_percent'], marker = markerstyle, ms=markersize,color =colourFP3)
ax[2].plot(x,df['FP4z_percent'], marker = markerstyle, ms=markersize,color =colourFP4)

#set y visible range on each axis
ax[0].set_ylim(97,103)
ax[1].set_ylim(-3,3)
ax[2].set_ylim(-3,3)


#set legend, listing horizontally and placing just above top plot
ax[0].legend( ncol=len(df.columns),bbox_to_anchor=(1,1.3)) #


plt.show()
