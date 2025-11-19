

# 🚢 Sea Battle — Console Game in Python

A simple console version of the classic Sea Battle game.
The player and the bot take turns shooting until one side has no ships left.

⸻

🎮 Features

🟦 Game Board
	•	Grid size: 10 × 10
	•	Cell types:
	•	Empty: [_]
	•	Ship: [ # ]
	•	Hit: [%]
	•	Miss: [@]

⸻

🚢 Ship Placement
	•	Four single-deck ships per side
	•	Ships are placed randomly
	•	Rules:
	•	Ships cannot touch each other
	•	No diagonal adjacency

⸻

🎯 Player Turn
	•	Enter coordinates (0–9)
	•	Input validation prevents:
	•	Out-of-bounds shots
	•	Repeated shots
	•	Console feedback: Hit or Miss

⸻

🤖 Bot Turn
	•	Bot shoots randomly
	•	Avoids repeated shots
	•	Shows the result of the shot

⸻

🏆 End of Game

The game ends when one board reaches 0 ships.
The winner is printed to the console.

⸻

📊 Statistics

After every match, a line is added to stats.txt:

user 14
bot 22

Format: winner + number of turns

⸻


✨ About This Project

A beginner-friendly Python practice project using:
	•	loops
	•	lists
	•	conditions
	•	functions
	•	random
	•	file I/O

