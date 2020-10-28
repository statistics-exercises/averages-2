# Arbitrary uniform random variables

In the previous exercise, you generated a uniform random variable that lay between 0 and 1.  This variable was a sample from ![](https://render.githubusercontent.com/render/math?math=U(0,1)).  To complete this exercise you will need to write a function to generate uniform random variables from ![](https://render.githubusercontent.com/render/math?math=U(a,b)).  In other words, we want a uniform random variable is greater than a and less than b.  It is very straightforward to generate such a random variable if we know how to generate a random variable from ![](https://render.githubusercontent.com/render/math?math=U(0,1)).  We simply need to generate a sample from ![](https://render.githubusercontent.com/render/math?math=U(0,1)) and then perform the following transformation:

![](https://render.githubusercontent.com/render/math?math=U(a,b)=a%2B(b-a)U(0,1))

 The number output here is (obviously) a uniform random variable that lies between a and b.

__To complete the exercise you thus need to complete the function called `uniform`__.  This function takes two arguments; namely, the `a` and `b` parameters that are introduced above.  It should `return` a uniform random variable between `a` and `b`.  

Once your code is complete a graph will be generated with samples from four different uniform distributions.  You should be able to see from this graph how by adjusting the `a` and `b` parameters in the expression above we can adjust the position of the centre of the distribution as well as the spread of the data. 
