# added this comment for testing

import streamlit as st
import requests

st.header('**OpenMatch**')

match_type = st.sidebar.selectbox('Match Type', ('NCT ID', 'Disease',  'Patient'))

API_KEY = 'your API key here'
HEADERS = {'x-api-key': API_KEY}

# NCT ID
def get_site_trial(NCTID: str):

    v2_base_trials = 'https://clinicaltrialsapi.cancer.gov/api/v2/trials/'
    url = f'{v2_base_trials}{NCTID}'
    r = requests.get(url, headers=HEADERS)
    return r.json()


def trial_info(query):

    trial = get_site_trial(NCTID)

    nct_id = trial['nct_id']
    protocol_id = trial['protocol_id']
    ctep_id = trial['ctep_id']
    official_title = trial['official_title']
    brief_summary = trial['brief_summary']
    detail_description = trial['detail_description']
    st.write(f'NCT#: {nct_id}\n'
        f'\nProtocolID: {protocol_id}\n'
        f'\nCTEP#: {ctep_id}\n '
        f'\nOfficial Title: {official_title}\n' 
        f'\nSummary: {brief_summary}\n' 
        f'\nDescription: {detail_description}')

    structured_eligibility = trial['eligibility']['structured']
    gender = structured_eligibility['gender']
    min_age = structured_eligibility['min_age_in_years']
    max_age = structured_eligibility['max_age_in_years']
    st.write(f'\nGender: {gender}\n'
        f'\nMininum Age: {min_age}\n'
        f'\nMaximum Age: {max_age}\n')


    inclusion_criteria = []
    exclusion_criteria = []

    unstructured_eligibility = trial['eligibility']['unstructured']
    for item in unstructured_eligibility:
        if item['inclusion_indicator'] is True:
            inclusion_criteria.append(item['description'])
        elif item['inclusion_indicator'] is False:
            exclusion_criteria.append(item['description'])
    
    st.write('**Inclusion criteria:** ')
    for i in inclusion_criteria:
        st.write(f'\t{i}')
        
    st.write('**Exclusion criteria:** ')
    for i in exclusion_criteria:
        st.write(f'\t{i}')
    
    if not exclusion_criteria:
        st.write('Poorly formatted criteria. Consider manual curation.')

    return


# Disease search
def build_url(disease: str,
              keywords: str='',
              country: str='United States',
              status: str='Active',
              study_type: str='Treatment'          
             ) -> str:
    
    base_url = "https://clinicaltrialsapi.cancer.gov/api/v2/trials?"
    
    disease = f"diseases.name._fulltext={disease.replace(' ', '%20')}&"
    country = f"sites.org_country={country.replace(' ', '%20')}&"
    status = f"current_trial_status={status}&"
    study_type = f"primary_purpose={study_type}&"
    if not keywords:
        keywords = None
    else:
        keywords = f"keyword={keywords.replace(' ', '%20')}"

    url = f"{base_url}{disease}{country}{status}{study_type}{keywords}"

    return url


def disease_search(url):
    r = requests.get(url, headers=HEADERS)
    return r.json()

def search_results(disease_query):
    
    trials = disease_query['data']
    for trial in trials:
        nct_id = trial['nct_id']
        official_title = trial['official_title']

        inclusion_criteria = []
        exclusion_criteria = []

        unstructured_eligibility = trial['eligibility']['unstructured']
        for item in unstructured_eligibility:
            if item['inclusion_indicator'] is True:
                inclusion_criteria.append(item['description'])
            elif item['inclusion_indicator'] is False:
                exclusion_criteria.append(item['description'])


        st.markdown(f'[**{official_title}**](https://clinicaltrials.gov/ct2/show/{nct_id})')
        st.write('**Summary:**', trial['brief_summary'])
        st.write('**Inclusion criteria:**')
        
        for i in inclusion_criteria:
            st.write(f'\t{i}')

        st.write('**Exclusion criteria:**')
        if not exclusion_criteria:
            st.write('Poorly formatted criteria. Consider manual curation.')
        else:
            for i in exclusion_criteria:
                st.write(f'\t{i}')



# Patient search
def label_patient_search(pathology, oncology, imaging):
    pass



# NCTID search
if match_type == 'NCT ID':
    NCTID = st.sidebar.text_input('Enter NCT ID', value='NCT04039230')
    nct_button = st.sidebar.button('Search')
    if nct_button:
        trial_id = get_site_trial(NCTID)

        trial_info(trial_id)


#Disease search
elif match_type == 'Disease':
    disease = st.sidebar.text_input('Enter disease type', key='Disease')
    disease_button = st.sidebar.button('Search')
    if disease_button:
        url = build_url(disease=disease)
        disease_query = disease_search(url)
        search_results(disease_query)


#Patient search    
elif match_type == 'Patient': 
    st.sidebar.write('Copy and paste report text into boxes on the right -->')
    pathology = st.text_area('Pathology report', key='Pathology')
    note = st.text_area('Oncology note', key='Note')
    imaging = st.text_area('Imaging', key='Imaging')
    genetics = st.text_area('Genetics', key='Genetics')

    patient_button = st.button('Submit')
    if patient_button:
        st.write('**Pathology report:**', pathology)
        st.write('**Oncology note:**', note)
        st.write('**Imaging report:**', imaging)
        st.write('**Genetics report:**', genetics)
