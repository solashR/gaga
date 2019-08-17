- In this repo given the build.py & test.py executables
- The build.py - simulated a build of artifacts, and print to stdout a list (json) of tests that need to run
- The test.py - simulate running a test after the build phase, the test.py can  get a test name as argument, can be only from the names build.py produced 
    some of the tests can fail, each test run also print some number to stdout

- You need to write a jenkins pipeline (scripted) code that:
    1. run the build script, and get the tests name
    2. run all the tests in parallel, after the build finish
    3. the build.py & test.py should not be changed
    4. before each shell invocation you should print "going to run <the cmd>"
    5. after each failed shell invocation you should print "cmd: <cmd> failed"
    6. after each successful shell invocation you should print "cmd: <cmd> succeeded"
    7. after each cmd you should check how much time the cmd took, if it took morethan 30 seconds you should print something to indicate that
    7. if one of the tests has failed the job should still pass
    8. THe job should have get a number as param (by default 2)
    8. after all tests were run you calculate the sum of all the numbers that failed tests printed, if the sum is not divided by the param you should fail the job
    9. the sum of the from step 8 should be written to some file and the file should be archived
