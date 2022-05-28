import pytest
from game_server_rolling_backup.main import convert_to_seconds


def test_convert_to_seconds_pass():
    assert 1 == convert_to_seconds('1s')
    assert 60 == convert_to_seconds('1m')
    assert 7200 == convert_to_seconds('2h')
    assert 172800 == convert_to_seconds('2d')
    assert 604800 == convert_to_seconds('1w')


@pytest.mark.xfail
def test_convert_to_seconds_fail():
    convert_to_seconds('1')
