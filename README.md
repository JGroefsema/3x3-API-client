# 3x3 API Client
An attempt at wrting a client for the FIBA 3x3 API.

## Usage
The scripts will rely on 2 text files in the same folder as the script itself. A file named 'apiKey.txt' which contains your API key and a file named 'eventId.txt' which contains the ID of the event you want data from. Run 'client.py' and 'gameId.py'. gameId.py will give ask you when it found a new game if you want to make that the game for which data is collected by client.py.

## Requirements
* Python 3
* Python websocket-client module

## Documentation
### Test environment
* Documentation: https://fiba-3x3-scores-uat.herokuapp.com/docs/TvFeedApiV3
* Reference client: https://fiba-3x3-scores-uat.herokuapp.com/api/ws/demo
* Score app: https://scores-uat.fiba3x3.com/

### Live environment
* Documentation: https://fiba-3x3-scores.herokuapp.com/docs/TvFeedApiV3
* Reference client: https://fiba-3x3-scores.herokuapp.com/api/ws/demo
* Score app: https://scores.fiba3x3.com/