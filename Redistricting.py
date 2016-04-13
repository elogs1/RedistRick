'''
Start of Toolbox Initialization for Redistricting Project
'''
import arcpy
import os

from arcpy import env


class Toolbox(object):

    '''
        Defines the information shown in the ArcToolbox.
    '''
    def __init__(self):
        '''
            Define the toolbox (the name of the toolbox is the name of the
            .pyt file).
        '''
        self.label = 'Toolbox'
        self.alias = ''
        # List of tool classes associated with this toolbox
        self.tools = [RedistRick]


class RedistRick(object):

    '''
        Boilerplate Python Toolbox Functions.
    '''
    def __init__(self):
        '''
            Define the tool (tool name is the name of the class).
        '''
        self.label = "Draw New Districts by Union"
        self.description = ("Uses a simple union and join to output a new "
                            "feature class of reformed polygon features")
        self.canRunInBackground = False

    def getParameterInfo(self):
        '''
            Define parameter definitions
        '''
        param0 = arcpy.Parameter(
	    displayName="Input Feature",
	    name="in_feature",
	    datatype="GPFeatureLayer",
	    parameterType="Required",
    	direction="Input")

        param1 = arcpy.Parameter(
        displayName="Record Set",
        name="record_set",
        datatype="GPFeatureRecordSetLayer",
        parameterType="Required",
        direction="Input")

	    """We will need this value to refer to the input layer(param0), right now I just have it hardcoded 
	    to the file I was going to choose in order to test"""
	    param1.value = 'Z:/5223/lab10/tl_2010_39049_tract10.shp'

	    params = [param0, param1]
	    return params

    def isLicensed(self):
        '''
            Set whether tool is licensed to execute.
        '''
        return True

    def updateParameters(self, parameters):
        '''
            Modify the values and properties of parameters before internal
            validation is performed.  This method is called whenever a
            parameter has been changed.
        '''
        return

    def updateMessages(self, parameters):
        '''
            Modify the messages created by internal validation for each tool
            parameter.  This method is called after internal validation.
        '''
        return

    def execute(self, parameters, messages):
        '''
            The source code of the tool.
        '''
        return

    # Toolbox Specific Functions

    '''
        Function takes layer and choosen attribute to group features off of.
        Returns a list of lists that includes the concatenated polygons.
    '''
    def groupby(self, attribute, condition):
        feature_class_list = []

        '''
            Implement an advanced join function and return a list of the new
            concatenated polygons.
        '''
        return feature_class

    '''
        Using an advanced algorithm concatenates adjacent polygon based on
        an attribute. Taking the mean across the total area. Combine to build
        features that meat the mean, within a user defined standard error.
    '''
    def equalDistribution(self):
        pass

    def split(self, quantity):
        pass

    '''
        Given a seed feature class cluster polygons to create equal areas
    '''
    def equalArea(self, seedArea):
        pass

    '''
    '''
    def naturalBoundaries():
        pass


class DescribeDistricts(object):
    def __init__(self):
        pass
