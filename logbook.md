# Log Book

The main idea for this technical test is the creation or a RESTful API that could allow us to get fibonacci sequences in two different implementations and also an inverse function.

I choosed during the first days to do the project using Python and the Flask framework (The Flask-RESTful extension). This choice was based on the fact that I'm already familiar with flask so it was easy to pick up with the RESTful extension.

The project was divided into four levels:
 - Level 1 : A route for a basic fibonacci implementation.
 - Level 2 : A route for an implementation that stores called instances results in cache.
 - Level 3 : A route for a better performing implementation of fibonacci.
 - Level 4 : A different route for an inverse function that for an input k return the closest n that verifies k = fib(n).

I started by creating a minimal api that I was going to update every step.

 # Level 1 :
For the first level, I created a [basic fibonacci function](https://github.com/Amine-Sa/Fibonacci-API/blob/6169ee34fcd1eabeb74d29eec690635a217d2821/comon/util.py#L5). This function was called inside my fibonacci resource.
Route : /v1/fibonacci/basic/my_number

# Level 2 :
For the second level I prefered using the cache decorator already present in Python [functools library](https://docs.python.org/3/library/functools.html) which saves the results of my function [functools_fibonacci](https://github.com/Amine-Sa/Fibonacci-API/blob/6169ee34fcd1eabeb74d29eec690635a217d2821/comon/util.py#L12) calls. This implementation saves only the called instance and not the recursive calls.
Route : /v1/fibonacci/functools/my_number

# Level 3 :
At this level I used the Flask-Caching extension. Cache is managed through a Cache instance, I choosed a SimpleCache which uses a local python dictionary for caching with the instance call as a key and the results as the value.
The function [advanced_fibonacci](https://github.com/Amine-Sa/Fibonacci-API/blob/6169ee34fcd1eabeb74d29eec690635a217d2821/comon/util.py#L18) returns the cached results if the instance was already called, otherwise we calculate the value while saving every recursive call into our cache.
Route : /v1/fibonacci/advanced/my_number

# Level 4 :
For the final level I made an inverse function for the fibonacci series.
