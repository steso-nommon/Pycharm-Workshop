# Pycharm-Workshop

## Exercise 2 - Debug and win

In this exercise you will practise running tests within a docker and debugging code.  
We will use the nommon-base-py3 image for running this Python3 code. 

For creating the image, open the pycharm terminal and use the command.

`./resources/docker/start_nommon_base_py3.sh -i`

For creating and running a docker container:

`./resources/docker/start_nommon_base_py3.sh -r`

(Note: If the container already exists, use: `./resources/docker/start_nommon_base_py3.sh -d` 
to delete the existing container)

Within the docker container use the following command to run the tests:

`pytest tests/tests_code/nommon_pizza`

**The tests are failing!**

Open a Jupyter Lab inside the docker and debug the code to fix the issues.


![](https://i0.wp.com/blog.cambro.com/wp-content/uploads/2021/10/PizzaQuiz.png?ssl=1)

