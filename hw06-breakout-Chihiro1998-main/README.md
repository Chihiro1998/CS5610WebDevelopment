# hw-breakout

Extends [Finishing up](https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript/Finishing_up) in the MDN tutorial.

<hr>

### Exercises

Migrate the CSS and JavaScript 
from [lesson10.html](https://github.com/end3r/Gamedev-Canvas-workshop/blob/gh-pages/lesson10.html) to Observable Framework.

1. Remove the alert
2. Remove the code that reloads the page whenever a user wins or loses
3. Stop the game gracefully
4. Add the "Start game" button
5. Center the "Start game" button below the game
6. Use the button to start and restart the game
7. Make sure that you can quickly and repeatedly click the "startGame" button without affecting the game.
8. Display appropriate message on canvas when game ends
9. Depending on how you set things up, the paddle doesn't track the mouse -- there's an offset. Fix that bug.
10. DRY (Don't Repeat Yourself) -- use functions to minimize duplication of code.
  The instructor solution added ~30 lines of code.

<hr>

### Noteworthy

* For debugging, try [display()](https://observablehq.com/framework/javascript#display-value) instead of `console.log()`
* [Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
* [cancelAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/Window/cancelAnimationFrame)
* [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
* [getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) and
  [MouseEvent.clientX](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/clientX)
