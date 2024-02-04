# 'subClassOf', 'parents', 'children', 'ancestors', and 'descendants'.

import requests
import pandas as pd


def search_terms(api_key, terms):
    search_url = "https://data.bioontology.org/search"
    all_details = {}
    for term in terms:
        params = {
            'q': term,
#            'page': 1,
        #     'include': 'synonym',
            'apikey': api_key
        }

        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            results = response.json()
            # Extract synonyms for each ontology
            details = {}
            for result in results['collection']:
                ontology = result['links']['ontology'].split('/')[-1]
                prefLabel_list = result.get('prefLabel',"")
                synonym_list = result.get('synonym', [])
                def_list = result.get('definition',[])

                details[ontology] = {
                    'term': term,
                    'prefLabel': prefLabel_list,
                    'synonym': synonym_list,
                    'definition': def_list,
                    'Ontology': ontology
                }
            all_details[term]=details
        else:
            all_details[term]= None

    # Convert details to a pandas DataFrame
    df_rows= []
    for term, ontologies in all_details.items():
         if ontologies:
              for ontology, data in ontologies.items():
                   df_rows.append(data)

    df = pd.DataFrame(df_rows)

    # Save DataFrame to an Excel file
    excel_filename = "ontology_details.xlsx"
    df.to_excel(excel_filename, index=False)

    return excel_filename
terms = [
    "Enemy release", "Exotic range", "Invasion success", "Biotic resistance", "Ecosystem",
    "Biodiversity", "Non-native species", "Genetic changes", "Energy allocation", "Growth",
    "Reproduction", "Defense mechanisms", "Specialist enemies", "Generalist enemies",
    "Phenotypic plasticity", "Native species", "Darwin's naturalization",
    "Richness of closely related species", "Islands", "Continental areas",
    "Ecological impacts", "Limiting similarity", "Propagule pressure", "Introduction events",
    "Disturbance", "Undisturbed ecosystems", "Invasional meltdown"
]

# Call the function with your API key and the list of terms
api_key = "1309478b-84ce-4247-ba81-8a794a568823"
excel_file = search_terms(api_key, terms)

#api_key = "1309478b-84ce-4247-ba81-8a794a568823"

#term = "Enemy release"
#synonyms = search_term(api_key, term)

#print(synonyms)
#if synonyms:
#    for ontology, synonym_list in synonyms.items():
#        print(f"Ontology: {ontology}, Synonyms: {', '.join(synonym_list)}")
#else:
#    print("No synonyms found for the term.")


#'prefLabel': 'enemy', 'synonym': ['natural enemy'], 'definition': ['An organism that is a predator, consumer, parasite, parasitoid or pathogen of another organism.'],
