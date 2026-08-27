import chess
import chess.pgn
board = chess.Board()
import zstandard
gre=("")


first_game = chess.pgn.read_game(gre)
print (first_game)