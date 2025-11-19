# Custom theming

# Custom theming

Deckset 2.0 introduces customization options for slide styles directly within the user interface. In addition to these UI-based controls, you can apply fine-grained styling to individual slides using the customization commands outlined below. Note that command-based styles will always override any styles set in the UI.

## Text and Headers

To customize the look and feel of your text and headers, you may add customization commands to `text`, `text-emphasis`, `text-strong`, `header`, `header-emphasis`, `header-strong`, `slidenumber-style` and `footer-style` with the desired color, alignment, line-height, text-scale, font and capitalization.
    
    
    [.text: #000000, alignment(left|center|right), line-height(10), text-scale(2.0), kern(1), Avenir Next Regular]
    [.header: #FF0000, alignment(left|center|right), line-height(18), text-scale(3.0), Avenir Next Bold, capitalization(default|upper|title)]
    [.footer-style: #2F2F2F, alignment(left|center|right), line-height(8), text-scale(1.5), Avenir Next Regular]
    

We recommend using Mac’s native Font Book application to search for fonts.

## Background color

To customize the background color of your slide, you may use the following customization command:
    
    
    [.background-color: #FF0000]
    

## Lists

To customize your list styles, you may add customization commands for the list color, bullet-character, alignment and ordered and unordered bullet indent.
    
    
    [.list: #000000, bullet-character(Custom String), alignment(left|center|right), bullet-indent(40), ordered-bullet-indent(20)]
    

## Tables

To customize the style of your tables, you may use the following commands:
    
    
    [.table-separator: #000000, stroke-width(10)] 
    [.table: margin(5)]
    

## Code

Deckset automatically picks a random set of colors with high enough contrast against the chosen background color for your code. You may add customization commands for the line-height and font family.

For consistent styles between code blocks and to prevent palette regeneration, use seed number `42` for persistence.
    
    
    [.code: auto(42), Font Family Name, line-height(4.2)]
    

You can also control alpha code build-in by specifying following command:
    
    
    [.code: dimmed-opacity(0.2)]
    

## Footnotes

To customize the look and feel of footnotes, you may use the following commands:
    
    
    [.footnote: #000000, alignment(left|center|right), line-height(10), text-scale(2.0), Avenir Next Regular]
    

Style the horizontal ruler that separates the footnote from the slide content like so:
    
    
    [.footnote-separator: #001100, height(10), margin(12)]
    

## Formulas

To customize the style of formulas, you may use the following command:
    
    
    [.formula: text-scale(42), alignment(center), #ff0011]
    

## Quotes

To customize the style of quotes, you may use the following commands:
    
    
    [.quote: #000000, alignment(left|center|right), line-height(10), text-scale(2.0), Avenir Next Regular]
    

To customize the style of the quote’s author, use:
    
    
    [.quote-author: #000000, alignment(left|center|right), line-height(10), text-scale(2.0), Avenir Next Regular]
    

## Graphs

To customise style of Mermaid Graphs, you may use the following command:
    
    
    [.graph: #ffffff, #aaffff, #000000, dark-mode(false)]
    

## Store theme choice in document

Deckset does store the theme choice as metadata to the file. In some cases, this information can get lost, e.g. in version control systems or when sending the file via email.

To make sure the theme choice doesn’t get lost, you can use the following command `theme: Fira`.

If you also want to specify the color choice, you can reference the number of the color swatch as it appears within Deckset e.g.:

`theme: Fira, 3`

Please note that this command can only be used globally, at the top of your Markdown file.