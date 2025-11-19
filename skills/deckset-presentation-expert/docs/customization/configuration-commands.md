# Configuration commands

# Configuration commands

Use commands to configure your presentation settings. Commands can either be applied _globally_ — if put at the top of your Markdown file — or _per slide_ to set or override global settings. When using global configuration commands, make sure that there are _no line breaks_ between any other commands at the top of your markdown file.

## Scale content to fit the slide

At times you have to fit more content onto one slide than the default font sizes allow for.

Deckset comes with an option to auto-scale paragraph text, lists, and other body content down to fit onto the slide. To enable this behavior put the `autoscale: true` command at the top of your markdown file.

You may turn this on or off on an individual slide by declaring `[.autoscale: true]` or `[.autoscale: false]` on the respective slide.

## Build lists

In Presenter and Rehearsal mode, you may want list items to appear one by one. To achieve this with Deckset, use the `build-lists: true` command.

Please note that this only affects Presenter (and Rehearsal) mode.

You may turn this on or off on an individual slide by declaring `[.build-lists: true]` or `[.build-lists: false]` on the respective slide.

## Slide numbers

To add running slide numbers to your presentation use the `slidenumbers: true` command.

You may turn this on or off on an individual slide by declaring `[.slidenumbers: true]` or `[.slidenumbers: false]` on the respective slide.

To add the count of slides in your presentation, use the `slidecount: true` command. You may also turn this off on an individual slide by declaring `[.slidecount: true]` or `[.slidecount: false]` on the respective slide.

## Footers

To add a persistent footer to each slide of your presentation, use the `footer: My Footer content` command.

To override your global footer or to add a footer to a single slide, add `[.footer: A different footer]` to the respective slide.

You may turn off the footer on an individual slide by declaring `[.hide-footer]` on the respective slide.

## Slide transitions

In Presenter mode, you may want to transition between slides. To achieve this with Deckset, use the `slide-transition: true` command.

You can control the duration of the transition by passing in the value in seconds: `slide-transition: fade(0.3)`.

You may also use this command on a single slide, like so: `[.slide-transition: fade(0.3)]` or `[.slide-transition: false]`.

## Use headers as slide dividers

To automatically start a new slide with each header, use the `slide-dividers: #, ##, ###, ####` command and specify the header levels you would like to take into account.

Please note that this command can only be used globally, at the top of your Markdown file.

## Default code language

You can specify a default code language by adding it at the top of your Markdown file:
    
    
    code-language: Swift
    

## Store theme choice in document

Deckset does store the theme choice as metadata to the file. In some cases, this information can get lost, e.g. in version control systems or when sending the file via email.

To make sure the theme choice doesn’t get lost, you can use the following command, referencing any theme by its name: `theme: Fira`.

If you also want to specify the color choice, you can reference the number of the color swatch as it appears within Deckset e.g.:

`theme: Fira, 3`

Please note that this command can only be used globally, at the top of your Markdown file.

## Automatically fit headers

Deckset allows you to fit header to entire slide to get that signature font look. However repeating this for every slide might be a bit cumbersome. You can address that by using the `fit-header` command like so:
    
    
    fit-header: #, ##
    

Note that this only works as a global command and needs to be placed on top of your md file.

## Global Background Image

To apply a background image to every slide in your presentation, simply add the `background-image` command at the very top of your Markdown file:
    
    
    background-image: image2.jpg
    
    (rest of your content)