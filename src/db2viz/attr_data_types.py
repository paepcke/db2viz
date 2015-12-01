### ===== DATA TYPES ===== (python data types)

# returns list of python data types of attributes in output
def getAttrDataTypes(output, numCols):
	example = output[0]
	return [type(example[i]) for i in range(numCols)]

def getAttrDataType(index):
	return type(attrDataTypes[index])

# returns list of values of attribute specified by index
def getAttrValues(output, index):
	return [row[index] for row in output]

# returns true if attribute at index is of type specified by datatype


### ===== ATTRIBUTE TYPES ===== (numerical/categorical data types)

# represents the type of an attribute
class AttrType:
	NUMERICAL = 'Numerical'
	CONTINUOUS = 'Continuous' #interval
	DISCRETE = 'Discrete'

	CATEGORICAL = 'Categorical'
	ORDINAL = 'Ordinal'
	NOMINAL = 'Nominal'

# returns the type of an attribute given the list of values
def getType(attr):
	dataType = type(attr[0])
	distinct_vals = set(attr)
	if dataType is str:
		if len(distinct_vals) > 100:
			return AttrType.ORDINAL # alphabetize?
		return AttrType.NOMINAL
	elif dataType is int:
		if len(distinct_vals) < 35:
			return AttrType.ORDINAL
		return AttrType.DISCRETE
	elif dataType is float:
		return AttrType.CONTINUOUS
	elif dataType is datetime:
		if len(distinct_vals) < 10:
			return AttrType.DISCRETE
		return AttrType.CONTINUOUS

# returns the type of an attribute given the attribute index
def getAttrType(output, index):
	return getType(getAttrValues(output, index))

# returns a list of attribute types of each attribute in output
def getAttrTypes(output, numCols):
	return [getAttrType(output, index) for index in range(numCols)]

# counts the number of the attributes of a given type from a list of attribute types
def countType(attrType):
	if attrType == AttrType.NUMERICAL:
		return attrTypes.count(AttrType.CONTINUOUS) + attrTypes.count(AttrType.DISCRETE)
	if attrType == AttrType.CATEGORICAL:
		return attrTypes.count(AttrType.ORDINAL) + attrTypes.count(AttrType.NOMINAL)
	return attrTypes.count(attrType)