from AnimalGame.farm.animals import Cow
from AnimalGame.gamestructure import Player


def test_feed_cow():
    cow = Cow()
    player = Player()

    # Füttere die Kuh korrekt
    event = player.feed(cow, "grass")
    assert event.action == "feed"
    assert "Moo" in event.result

    # Falsches Futter
    event2 = player.feed(cow, "apple")
    assert "refuses" in event2.result
