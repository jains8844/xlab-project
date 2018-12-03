from flask import Flask, render_template, request
import matplotlib
import os,datetime
matplotlib.use('Agg')
from matplotlib import pyplot as plt
app=Flask('__name__')
@app.route('/')
@app.route("/level2", methods=['GET', "POST"])
def level2():
	return render_template('main.html')

@app.route('/plotting', methods=['GET','POST'])
def plotting():
	if(request.method=='POST'):
		xaxis=request.form['xaxis']
		x_points=map(int, xaxis.split(','))
		yaxis=request.form['yaxis']
		y_points=map(int, yaxis.split(','))
		fig=plt.figure()
		ax=fig.add_subplot(111)
		s=request.form['titl']
		s1=request.form['xlabel']
		s2=request.form['ylabel']
		print s,s1,s2
		if(request.form['type']=='hist'):
			ax.hist(x_points, y_points, histtype='bar', rwidth=0.6, color='g')
		elif(request.form['type']=='bar'):
			ax.bar(x_points, y_points, width=0.5, color='b')
		elif(request.form['type']=='line'):
			ax.plot(x_points, y_points)
		elif(request.form['type']=='scatter'):
			ax.scatter(x_points, y_points)
		plt.title(s)
		plt.xlabel(s1)
		plt.ylabel(s2)
		s='static/level1'+str(datetime.datetime.now())[11:]+'.png'
		fig.savefig(s)
		return render_template('level2graph.html',string1=s)
	return
if __name__=='__main__':
	app.debug=True
	app.run(port=8080)