import streamlit as st
import random

# Initialize board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Check winner
def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# AI move
def ai_move(board):
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty:
        i, j = random.choice(empty)
        board[i][j] = "O"

# Reset
def reset_game():
    st.session_state.board = initialize_board()
    st.session_state.game_over = False
    st.session_state.result = ""
    st.session_state.should_rerun = True

# Main
def main():
    st.title("🎮 Tic-Tac-Toe - AI vs You")

    if "board" not in st.session_state:
        st.session_state.board = initialize_board()
        st.session_state.game_over = False
        st.session_state.result = ""

    board = st.session_state.board

    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            key = f"cell_{i}_{j}"
            if cols[j].button(board[i][j] if board[i][j] != " " else " ", key=key, use_container_width=True):
                if board[i][j] == " " and not st.session_state.game_over:
                    board[i][j] = "X"

                    if check_winner(board, "X"):
                        st.session_state.result = "🎉 You win!"
                        st.session_state.game_over = True

                    elif is_draw(board):
                        st.session_state.result = "😐 It's a draw!"
                        st.session_state.game_over = True

                    else:
                        ai_move(board)

                        if check_winner(board, "O"):
                            st.session_state.result = "💻 AI wins!"
                            st.session_state.game_over = True

                        elif is_draw(board):
                            st.session_state.result = "😐 It's a draw!"
                            st.session_state.game_over = True

    # 🟢 Show result if game over
    if st.session_state.get("result"):
        if "win" in st.session_state.result.lower():
            st.success(st.session_state.result)
        elif "draw" in st.session_state.result.lower():
            st.info(st.session_state.result)
        elif "ai" in st.session_state.result.lower():
            st.error(st.session_state.result)

    if st.session_state.game_over:
        st.button("🔄 Play Again", on_click=reset_game)

    if st.session_state.get("should_rerun", False):
        st.session_state.should_rerun = False
        st.rerun()

if __name__ == "__main__":
    main()
