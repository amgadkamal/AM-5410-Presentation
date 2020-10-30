'''
project to show different types of graphs using matplotlib, using stock market data.
BSSD 5410-Presentation/project.
Supervised by Dr. Jonathan Lee.
Documentation for matplotlib:https://matplotlib.org
Link helped me with Python swich case solutions:https://data-flair.training/blogs/python-switch-case/

'''
#import matplotlib
import matplotlib.pyplot as plt

#import numpy
import numpy as np

#linear chart function
def linear_chart(x,y,y2):
    plt.plot(x, y,label="Amazon")
    plt.plot(x, y2,label='Google')
    plt.legend(loc="upper center")
    return plt.show()
#end def linear_chart

#step chart function
def step_chart(x,y,y2):
    plt.step(x, y,label="Amazon")
    plt.step(x, y2,label='Google')
    plt.legend(loc="upper center")
    return  plt.show()
#end def step_chart

#bar chart function
def bar_chart(x,y,y2):
    plt.bar(x, y, align='edge', width=.1, label="Amazon")
    plt.bar(x, y2, align='center', width=.1, label='Google')
    plt.legend(loc="upper center")
    plt.legend(loc="upper center")
    return plt.show()
#end def bar_chart

#scatter chart function
def scatter_chart(x,y,y2):
    plt.scatter(x, y, 50,label="Amazon")
    plt.scatter(x, y2, 50,label='Google')
    plt.legend(loc="upper center")
    return plt.show()
#end def scatter_chart

def menu():
    #menus
    print("Choose graph type \n","linear \n","step \n","bar \n","scatter \n")
#end def menu

#choose a method for the graph type
class Switcher(object):
    def indirect(self, method_name):
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()

    def linear(self):
        return linear_chart

    def step(self):
        return step_chart

    def bar(self):
        return bar_chart

    def scatter(self):
        return scatter_chart
#end of class Switcher

#read data files
def read_file(name):
    with open(name) as f:
        lines = f.readlines()
        x = [line.split()[0] for line in lines]#date
        y = [line.split()[1] for line in lines]#volume
        for i in range(0, len(y)):
            y[i] = int(y[i])
    return y,x
#end of def read_file

#operation function
def operation(a,x,y,y2):
    s = Switcher()
    w = s.indirect(a)
    return w(x,y,y2)
#end def operation

#graphs specification
def graph_specs():
    plt.title("Stock Market")#title
    fig = plt.gcf()#size
    fig.set_size_inches(13, 6)
    plt.tick_params(labelsize=7);#tick paramter size
    plt.xlabel("Date")#x axis label
    plt.ylabel("Volume")#y axis label
    plt.yticks(np.arange(1000000, 12000000, 500000))#min,max,step for y axis
    plt.grid()#make grid
# end def graph_specs

#main function
def main():
    menu()#pint menu
    y=read_file("Amazon.txt")#read the first file
    y2=read_file("Google.txt")# read the second file
    while True:
     type = input() #input user
     graph_specs() #call specifications for graph
     graph= operation(type,y[1],y[0],y2[0]) # call operation function
     print(graph)# show graph
#end def main

if __name__ == '__main__':
     main()


