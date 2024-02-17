*"Debugging is like being the detective in a crime movie where you are also the murderer."*
*Filipe Fortes*

​	We all know that debugging takes time. However, there are a few tricks to write our code in such a way, which will save us time debugging. This article will showcase 7 of those techniques. While the examples are in Python, most of the things mentioned here will apply to any programming language. The techniques are ordered by level of complexity and also from scope - from changes you can make in your code instantly, to more architectural patterns that help with debugging (and a lot more things).

## Separating expressions in different variables

​	The simplest thing to do to make our code more debugable is to separate different expressions and/or actions into separate variables. For example, we can have the following code:

```python
def calculate_based_on_user_input():
	user_input = parse_input(read_input())
	return calculate(user_input.number)
```

​	Let's imagine we have traced the bug to this function, called `calculate_based_on_user_input`. What it does, is reads some input from the user, parses it, takes a part of it (the attribute `number`), and then returns the result of some calculations on the specific part of the input. Where can the bug be? Is it in the reading of the input or it's parsing? Perhaps the bug is in the `calculate` function? Could it be in the attribute itself (in Python, attributes can be properties, which can have certain behaviors attached to them - just like functions/methods)?