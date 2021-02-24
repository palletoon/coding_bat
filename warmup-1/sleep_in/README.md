# sleep_in

[Original Probelm](https://codingbat.com/prob/p173401)

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

## Project Log

To start out, I made a very long version of this program that looked like this:

```python
def sleep_in(weekday, vacation):
    if weekday == True:
        if vacation == True:
            return True
        else:
            return False
    else:
        if vacation == True:
            return True
        else:
            return True
```

I realized that the program ALWAYS output `True` except in one case, and that I could shorten the program if I reorganized and combine the variable chekcs to focus on the `False` case. My second version of the code looked like this:
```python
def sleep_in(weekday, vacation):
    if weekday == True and vacation == False:
        return False
    else:
        return True
```
```python
def sleep_in(weekday, vacation):
    if weekday and vacation == False
        return False
    else:
        return True
```

Then I tried to update the `if` statement to read `if weekday and not vacation:` but I found that python didn't like that because it didn't know that the `weekday` and `vacation` variables were always going to be boolean (i.e., Ture/False) values. So I remembered that there's a new feature in python called [type hinting](https://docs.pytest.org/en/stable/contributing.html?highlight=type%20hinting) that will allow me to tell python what kind of parameters the function expects. Here's the next version of my code:

```python
def sleep_in(weekday: bool, vacation: bool):
    if weekday and not vacation:
        return False
    else:
        return True 
```

Finally, I remembered that I could use the shorthand "ternary" syntax for the if/then statement to get my code down to a single line:

```python
def sleep_in(weekday, vacation):
    return False if weekday and not vacation else True
```

Overall, I'm really pleased with how this program evolved. I'm glad to know:

1. How to use type hinting effetively, and
2. Better how to use the ternary if/then statement