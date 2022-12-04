import panel as pn
from myst_nb import glue

pn.extension('plotly')

def gluePlotly(name,fig,**kwargs):
    """Wrap Plotly object with Panel and glue()"""
    return glue(name, pn.pane.Plotly(fig,**kwargs), display=False)