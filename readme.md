#Remaking Dave
-----
This is a project where me and some of our friends are trying to make something similar to [Dangerous Dave](https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=dangerous+dave+wiki&*), using [pygame](http://www.pygame.org/lofi.html). You are most welcome to participatein this project and learn new things along with us, all you need to know is a bit of Python(loops, functions, classes).

##Setting up the enviornment
----
1. Clone the repository `git clone https://github.com/lambainsaan/RemakingDave.git`
2. Check if it works!

```
cd RemakingDave/
pip install pygame
python binder.py
```

### Running the test cases

You might get an error when you try to run the program tests/test_player.py, it is probably because the PYTHONPATH enviornment variable does not have the path associated with the module RemakingDave. You can add it on Unix based machine using the command `export PYTHONPATH=$HOME/path-of-remakingdave/:$PYTHONPATH`.

On Windows OS you can add the module's path to the enviornment variable using the information at https://www.java.com/en/download/help/path.xml
