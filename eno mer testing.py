import chess

board = chess.Board()
ikkemat = True

while ikkemat == True:
    print(board)
    print(board.legal_moves)
    trekk = input("Hva trekk vil du gjøre? Her er alle lovlige trekk: ")
    
    
    try:
        move = board.parse_san(trekk)
        board.push(move)
    except ValueError:
        print( board)
    
    if board.is_checkmate() == True:
        ikkemat = False
        print("spille er over")
        print(board)