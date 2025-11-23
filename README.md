[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?repo=eugenschindler/test-sprinkler-system-agiledev-2025)

In Codespaces, select VSCode as IDE and Standard resources (up to 4 cores, 8 GB RAM, 30 GB storage).

The application (main.py entrypoint) is immediately run as part of starting the workspace. You can from there try the following:

1. Go through the turns of the simulation (type in values until you choose `y` when asked to stop the simulation)
2. Preview the generated HTML report:
   1. Click the "Go Live" button at the lower right of the VScode window (3 to the right)
   2. In the popup that follows, click "Open Browser" (you may need to enable your browser to allow popup windows/tabs)
   3. Go the newly opened tab and observe the HTML file - you can leave the tab open, since the view updates live when you rerun the simulation and regenerate the report during the session.
3. Type `python main.py` to run the main entry point of the code again
4. Type `python -c "from read_sensors import ReadSensors; print(ReadSensors().get_reservoir_level())"` to run the example get_reservoir_level() function from ReadSensors (don't forget the closing quote ")
5. Type `python -m unittest discover tests/` to run all tests (currently one example test is present)
6. Edit `test/test_read_settings.py` to make the test fail

This example app does not do anything useful, except show you Python command-line programming basics.
It contains some example code that shows how you can:
- use classes and test them manually isolation
- run tests with a standard Python test framework

You're expected to change pretty much everything, or even throw everything away. As you choose! 

For copyright information, see COPYRIGHT file.
