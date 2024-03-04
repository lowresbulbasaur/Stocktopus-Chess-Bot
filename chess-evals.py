import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from google.colab import drive
drive.mount('/content/drive')
path = "/content/drive/My Drive/Stocktopi Secret Sauce/chessDataProcessed.csv"

!pip install python-chess==0.31.3
!chmod 755 -R '/content/drive/My Drive/Stocktopi Secret Sauce/stockfish/stockfish_14.1_linux_x64_bmi2'

import chess
import chess.engine

# this function turns a FEN string into a board
def get_board(fen):
  return chess.Board(fen)

# this function returns the stockfish eval of the board
# code modified from https://colab.research.google.com/drive/1GSeBQdyZH_nHvl52XW0uhXV3Cslho24O#scrollTo=QauvWk2MkddY
def stockfish(board, depth):
  stockfish_path = r'/content/drive/My Drive/Stocktopi Secret Sauce/stockfish/stockfish_14.1_linux_x64_bmi2'
  with chess.engine.SimpleEngine.popen_uci(stockfish_path) as sf:
    result = sf.analyse(board, chess.engine.Limit(depth=depth))
    score = result['score'].white().score()
    return score

test = get_board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
print(test)
print(stockfish(test, 0))