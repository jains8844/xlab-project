from flask import Flask, render_template, request
import matplotlib
import os,datetime
matplotlib.use('Agg')
from matplotlib import pyplot as plt
app=Flask('__name__')
@app.route('/')
@app.route("/level1", methods=['GET', "POST"])
def level1():
	return render_template('main.html')
@app.route('/level1graph', methods=['GET','POST'])
def level1_graph():
	if request.method=='POST':
		xaxis=request.form['xaxis']
		x_points=map(int, xaxis.split(','))
		yaxis=request.form['yaxis']
		y_points=map(int, yaxis.split(','))
		fig=plt.figure()
		ax=fig.add_subplot(111)
		ax.plot(x_points, y_points)
		s=request.form['titl']
		s1=request.form['xlabel']
		s2=request.form['ylabel']
		plt.title(s)
		plt.xlabel(s1)
		plt.ylabel(s2)
		s='static/level1'+str(datetime.datetime.now())[11:]+'.png'
		fig.savefig(s)
		return render_template('level1graph.html',string1=s)
	return
if __name__=='__main__':
	app.debug=True
	app.run(port=8080)
