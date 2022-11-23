# Pycharm-Workshop

## Exercise 2 - Debug and win

In this exercise you will practise running tests within a docker and debugging code.  
We will use the nommon-base-py3 image for running this Python3 code. 

If the image doesn't exist. Open the pycharm terminal and use the command.

`./resources/docker/start_nommon_base_py3.sh -i`

For creating and running a docker container:

(Note: If the container already exists, use: `./resources/docker/start_nommon_base_py3.sh -d` 
to delete the existing container)

`./resources/docker/start_nommon_base_py3.sh -r`


Within the docker container use the following command to run the tests:

`pytest tests/tests_code/nommon_pizza`

**The tests are failing!**

Open a Jupyter Lab inside the docker and debug the code to fix the issues.

For opening a jupyter lab, use the command `jl` within the docker terminal.  
You ~~should~~ **MUST** use the debug tool of jupyter lab.

**_The only code that needs to be changed is the function that gives the error._**


![](https://i0.wp.com/blog.cambro.com/wp-content/uploads/2021/10/PizzaQuiz.png?ssl=1)

