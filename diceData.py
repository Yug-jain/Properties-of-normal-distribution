import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
diceresult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
mean=sum(diceresult)/len(diceresult)
std_dev=statistics.stdev(diceresult)
median=statistics.median(diceresult)
mode=statistics.mode(diceresult)

print(mean)
print(median)
print(std_dev)
print(mode)

firststd_start,firststd_end=mean-std_dev, mean+std_dev
secondstd_start, secondstd_end=mean-(2*std_dev), mean+(2*std_dev)
thirdstd_start, thirdstd_end=mean-(3*std_dev), mean+(3*std_dev)
fig=ff.create_distplot([diceresult],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,0.17], mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[firststd_start,firststd_start],y=[0,0.17], mode="lines",name="STANDARD DEVIATION1"))
fig.add_trace(go.Scatter(x=[firststd_end, firststd_end],y=[0,0.17], mode="lines",name="STANDARD DEVIATION1"))
fig.add_trace(go.Scatter(x=[secondstd_start,secondstd_start],y=[0,0.17], mode="lines",name="STANDARD DEVIATION2"))
fig.add_trace(go.Scatter(x=[secondstd_end, secondstd_end],y=[0,0.17], mode="lines",name="STANDARD DEVIATION2"))
fig.show()

listofdatawithinstd1=[result for result in diceresult if result>firststd_start and result<firststd_end]
listofdatawithinstd2=[result for result in diceresult if result>secondstd_start and result<secondstd_end]
listofdatawithinstd3=[result for result in diceresult if result>thirdstd_start and result<thirdstd_end]
print("percentage of data that lies between first standard deviation is"+str((len(listofdatawithinstd1)*100/len(diceresult))))
print("percentage of data that lies between second standard deviation is"+str((len(listofdatawithinstd2)*100/len(diceresult))))
print("percentage of data that lies between third standard deviation is"+str((len(listofdatawithinstd3)*100/len(diceresult))))
