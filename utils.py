import uuid
import dialogflow
from google.api_core.exceptions import InvalidArgument

def detect_intent(project_id, text, session_id=str(uuid.uuid4()), language_code='en-US'):
    """
    Returns the result of detect intent with texts as inputs and analyzes the
    sentiment of the query text.
    Using the same `session_id` between requests allows continuation
    of the conversaion.
    """

    # SETUP
    session_client = dialogflow.SessionsClient()
    session_path = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session_path))

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    # Enable sentiment analysis
    sentiment_config = dialogflow.types.SentimentAnalysisRequestConfig(
        analyze_query_text_sentiment=True)

    # Set the query parameters with sentiment analysis
    query_params = dialogflow.types.QueryParameters(sentiment_analysis_request_config=sentiment_config)

    # Detect intent
    response = session_client.detect_intent(session=session_path, query_input=query_input,query_params=query_params)
    query_text = response.query_result.query_text
    detected_intent = response.query_result.intent.display_name
    detected_intent_confidence = response.query_result.intent_detection_confidence
    fulfillment_text = response.query_result.fulfillment_text

    print(fulfillment_text)
    print('Session id', session_id)
    return fulfillment_text
