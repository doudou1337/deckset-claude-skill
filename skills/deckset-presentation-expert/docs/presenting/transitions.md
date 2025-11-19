# Transitions

# Transitions

## Enabling transitions

When presenting, you may want to transition between slides. To achieve this with Deckset, use the `slide-transition: true` command.

## Transition styles

The following transition styles are available:

  * `fade` — fades between slide (default)
  * `fadeThroughColor(#000000)` — fades through a color, into the next slide. The color is passed as hex value in parentheses.
  * `push(horizontal|vertical|top|right|bottom|left)` — the next slide pushes the previous out of the viewport. Supports the use of `horizontal` and `vertical` parameters, which pushes slides from the right (or top respectively) when going forward and left (or bottom respectively) when going backwards in the presentation.
  * `move(horizontal|vertical|top|right|bottom|left)` — the next slide moves over the top of the previous slide. Supports the use of `horizontal` and `vertical` parameters, which moves slides from the right (or top respectively) when going forward and left (or bottom respectively) when going backwards in the presentation.
  * `reveal(horizontal|vertical|top|right|bottom|left)` — the next slide is revealed by moving the previous slide out of the viewport. Supports the use of `horizontal` and `vertical` parameters, which reveals slides from the right (or top respectively) when going forward and left (or bottom respectively) when going backwards in the presentation.

## Transition timing

You can control the duration of the transition by passing in the value in seconds: `slide-transition: fade(0.3)`.

## Transitions on individual slides

You may also use the transition command on a single slide, like so: `[.slide-transition: push(horizontal, 0.3)]` or `[.slide-transition: false]`.