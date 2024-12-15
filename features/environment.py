from gurux_dlms_agent import DlmsAgent

def before_all(context):
    context.data = {}
    context.data['is connected'] = False
    context.data['dlms agent'] = DlmsAgent()
    context.data['obis value'] = "None"

def after_all(context):
    context.data['dlms agent'].disconnect()
    context.data['dlms agent'] = None