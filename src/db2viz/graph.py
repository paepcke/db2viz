import matplotlib.pyplot as plt
import numpy as np
import collections
from attr_data_types import *


def create_chart(output, attr_names, display_attrs, display_type):
	print display_type

	if display_type == 'histogram':
		if len(display_attrs) == 1: 
			# long list of numbers, must consolidate
		    
		    points = getAttrValues(output, 0)
		    print points
		    """
		    try:
		        new_points = []
		        #for x in points:
		        #    y = x.encode('utf8')
		        #    new_points.append(float(y))
		        #    print float(y)
		        #points = [float(x.encode('utf8')) for x in points] #debug@home
		        new_points = [float(x) for x in points]
		    except ValueError, err:
		        print x # TODO: find the None!! check if it's the string 'None' # FOUND...
		        print err
		    """
		    counter = collections.Counter(points)

		    if len(counter) > 20: 
		    	#divide into buckets

		        numBuckets = 50 # TODO: give user control?
		        min_x = float(min(points))
		        max_x = float(max(points)) + 1
		        bins = np.arange(min_x, max_x)
		        freq, bins = np.histogram(points, bins=numBuckets)

		        categories = bins[1:] # this is probably wrong...
		        values = freq

		    else:
		        # use given datapoints as buckets

		        categories = counter.keys()
		        values = counter.values()

		    fig, ax = plt.subplots()

		    index = np.arange(len(categories))
		    bar_width = 0.9

		    rects = plt.bar(index, values, bar_width, color='g')
		    
		    plt.xlabel(attr_names[0])
		    plt.ylabel('count')
		    plt.title(attr_names[0])
		    plt.xticks(index + bar_width, categories)

		    plt.show()

		elif len(display_attrs) == 2:
			# pairs (x, count(x)) already given - simply plot as bar_graph

		    categories = getAttrValues(output, 0)
		    values = getAttrValues(output, 1)

		    fig, ax = plt.subplots()

		    index = np.arange(len(categories))
		    bar_width = 0.9

		    rects = plt.bar(index, values, bar_width, color='g')
		    
		    plt.xlabel(attr_names[0])
		    plt.ylabel(attr_names[1])
		    plt.title(attr_names[1] + ' vs. ' + attr_names[0])
		    plt.xticks(index + bar_width, categories)

		    plt.show()

		else:
			print 'Cannot plot more than three attributes in histogram'


	elif display_type == 'barchart':

		if len(display_attrs) == 1: 
			print 'Please provide bar labels or values'

		elif len(display_attrs) == 2:
		    categories = getAttrValues(output, 0)
		    values = getAttrValues(output, 1)

		    fig, ax = plt.subplots()

		    index = np.arange(len(categories))
		    bar_width = 0.9

		    rects = plt.bar(index, values, bar_width, color='g')
		    
		    plt.xlabel(attr_names[0])
		    plt.ylabel(attr_names[1])
		    plt.title(attr_names[1] + ' vs. ' + attr_names[0])
		    plt.xticks(index + bar_width, categories)

		    plt.show()

	elif display_type == 'scatterplot':

		if len(display_attrs) == 1:
			print 'make 1d scatterplot!! (with box and whiskers)'

		elif len(display_attrs) == 2:
		    x = getAttrValues(output, 0)
		    y = getAttrValues(output, 1)
		    plt.plot(x, y, 'x')
		    plt.xlabel(attr_names[0])
		    plt.ylabel(attr_names[1])
		    plt.title(attr_names[1] + ' vs. ' + attr_names[0])
		    plt.show()

	elif display_type == 'lineplot':

		if len(display_attrs) == 2:
		    x = getAttrValues(output, 0)
		    y = getAttrValues(output, 1)
		    plt.plot(x, y, 'x', linewidth = 2)
		    plt.xlabel(attr_names[0])
		    plt.ylabel(attr_names[1])
		    plt.title(attr_names[1] + ' vs. ' + attr_names[0])
		    plt.show()
		    # line of best fit?

		else:
			print 'need at least 2 dimensions for lineplot' #3d?

	elif display_type == 'area':

		if len(display_attrs) == 2:
			x = getAttrValues(output, 0)
			y = getAttrValues(output, 1)
			plt.plot(x, y, 'x', linewidth = 2)
			plt.xlabel(attr_names[0])
			plt.ylabel(attr_names[1])
			plt.title(attr_names[1] + ' vs. ' + attr_names[0])
			plt.show()

		else:
			print 'need at least 2 dimensions for area curve' #3d?

	elif display_type == 'boxplot':

		if len(display_attrs) == 1:
			print 'make 1d plot with box and whiskers'

#plt.savefig('chart.png')
