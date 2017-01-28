import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./key.json"
def run_quickstart():
    # [START language_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import language
	
    # Instantiates a client
    language_client = language.Client()

    # The text to analyze
    text = ("Jack's birthday party next Thursday")
    document = language_client.document_from_text(text)

    # Detects the sentiment of the text
    entities = document.analyze_entities()

    for entity in entities:
     print('=' * 20)
     print('         name: %s' % (entity.name,))
     print('         type: %s' % (entity.entity_type,))
     print('wikipedia_url: %s' % (entity.wikipedia_url,))
     print('     metadata: %s' % (entity.metadata,))
     print('     salience: %s' % (entity.salience,))
if __name__ == '__main__':
    run_quickstart()
