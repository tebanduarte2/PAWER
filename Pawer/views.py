from django.shortcuts import render
import requests
from django.conf import settings

def base_view(request):
    return render(request, 'base.html')

def search_address(address):
    """
    Uses LocationIQ Search API to find addresses.

    Args:
        address (str): The address string to search for.

    Returns:
        list or None: A list of dictionaries containing location data
                      if successful, otherwise None.
    """
    api_key = settings.LOCATIONIQ_API_KEY
    base_url = "https://us1.locationiq.com/v1/search.php"

    params = {
        'key': api_key,
        'q': address,
        'format': 'json',
        'limit': 5 # Optional: limit the number of results
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()

        if data and isinstance(data, list):
            return data # Return the list of results
        else:
            return None # Address not found or API returned unexpected result

    except requests.exceptions.RequestException as e:
        print(f"Error calling LocationIQ API: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing LocationIQ API response: {e}")
        return None
    
def contact_view(request):
    search_results = None
    query = None

    if request.method == 'GET':
        # Get the address query from the GET parameters
        query = request.GET.get('address_query')

        if query:
            # Call the search_address function with the user's query
            search_results = search_address(query)

    # Render the contact template, passing the search results and query
    return render(request, 'contact.html', {
        'search_results': search_results,
        'query': query
    })