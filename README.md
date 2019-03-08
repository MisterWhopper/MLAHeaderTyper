# MLAHeaderTyper
A Python script that types a preformatted MLA header given a trigger word

This script takes full advantage of the amazing [Keyboard module by boppeh.](https://github.com/boppreh/keyboard) It will need to be installed as a prerequisite before running this script.

To run this script, simply use
    python3 MLAHeaderTyper.pyw

Or you can just double-click to run it on windows.

Using the default configuration, the trigger word for a header is "%mlaheader% "; you MUST spell it correctly AND hit the space key after doing so in order for the script to catch the word properly.

When you do type the trigger word, you'll be met with an output that looks like this:
   
    MisterWhopper
    <PROFESSOR NAME>
    <CLASS NAME>
    <CURRENT DATE> <- this will actually be the current date
                      
The other keyword by default is "%mlacitation% "; same deal with spelling and hitting the space key. This one simply types:

    (<AUTHOR>, <PAGE NUMBER>). 

This script was for my own ease of use, as I can never remember how to do a properly formatted MLA header (always forget is it date first, or teacher, or class, etc.)

Feel free to download this code and modify it anyway you like.
