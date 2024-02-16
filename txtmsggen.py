"""
Module with web scraping and generation functions.
All functions here will be run in the main program main.py
Test script currently under development
Created by Tristan Golden on 9/7/20
"""
#https://pointpickup.com/control-panel/accounts/info/211831 account url example number at end changes account


def get_pup_partner(html):
    """function narrows search top only html with info on pickup partner"""
    substr = html[html.index('Pickup Partner')+19:]  # narrow search to pickup partner html not company
    #print(substr) #print for debugging
    substr = substr[:substr.index('<div>')]
    #print(substr) #print for debugging
    return substr

#TODO: consolidate the function below to a universal functionality and terminology so to reduce program size and improve efficiency
def find_drvr_name(html):
    """this function parses through the html to find the drivers name"""
    puppartner = get_pup_partner(html)
    substr = puppartner[puppartner.index('Full name'): puppartner.index('Email')] #narrow search to just the name line of html
    #print(substr) #print for debugging
    name = substr[substr.index('>')+1: substr.index('</a>')]
    #print(name) #print for debugging
    while(name[0] == ' ' or name[0] == '\n'):
        name = name[1:]
    #print(name) #print for debugging
    name = name.strip()
    return name

def get_client(html):
    """function narrows search top only html with info on company/client"""
    substr = html[html.index('Client') + 11:]  # narrow search to client/company html not the pickup partner
    # print(substr) #print for debugging
    substr = substr[:substr.index('<div>')]
    # print(substr) #print for debugging
    return substr

#TODO: consolidate the function below to a universal functionality and terminology so to reduce program size and improve efficiency
def find_company_name(html):
    """this function parses through the html to find the client/company info"""
    comp = get_client(html)
    substr = comp[comp.index('Full name'): comp.index('Email')]  # narrow search to just the name line of html
    # print(substr) #print for debugging
    cliname = substr[substr.index('>') + 1: substr.index('</a>')]
    # print(name) #print for debugging
    cliname = cliname.strip()
    return cliname

def get_ord_dets(html):
    """narrows the search to the order details"""
    substr = html[html.index('order_details_table') + len('order_details_table') + 2:]
    #print(substr) #print for debugging
    substr = substr[:substr.index('<br />')]
    return substr

def find_dist(html):
    """function grabs the distance of the order from the order details"""
    orderdets = get_ord_dets(html)
    dist = orderdets[orderdets.index('ord-col-2')+11:]
    dist = dist[:dist.index('</div>')]
    #print(dist) #print for debugging
    dist = dist.strip()
    return dist

def find_price(html):
    """function grabs the full cost of the order from the order details"""
    orderdets = get_ord_dets(html)
    price = orderdets[orderdets.index('ord-det-item ord-det-item-total total-cost') + 40:]
    #print(price) #print for debugging
    price = price[price.index('ord-col-3') + 11:]
    #print(price) #print for debugging
    price = price[:price.index('</div>')]
    #print(price) #print for debugging
    price = price.strip()
    return price

def get_route_dets(html):
    """this function narrows the search to the route details"""
    routedets = html[html.index('route_details_small'):]
    routedets = routedets[routedets.index('point-details'):]
    return routedets

def find_store_adrs(html):
    """this function grabs the details of the pickup point for the order"""
    pickup = get_route_dets(html)
    pickup = pickup[pickup.index('point-address'):]
    pickup = pickup[pickup.index('<h5>')+4: pickup.index('</h5>')]
    return pickup
def gen_unmrkd_pup(html):
    name = find_drvr_name(html)
    message = 'Hi ' + name + '. Just a friendly reminder from PPUP here.'+ \
              ' Remember to mark your points and completion in the app when you arrive at the various locations.'
    return message
def gen_no_geo_no_pup(html):
    name = find_drvr_name(html)
    message = 'Hi ' + name + '. Looks like you aren\'t pinging on your maps location services. Is everything all right?'
    +    ' Are you at the location to pick up the order? TEXT(Y/N)'
    return message

def gen_no_geo_no_doff(html):
    name = find_drvr_name(html)
    message = 'Hi ' + name +'. Looks like you aren\'t pinging on your maps location services. Is everything all right?'
    + 'Are you at the location to deliver the order? TEXT(Y/N)'
    return message

def gen_store_wait(html):
    name = find_drvr_name(html)
    message = 'Hey' + name + ', this is Point Pickup. It looks like you\'ve been waiting for your order for a while.' + \
            ' Are there delays at the store? If so would you like us to cancel the order so you can move on to \"better things\" like maybe another order?' + \
              'Or would you like to keep the order and wait for it. TEXT (Y/N)'
    return message
def gen_pub(html):
    name = input('Enter the Driver\'s name here: ')
    price = find_price(html)
    distance = find_dist(html)
    message = 'Hey ' + name + '! Point Pickup here. I\'ve got an order opportunity here at your local Walmart: only ' + distance + ' to deliver. Currently going for ' + price + '.'
    return message

# prints for "unit testing" the functions
# print(find_price(html))
# print(find_company_name(html))
# print(find_drvr_name(html))
# print(find_dist(html))
# print(find_store_adrs(html))

