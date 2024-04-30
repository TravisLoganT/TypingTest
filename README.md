# Speed Typing Test
## Description
The Speed Typing Test is a console-based application designed to help users improve their typing skills. It measures typing speed in words per minute (WPM) and provides immediate visual feedback on typing accuracy. The program randomly selects a line of text from a predefined file, and users must type the text as quickly and accurately as possible.
<img width="990" alt="image" src="https://github.com/TravisLoganT/TypingTest/assets/91529655/b5788612-a988-4263-a147-e223d40e3076">


## Features
- Random Text Generation: Each test randomly picks one line of text from writing_texts.txt, ensuring a variety of typing challenges.
- Real-Time Typing Feedback: Typed characters are immediately checked and displayed in different colors based on accuracy (green for correct, red for incorrect).
- WPM Calculation: The program calculates the words per minute dynamically, providing real-time performance metrics.
- Continuous Testing: After completing one test, users can start another immediately to practice continuously.
## Installation
### Prerequisites
- Python 3.x installed on your machine
- curses library (Note: Windows users might need to install Windows Curses to enable support for the curses module)
### Setup
1. Clone the repository or download the source code:
bash
```
git clone https://your-repository-url.git
cd speed-typing-test
```
2. If necessary, install windows-curses on Windows:
bash
```
pip install windows-curses
```
## Usage
To start the typing test, run the program from the terminal:

bash
```
python3 main.py
```
### Controls
- Typing: Simply type on your keyboard to match the displayed text.
- Backspace: Correct mistakes by pressing backspace to delete the last character.
- Esc Key: Press the Escape key anytime to exit the current test or the program.
## Configuration
To change the source text, edit the writing_texts.txt file and add any text lines you want to include in the test. Each line in the file represents a separate test.

## Contributions
Contributions to this project are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: git checkout -b your-branch-name.
3. Make your changes and commit them: git commit -am 'Add some feature'.
4. Push to the branch: git push origin your-branch-name.
5. Create a new Pull Request.
