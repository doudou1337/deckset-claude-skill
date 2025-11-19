# Code Blocks

# Code Blocks

## Syntax Highlighting

Use GitHub style fenced code blocks to specify the language.
    
    
    ```javascript
    $.ajax({
      url: "/api/getWeather",
      data: {
        zipcode: 97201
      },
      success: function( data ) {
        $( "#weather-temp" ).html( "**" + data + "** degrees" );
      }
    });
    ```
    

![Syntax Highlighting](../../img/slide-38.md.png)

## Highlight Lines of Code

To put the focus on specific lines of your code block, use the following command:
    
    
    [.code-highlight: 2]
    
    ```javascript
    $.ajax({
      url: "/api/getWeather",
      data: {
        zipcode: 97201
      },
      success: function( data ) {
        $( "#weather-temp" ).html( "**" + data + "** degrees" );
      }
    });
    ```
    

![Highlight line of code](../../img/highlight-single-loc.png)

You can also highlight a range of lines:
    
    
    [.code-highlight: 2, 6-8]
    
    ```javascript
    $.ajax({
      url: "/api/getWeather",
      data: {
        zipcode: 97201
      },
      success: function( data ) {
        $( "#weather-temp" ).html( "**" + data + "** degrees" );
      }
    });
    ```
    

![Highlight ranges](../../img/highlight-range-loc.png)

## Step through Highlighted Lines of Code

When presenting, you can step through multiple highlights incrementally. Place as many `[.code-highlight]` commands above a code block in the order you would like the lines of code to be highlighted when presenting.
    
    
    [.code-highlight: none]
    [.code-highlight: 2]
    [.code-highlight: 6-8]
    [.code-highlight: all]
    
    ```javascript
    $.ajax({
      url: "/api/getWeather",
      data: {
        zipcode: 97201
      },
      success: function( data ) {
        $( "#weather-temp" ).html( "**" + data + "** degrees" );
      }
    });
    ```
    

## Automatic Scaling

Don’t worry if your code is slightly too long. Deckset scales code blocks to fit automatically.
    
    
    ```ruby
    def establish_connection(spec = nil)
      spec     ||= DEFAULT_ENV.call.to_sym
      resolver =   ConnectionAdapters::ConnectionSpecification::Resolver.new configurations
      spec     =   resolver.spec(spec)
    
      unless respond_to?(spec.adapter_method)
        raise AdapterNotFound, "database configuration specifies nonexistent #{spec.config[:adapter]} adapter"
      end
    
      remove_connection
      connection_handler.establish_connection self, spec
    end
    ```
    

![Automatic Scaling](../../img/slide-39.md.png)

## Inline `code`

Use code within normal text by enclosing it in backticks.

For example: ``func map<A, B>(x: A?, f: A -> B) -> B?``

![Inline Code](../../img/slide-40.md.png)

## Code background

You can enable custom code background by customising one of existing themes using customisation menu:

![Inline Code](../../img/code-background.png)

This feature is currently unavailable from Markdown level. But please let us know if you’d like it to be configurable from Markdown level as well!