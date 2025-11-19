#🚢 Sea Battle — Console Game in Python

A simple console version of the classic Sea Battle game.
The player and the bot take turns shooting until one board has no ships left.

⸻

🎮 Features

🟦 Game Board
	•	Size: 10×10
	•	Cell types:
	•	Empty: [_]
	•	Ship: [ # ]
	•	Hit: [%]
	•	Miss: [@]

⸻

🚢 Ship Placement
	•	Each side gets four single-deck ships
	•	Ships are placed randomly
	•	Placement rules:
	•	Ships do not touch each other
	•	No diagonal adjacency

⸻

🎯 Player Turn
	•	Player enters coordinates (0–9)
	•	Input validation protects against:
	•	Out-of-bounds shots
	•	Repeated shots
	•	Console feedback: Hit or Miss

⸻

🤖 Bot Turn
	•	Bot shoots randomly
	•	Avoids repeated shots
	•	Shows its move result

⸻

🏆 End of Game

The game ends when one field has 0 ships remaining.
Winner is printed to the console.

⸻

📊 Statistics

After each match, statistics are appended to stats.txt in format:

user 14
bot 22

Where the number is how many turns the match lasted.

⸻

📁 Project Structure

sea_battle.py
stats.txt      # auto-created after first game


⸻

⭐️ About This Project

This project helps practice:
	•	loops
	•	conditions
	•	lists
	•	functions
	•	random module
	•	file I/O

 
