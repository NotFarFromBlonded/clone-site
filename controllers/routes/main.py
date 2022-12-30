from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    if at.Image26.onClick:
        if at.TextBox71.styles.color == '#666666':
            at.TextBox71.styles.height = '0px'
            at.TextBox71.styles.color = '#000000'
        else:
            at.TextBox71.styles.height = '100%'
            at.TextBox71.styles.color = '#666666'
    
    if at.Image33.onClick:
        if at.TextBox85.styles.color == '#666666':
            at.TextBox85.styles.height = '0px'
            at.TextBox85.styles.color = '#000000'
        else:
            at.TextBox85.styles.height = '100%'
            at.TextBox85.styles.color = '#666666'
    
    if at.Image34.onClick:
        if at.TextBox87.styles.color == '#666666':
            at.TextBox87.styles.height = '0px'
            at.TextBox87.styles.color = '#000000'
        else:
            at.TextBox87.styles.height = '100%'
            at.TextBox87.styles.color = '#666666'
    
    if at.Image35.onClick:
        if at.TextBox89.styles.color == '#666666':
            at.TextBox89.styles.height = '0px'
            at.TextBox89.styles.color = '#000000'
        else:
            at.TextBox89.styles.height = '100%'
            at.TextBox89.styles.color = '#666666'

    if at.Image39.onClick:
        if at.TextBox97.styles.color == '#666666':
            at.TextBox97.styles.height = '0px'
            at.TextBox97.styles.color = '#000000'
        else:
            at.TextBox97.styles.height = '100%'
            at.TextBox97.styles.color = '#666666'
    
    if at.Image38.onClick:
        if at.TextBox96.styles.color == '#666666':
            at.TextBox96.styles.height = '0px'
            at.TextBox96.styles.color = '#000000'
        else:
            at.TextBox96.styles.height = '100%'
            at.TextBox96.styles.color = '#666666'
    
    if at.Image37.onClick:
        if at.TextBox95.styles.color == '#666666':
            at.TextBox95.styles.height = '0px'
            at.TextBox95.styles.color = '#000000'
        else:
            at.TextBox95.styles.height = '100%'
            at.TextBox95.styles.color = '#666666'
    
    if at.Image36.onClick:
        if at.TextBox94.styles.color == '#666666':
            at.TextBox94.styles.height = '0px'
            at.TextBox94.styles.color = '#000000'
        else:
            at.TextBox94.styles.height = '100%'
            at.TextBox94.styles.color = '#666666'
    
    if at.Flex146.onClick or at.Flex150.onClick:
        if at.Div177.styles.display == 'inline-block':
            at.Div177.styles.display = 'none'
            at.Div127.styles.display = 'inline-block'
        else:
            at.Div177.styles.display = 'inline-block'
            at.Div127.styles.display = 'none'

    if at.Image100.onClick:
        if at.Div178.styles.display == 'block':
            at.Div178.styles.display = 'none'
        else:
            at.Div178.styles.display = 'block'