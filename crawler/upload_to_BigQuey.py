from creds.credentials import credentials, creds

def upload_to_BigQuery(data):
    '''
    Removes from list `raw_urls` the elements of list `trash_list`. An error is thrown if there is a connection problem.
    
    :param data: pandas DataFrame
    
    :return: no return.
    '''

    project_id = 'vini-project-379618'              
    dataset_id = 'coding_test_lima_consulting'
    table_id = 'bbc_news'
    destination_table = f'{dataset_id}.{table_id}'

    table_schema = [
            {'name': 'Headline', 'type': 'STRING'},
            {'name': 'Authors', 'type': 'STRING'},
            {'name': 'Publication_datetime', 'type': 'DATETIME'},
            {'name': 'Article', 'type': 'STRING'},
            {'name': 'URL', 'type': 'STRING'},
            {'name': 'Redirected_URL', 'type': 'STRING'}
    ]

    try:
        data.to_gbq(
            credentials=credentials(),
            destination_table=destination_table,
            if_exists='replace',
            project_id=project_id,
            table_schema=table_schema
        )
    except:
        ConnectionError(f'Error when trying to upload data to BigQuery')
