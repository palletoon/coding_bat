# monkey_trouble

[Original Problem](https://codingbat.com/prob/p120546)

We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

```python
monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
```

## Project Log

This project was completed much faster than the first one because I was able to use what I learned from the previous exercise. I was able to get my code even shorter because I realized that I could just return the result of the Boolean expression rather than returning explicit `True` or `False`.
