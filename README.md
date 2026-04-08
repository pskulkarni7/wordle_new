Word Guessing Game (Python) — Project

A command-line Wordle-inspired game built in Python, demonstrating strong fundamentals in data validation, algorithm design, and modular programming.

This project highlights my ability to design user-centric applications, implement clean logic, and ensure code reliability through testing.

🚀 Project Overview
Developed a 5-letter word guessing game with real-time feedback
Implemented a scoring logic algorithm to evaluate guesses
Integrated file-based datasets for dynamic gameplay
Designed a modular and testable code structure
Added input validation and error handling for improved user experience
🛠️ Tech Stack
Language: Python
Concepts Used:
Functions & modular programming
File handling (read/write operations)
Input validation
Algorithm design
Testing & debugging
🎯 Key Features
🔤 Random word selection from dataset
✅ Input validation against a dictionary
💡 Intelligent feedback system:
X → Correct letter, correct position
? → Correct letter, wrong position
- → Letter not in word
🔁 6 attempts per game
📝 Game result logging for tracking performance
🧩 Core Logic (Scoring Algorithm)

The score_guess() function compares the guessed word with the target word:

score_guess("world", "hello")
# Output: [0, 1, 0, 2, 0]

✔ Demonstrates:

Iteration and conditional logic
String comparison techniques
Position-based evaluation
🧪 Testing Approach
Created a dedicated test_game() function
Covered:
Scoring logic validation
File reading correctness
Random word selection

✔ Ensures reliability and correctness of core functionality

📂 Project Structure
.
├── game.py
├── target_words.txt
├── all_words.txt
├── play_list.txt
└── README.md
▶️ How to Run
python game.py
🎮 Gameplay Flow
User enters name
Optional instructions displayed
System selects a random word
User has 6 attempts to guess
Feedback provided after each guess
Game result stored for tracking
📊 Skills Demonstrated

✔ Problem-solving & algorithm design
✔ Data validation & error handling
✔ Clean, modular coding practices
✔ File-based data processing
✔ Testing and debugging

💼 Relevance to Roles

This project is relevant for:

Data Analyst / Data Quality Roles
Data validation logic
Structured data handling
QA / Test Analyst Roles
Test case design
Edge case handling
Debugging mindset
Python Developer Roles
Core programming fundamentals
Modular design
⚠️ Improvements & Future Enhancements
Handle duplicate letter scoring more accurately
Replace CLI with GUI (Tkinter or Web App)
Add unit testing framework (pytest)
Store results in a database instead of text file
Remove debug print statements for production
📌 Key Takeaway

This project demonstrates my ability to:

Translate logic into working code
Build user-friendly applications
Ensure correctness through testing
Write clean and maintainable Python programs
👩‍💻 Author

Pallavi Kulkarni
Data Analyst | QA Specialist | Python Enthusiast
