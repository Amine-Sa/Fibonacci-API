# Log Book

The main idea for this technical test is the creation or a RESTful API that could allow us to get fibonacci sequences in two different implementations and also an inverse function.

I choosed during the first days to do the project using Python and the Flask framework (The Flask-RESTful extension). This choice was based on the fact that I'm already familiar with flask so it was easy to pick up with the RESTful extension.

The project was divided into four levels:
 - Level 1 : A route for a basic fibonacci implementation.
 - Level 2 : A route for an implementation that stores called instances results in cache.
 - Level 3 : A route for a better performing implementation of fibonacci.
 - Level 4 : A different route for an inverse function that for an input k returns the closest n that verifies k = fib(n).

**I started by creating a minimal api that I was going to update every step.**

 ## Level 1 :
For the first level, I created a [basic fibonacci function](https://github.com/Amine-Sa/Fibonacci-API/blob/6169ee34fcd1eabeb74d29eec690635a217d2821/comon/util.py#L5). This function was called inside my fibonacci resource.

Route : `/v1/fibonacci/basic/my_number`

 ## Level 2 :
For the second level I prefered using the cache decorator already present in Python [functools library](https://docs.python.org/3/library/functools.html) which saves the results of my function [functools_fibonacci](https://github.com/Amine-Sa/Fibonacci-API/blob/6169ee34fcd1eabeb74d29eec690635a217d2821/comon/util.py#L12) calls. This implementation saves only the called instance and not the recursive calls.

Route : `/v1/fibonacci/functools/my_number`

 ## Level 3 :
At this level I used the Flask-Caching extension. Cache is managed through a Cache instance, I choosed a SimpleCache which uses a local python dictionary for caching with the instance call as a key and the results as the value.
The function [advanced_fibonacci](https://github.com/Amine-Sa/Fibonacci-API/blob/6169ee34fcd1eabeb74d29eec690635a217d2821/comon/util.py#L18) returns the cached results if the instance was already called, otherwise we calculate the value while saving every recursive call into our cache.

Route : `/v1/fibonacci/advanced/my_number`

 ## Level 4 :
For the final level I made an inverse function for the fibonacci series. The function was based on the [Binet's formula](https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula) which gives us an easy inverting function [reverse_fibonacci](https://github.com/Amine-Sa/Fibonacci-API/blob/2d0546584ca21aef8233bf233a1e765302adabc6/comon/util.py#L28).

Route : `/v1/reverse-fibonacci/k`

**After implementing functions, creating and adding resources to my application, I updated the structure of my project to a structure that scales easily with largest projects and maintains an organised layout.**  
**Here is my final structure : **
```
├── app.py  
├── comon  
│   ├── __init__.py  
│   └── util.py  
├── resources  
│   ├── advanced.py  
│   ├── basic.py  
│   ├── funcache.py  
│   ├── __init__.py  
│   └── reversed.py  
└── tests  
    ├── __init__.py  
    └── test_.py  
```

### Unit Testing :

**After getting the project in order, I started putting some unit tests using the libraries [unittest](https://docs.python.org/3/library/unittest.html) and [hypothesis](https://hypothesis.readthedocs.io/en/latest/).**  
**Some of the implemented tests :** Response status code, content type, content values and for reverse_fibonacci function I prefered using a hypothesis test which verifies for example the assertion `reverse_fibonacci(functools_fibonacci(num)) == num` for a bunch of values automatically instead of testing manually for every single integer.

### Docker image :

**For the docker image I used Alpine Linux which is a light weight distribution. This container will allow us to run the API and to deploy it easily.**  

### Testing Web Application :

**To be able to test my API I created a small Web App with Flask that I putted inside the test directory and will run in a different server.**

### Changes for Production :

**If the API is meant for production use the first step will be handling errors and bad inputs inside resources files (I believe that handling errors inside the resource will be less expensive and more secured than hadling it inside the called function. Handling the bad inputs inside our function could expose some snesitive informations about it).
