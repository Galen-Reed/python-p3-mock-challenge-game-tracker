class Game:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be of type str.")
        if len(title) == 0:
            raise ValueError("Title must be longer than 0 characters.")
        
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    def results(self):
        return self._results

    def players(self):
        return list({result.player for result in self._results})

    def average_score(self, player):
        if not isinstance(player, Player):
            raise TypeError("Player must be of type Player.")
        player_scores = [result.score for result in self.results() if result.player == player]
        return sum(player_scores) / len(player_scores) if player_scores else 0

class Player:
    def __init__(self, username):
        if not isinstance(username, str):
            raise TypeError("Username must be of type str.")
        if len(username) < 2 or len(username) > 16:
            raise ValueError("Username must be between 2 and 16 characters.")

        self._username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be of type str.")
        if not (2 <= len(value) <= 16):
            raise TypeError("Username must be between 2 and 16 characters.")
        self._username = value


    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)

class Result:

    all = []

    def __init__(self, player, game, score):
        if not isinstance(game, Game):
            raise TypeError("Game must be of type Game.")
        if not isinstance(player, Player):
            raise TypeError("Player must by of type Player.")
        if not isinstance(score, int):
            raise TypeError("Score must be a number.")
        if not (1 <= score <= 5000):
            raise ValueError("Score must be between 1 and 5000.")
        
        self._player = player
        self._game = game
        self._score = score

        game._results.append(self)
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @property
    def player(self):
        return self._player
    
    @property
    def game(self):
        return self._game
