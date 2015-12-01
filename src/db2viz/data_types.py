### ===== DATA TYPES ===== (python data types)

# returns list of python data types of attributes in output
def getAttrDataTypes(output, numCols):
	example = output[0]
	return [type(example[i]) for i in range(numCols)]

def getAttrDataType(index):
	return type(attrDataTypes[index])

# returns list of values of attribute specified by index
def getAttrValues(index):
	return [row[index] for row in output]

# returns true if attribute at index is of type specified by datatype