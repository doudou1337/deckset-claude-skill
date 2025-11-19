# Presenter Notes

# Presenter Notes

## Using presenter notes

Deckset turns every paragraph that starts with a `^` into presenter notes and doesn’t show this text on the slides.

You’ll see these notes on the presenter display (with two screens connected) or by using the rehearsal mode.

To preview your presenter notes in the main application window, you can turn them on by selecting `Toggle Presenter Notes` from the `View` menu.

To start another presenter note paragraph, prefix it with a caret again. Deckset will automatically scale the notes down to fit onto the presenter display in case you have a lot of text.

Example:
    
    
    # My slide title
    
    ^ This is a presenter note.
    

![Presenter Notes](../../img/presenter-notes.png)

## Customize the display of presenter notes

To customize the style of presenter notes, in both Presenter and Rehearsal modes and in exported documents, you may use the `presenter-notes` command like so:

`presenter-notes: text-scale(2), alignment(left|right|center), Helvetica`

You may also use this command on a single slide, like so:

`[.presenter-notes: text-scale(2), alignment(left|right|center), Helvetica]`