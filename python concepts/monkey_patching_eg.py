# https://medium.com/@dsrao0712/what-is-monkey-patching-and-why-is-it-used-a757a2bb7b4f

# actual function
def get_delivery_partners_by_pincode(data, headers, session: Session):
    """ Fetches delivery partner data from the external microservice """
    # API Call to External Microservice
    response = requests.get(API_URL, headers=headers, params=data)
    if response.status_code != 200:
        raise APIException("Error Fetching Delivery Partner Data")
    return response.json()



# fake or substitute function
def fake_get_delivery_partners_by_pincode(data, headers, session: Session):
    """ Fake function that generates a dummy response """
    return {"delivery_partner_info": [{"name": "Dummy Delivery Partner", "phone": "123-456-7890"}]}

# Monkey patching the original function with the fake function
get_delivery_partners_by_pincode = fake_get_delivery_partners_by_pincode

def update_dp_info(session : Session):
    data = {}
    headers = {}

    fetch_dp_info = get_delivery_partners_by_pincode(data , headers, session)
    # Adding delivery partner info in Orders Table
    order = session.query(Order).filter_by(id == data.order_id).one()
    order.delivery_partner_info = fetch_dp_info.delivery_partner_info
    session.commit()