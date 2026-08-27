import chess
board=chess.Board()
ikkemat=True
while ikkemat==True:
    print(board)
    print(board.legal_moves)
    trekk=input(str("hva trekk vil du gjøre her er all lovlig trekk "))
    board.push_san(trekk)
if board.is_checkmate==True:
    ikkemat=False
    print("spille er over")
    print(board)    