# 🎮 Tic-Tac-Toe - AI vs You

Welcome to the **Tic-Tac-Toe** game where you can play against an AI! The goal is simple: get three of your marks in a row to win. Play on a 3x3 board and try to outsmart the AI!

## 📝 Features:
- **2 Players Mode**: You play as "X" and the AI plays as "O".
- **Winner Detection**: The game will notify you if you win, if it’s a draw, or if the AI wins.
- **Game Reset**: Start a new game easily with the reset button.

## 🚀 How to Run

1. **Install Streamlit**:
   To run the Tic-Tac-Toe app, you need to install Streamlit if you haven't already:

   ```bash
   pip install streamlit
🎨 App Interface
User Interface: The board is a simple 3x3 grid where you can click the empty spaces to place your "X".

AI Move: The AI makes its move after you play. The AI uses a random choice for its moves.

Result Notifications: Once the game ends, you will see a message informing you of the result:

"🎉 You win!"

"💻 AI wins!"

"😐 It's a draw!"

⚙️ Code Breakdown
1. Game Logic:
Board Initialization: The game board is a 3x3 grid initialized with empty spaces.

Winner Check: After every move, we check if the current player (either "X" or "O") has won.

Draw Check: If all spaces are filled and there is no winner, it’s a draw.

2. AI Move:
The AI randomly chooses an available cell to make its move. It will play as "O".

3. Resetting the Game:
The game can be reset by clicking the "🔄 Play Again" button, which will clear the board and start a new game.
💡 Contributing
Feel free to fork this repository and submit your pull requests for improvements, bug fixes, or new features.

If you have an idea to make the AI smarter or add difficulty levels, please share your thoughts!

📄 License
This project is open-source and available under the MIT License.

🧑‍💻 Tech Stack
Python: For backend logic.

Streamlit: For building the user interface.

Random Module: To simulate the AI's moves.

🤖 Try to Beat the AI!
Can you outsmart the AI and win the game? Play now and see if you can be victorious in Tic-Tac-Toe!
