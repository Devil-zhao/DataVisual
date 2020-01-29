import matplotlib.pyplot as plt 
from random_walk import RandomWalk
#创建一个RandomWalk实例,并将其包含的点全都绘制出
#只要程序处于活动状态，就不断模拟随机漫步
while True:
    rw=RandomWalk(50000)
    rw.fill_walk()

    #设置窗口的尺寸
    plt.figure(figsize=(10,6))

    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)

    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_xaxis().set_visible(False)
    plt.show()

    keep_running=input("进行下一次模拟?(y/n)")
    if keep_running=='n':
        break