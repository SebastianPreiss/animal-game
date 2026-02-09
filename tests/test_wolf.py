from AnimalGame.farm.animals import Cow
from AnimalGame.wild.animals import Wolf


def test_wolf_eats_cow():
    cow = Cow()
    wolf = Wolf()

    assert cow.is_alive

    event = wolf.eat(cow)

    assert not cow.is_alive
    assert "devours" in event.result

    event2 = wolf.eat(cow)
    assert "already dead" in event2.result
