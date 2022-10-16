import tictactoe as ttt

board = ttt.initial_state()
best_action = ttt.minimax(board)

print(best_action)
print(ttt.result(board, best_action))
# 551242 calls to max_value + min_value - 1 cache key - AI starts (1st move)
# ~59705 - 9 cache keys - Human starts (2nd move)
# ~8104 - 8 cache keys (AI always start in the same position, 8 possibles slots for the human) - AI start, Humans take their turn (3rd move)
# ~1285 - 9*1(already cached)*7=63 cache keys - Humans start - AI - Humans again (4th move)

# with 1+9+8+63=81 cache keys we would save us 551242+8104=559.346 calls to the max_value and min_value functions per game if AI takes the first move or 59705+1285=60.990 calls if Humans start.
