

class tool(iso):
    def __init__(self):
        pass
'''
Tool Error Detection (TD) TD1, TD2, TD3
Tool Impact (TI) TI1, TI2
Tool Classification Level (TCL) TCL1, TCL2, TCL3
'''
def TDLevel():
    pass

#Determines if the tool impacts the source code or test code
'''
get_data_from_user()
data_processing()
get_recommendation()
TILevel()
'''

def getSourceContact(tool_type, ):
    #recommender()
    pass

def TILevel(source_contact = False, ):
    if source_contact == True:
        return 2
    else: return 1

def tclLevel(TD_level, TI_level):
    #check limits
    if TD_level > 3 or TD_level < 1: return -1 #Error
    if TI_level > 2 or TI_level < 1: return -1 #Error

    if(TI_level == 1):
        return 1 #TCL1
    else:
        if TD_level == 1: return 1 #TCL1
        elif TD_level == 2: return 2 #TCL2
        else: return 3 #TCL3
 