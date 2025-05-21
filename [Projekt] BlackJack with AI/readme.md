# Documentation - Project BlackJack with AI
This is the main documentation for this project. For more detailed information on the AI responses of GPT-4o, please check the attached PDF conversation log.

## Project Task
> **Realisieren Sie ein Blackjack-Spiel in Python. Gehen Sie schrittweise vor, bitten Sie die KI
also erst einfach um das Programm und spezifizieren sie nach und nach (die Karten sollen
als Objekte realisiert werden, man soll um Spielgeld spielen können, usw.). Wenn Ihnen
das Programm noch nicht gefällt, lassen Sie es änden. Eigene Ideen sind natürlich auch
willkommen!**

## Information
- **Model used:** GPT-4o </br>
- **Time needed:** About 70 minutes

## Prompts & Comments (with matching commit)

### Prompt 1 – Commit: [`ca30916`](https://github.com/ClarkLiam/INF-Basis26/commit/ca30916) <span style="color:#2980ff">`ca30916`</span>
Intention to create an working basic game framework with as little input as possible </br>

> **Create a python game based on the classic blackjack casino game, with a proper card set.**

-> Appears to work, hit or stand have to be entered as entire word to work.

---

### Prompt 2 – Commit: [`411fb4a`](https://github.com/ClarkLiam/INF-Basis26/commit/411fb4a) <span style="color:#2980ff">`411fb4a`</span>
Intention to make 'hit' or 'stand' to 'h' and 's' for better gameflow, also trying to force the cards to be objects </br>

> **Using your working game file adjust the following: Make the playing cards objects and assign them the values needed, also change the hit or stand question to expect 'h' and 's' for hit and stand.**

-> Requested changes appear to be implemented correctly, game is still working as expected

---

### Prompt 3 – Commit: [`d4d64fb`](https://github.com/ClarkLiam/INF-Basis26/commit/d4d64fb) <span style="color:#2980ff">`d4d64fb`</span>
Intentiding to add the functionality of a more realistic scenario by adding a play again and a welcome message </br>

> **Now use the given code and add an welcoming message at the beginning of the game as well as an play again option after ending the complete round.**

-> Changes are working as expected

---

### Prompt 4 – Commit: [`b1e05cf`](https://github.com/ClarkLiam/INF-Basis26/commit/b1e05cf) <span style="color:#2980ff">`b1e05cf`</span>
Intention is to add the functionallity of playing for money (every player starts with 100$) </br>

> **Now add the functionality to play for in game money. every player should begin with 100$ and cannot deposit any more money if he has none left. If the player loses, he will lose his stake, if he wins he will get the doubled amount back, if the game is a tie, the gets back his stake. Also tell the player his current amount of money left and ask for the amount to gamble with in this round.**

-> GPT-4o automatically added a game over condition, incase the player has no money left; the requested changes seem to work fine

---

### Prompt 5 – Commit: [`1eb7d52`](https://github.com/ClarkLiam/INF-Basis26/commit/1eb7d52) <span style="color:#2980ff">`1eb7d52`</span>
Intention to make the game playable by multiple players, already forcing the use of classes </br>

> **Using the previous code, adjust the game to be playable by multiple players, by including a player class, with the name, balance and all other needed objects for a working game.**

-> Only asking for stake after displaying the players hand, everything else seems to work

---

### Prompt 6 – Commit: [`fd2f379`](https://github.com/ClarkLiam/INF-Basis26/commit/fd2f379) <span style="color:#2980ff">`fd2f379`</span>
Trying to fix the logic error mentioned in the comment to promt 5 </br>

> **The code you created includes an game order mistake, the system is asking for the players stake after showing him the dealers and the players hand, player ask all players to put in there stakes before starting the round**

-> Seems to have fixed the issue

## Code Check
Using GitHub Copilot (Model: GPT-4.1), the generated Code was checked for major mistakes in the code, as well as incorrect usage of functions and features. The check did not return any major issues.

## Final Results:
After these 6 prompts, the GPT-4o model seems to have created a well-running multiplayer Blackjack game.

## Notes
- GPT-4o seems to take a higher amount of time to refine and code, compared to other tools
- The system seems to forget parts of the rules and only ever implementet basic game rules
