import requests
import json
from typing import Optional, List, Dict, Any

def fetch_gbif_occurrence_data(scientific_name: str, country: str = 'FI') -> Optional[List[Dict[str, Any]]]:
    """
    Fetches species occurrence data from the GBIF API.

    Args:
        scientific_name: The scientific name of the species (e.g., "Ursus arctos").
        country: The ISO country code to filter occurrences by (default is 'FI' for Finland).

    Returns:
        A list of occurrence records as dictionaries if successful, otherwise None.  Each dictionary
        represents a single occurrence record and contains fields like 'latitude', 'longitude',
        'scientificName', etc.

    Source:
        GBIF - Global Biodiversity Information Facility
        https://api.gbif.org/v1/occurrence/search
        DOI: 10.15468/dl.xxxxxxxx (Replace with actual DOI when available)
    """

    base_url = "https://api.gbif.org/v1/occurrence/search"
    params = {
        'scientificName': scientific_name,
        'country': country,
        'format': 'json',  # Explicitly request JSON format
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        if 'results' in data:
            return data['results']
        else:
            print(f"Warning: No results found for {scientific_name} in {country}.")
            return []  # Return empty list, not None, to indicate no matches
    except requests.exceptions.RequestException as e:
        print(f"Network error fetching data for {scientific_name}: {e}")
        return None
    except requests.exceptions.Timeout as e:
        print(f"Timeout error fetching data for {scientific_name}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON response for {scientific_name}: {e}")
        return None
