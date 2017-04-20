from pyspark import SparkContext
from pyspark import SQLContext
from graphframes import GraphFrame

sc = SparkContext()
sqlContext = SQLContext(sc)

nodes = sqlContext.read.format("com.databricks.spark.csv").load("D:\Softwares\spark\project\graph_nodes.csv")
nodes = nodes.selectExpr("_c0 as id")
edges = sqlContext.read.format("com.databricks.spark.csv").load("D:\Softwares\spark\project\graph_edges.csv")
edges = edges.selectExpr("_c0 as src", "_c1 as dst", "_c2 as payment")

G = GraphFrame(nodes, edges)

print "In-Degree"
G.inDegrees.sort('inDegree', ascending=False).show()

print "Out-Degree"
G.outDegrees.sort('outDegree', ascending=False).show()

print "Vertex Degree"
G.degrees.sort('degree', ascending=False).show()

print "Triangle Count"
Results=G.triangleCount()
Results.select("id", "count").show()

print "Label Propagation"
G.labelPropagation(maxIter=10).show()

print "PageRank"
G.pageRank(resetProbability=0.15, tol=0.01).vertices.sort('pagerank', ascending=False).show()


print "ALL DONE"
