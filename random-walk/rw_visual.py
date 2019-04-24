import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 不断模拟随机漫步
while True:
	# 创建一个实例，并绘制点
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	# 设置窗口尺寸
	plt.figure(dpi=128,figsize=(10,6))
	
	point_number = list(range(rw.num_points))
	
	plt.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,
	    edgecolor='none',s=1)
	
	# 突出起点和终点    
	plt.scatter(0,0,c='green',edgecolors='none',s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',
	    s=100)
	
	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	  
	plt.show()
	
	keep_running = input("Make another walk?(y/n):")
	if keep_running == 'n':
		break
