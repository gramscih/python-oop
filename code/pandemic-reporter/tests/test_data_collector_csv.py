
class MockResponse(object):
    def __init__(self):
        pass

    def reader(self):
        pass

    def __next__():
        pass
    

@path("data_collector_csv.csv.reader")
def test_csv_empty(mock_reader):
    mock_reader.return_value = MockResponse()
