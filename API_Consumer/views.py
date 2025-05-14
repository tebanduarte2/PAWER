from django.shortcuts import render
import requests

NFT_API_URL = 'pongan_aqui_la_url_de_la_api'  # Replace with the actual API URL

def consumeAPI():
    try:
        
        response = requests.get(NFT_API_URL)

        response.raise_for_status()

        nft_data = response.json()

        
        if isinstance(nft_data, dict) and 'name' in nft_data:
            return nft_data
        else:
            
            print(f"API returned data in unexpected format: {nft_data}")
            return None

    except requests.exceptions.RequestException as e:
        
        print(f"Error fetching NFT data from API: {e}")
        return None
    except ValueError as e:
        
        print(f"Error parsing NFT data JSON: {e}")
        return None

def nft_detail_view(request):
    nft_data = consumeAPI() 

    
    context = {
        'nft': nft_data, 
        'error_message': None }
    

    
    if nft_data is None:
        context['error_message'] = "Could not fetch NFT data from the API."

    
    return render(request, 'consumeAPI.html', context)

