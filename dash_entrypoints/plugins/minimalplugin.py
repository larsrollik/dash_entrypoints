import dash


def plug(app):
    dash.minimal_plugin_attribute = {"test1": 1}
    print("DISCOVERED minimal plugin !")
