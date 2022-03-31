from unittest import TestCase

from rugby_game import RugbyGame


class RugbyGameTest(TestCase):
    def test_init_game(self):
        game = RugbyGame("UBB", "Toulouse")

        assert game.get_score() == "0-0"

    def test_drop(self):
        game = RugbyGame("UBB", "Toulouse")
        game.drop("UBB")

        assert game.get_score() == "3-0"
        game.drop("Toulouse")
        assert game.get_score() == "3-3"

    def test_essai(self):
        game = RugbyGame("UBB", "Toulouse")
        game.essai("UBB")

        assert game.get_score() == "5-0"

    def test_transformation(self):
        game = RugbyGame("UBB", "Toulouse")
        game.essai("UBB")

        game.transformation("UBB")

        assert game.get_score() == "7-0"

    def test_transformation_si_essai(self):
        game = RugbyGame("UBB", "Toulouse")
        game.drop("UBB")

        game.transformation("UBB")
        assert game.get_score() == "3-0"

        game.essai("UBB")
        game.transformation("UBB")

        assert game.get_score() == "7-0"