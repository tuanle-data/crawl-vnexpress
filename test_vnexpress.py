from vnexpress import get_news, get_sports_news


def test_greater_than_zero():
    assert len(get_sports_news()) > 0

def test_type_of_result():
    assert type(get_sports_news()) == list

