class Player:
    def __init__(self, username):
        if not (2 <= len(username) <= 16):
            raise ValueError("Username must be between 2 and 16 characters long")
        self._username = username
        self._results = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters long")
        self._username = value

    def add_result(self, result):
        self._results.append(result)

    def results(self):
        return self._results

    def games_played(self):
        return list({result.game for result in self._results})

    def played_game(self, game):
        return any(result.game == game for result in self._results)

    def num_times_played(self, game):
        return sum(1 for result in self._results if result.game == game)


class Game:
    def __init__(self, title):
        if not title:
            raise ValueError("Title cannot be empty")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot modify the title")

    def add_result(self, result):
        self._results.append(result)

    def results(self):
        return [result for result in self._results if result.game == self]

    def players(self):
        return list({result.player for result in self._results if result.game == self})

    def average_score(self, player):
        scores = [result.score for result in self._results if result.player == player]
        return sum(scores) / len(scores) if scores else 0


class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000")
        self._score = score
        self.player = player
        self.game = game
        game.add_result(self)
        player.add_result(self)
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        raise AttributeError("Cannot modify the score")
