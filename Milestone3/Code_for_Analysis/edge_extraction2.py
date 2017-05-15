from pyspark import SparkContext
sc=SparkContext()

file1 = sc.textFile("D:\Softwares\spark\project\edges.txt")
file2 = file1.map(lambda x: ((x[1], x[2], {'weight':float(x[-1])})))
file2.saveAsTextFile("D:\Softwares\spark\project\output\edges2")
#file3 = file1.map(lambda x: (x[1]))
#file3.saveAsTextFile("D:\Softwares\spark\project\output\nodes")
print "done"
