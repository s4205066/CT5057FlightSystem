Open with command prompt:
python main.py

----------------------------------------------------------------
The requirements for the assessment 

The primary goal of this assignment is to grasp the design and functionality of fundamental searching, sorting, and traversing algorithms (LO1). It involves comprehending various methodologies for assessing the efficiency of algorithms (LO2) and comparing them based on their performance metrics, including both time and space considerations (LO3).

For this assignment, your task is to create a flight scheduling program that enables customers to book and schedule flights, utilizing a variety of data structures covered in the lectures.

Each flight has the following properties:

·        A flight number (integer 0- 999)      

·        A departure airport   

·        A departure date        

·        An arrival airport      

·        A seating list 

Each seating list has the following properties:

·       The number and range of first class seats (i.e. 5 seats, seats 1, 2, 3, 4, and 5).

·       The number and range of business class seats (i.e. 10 seats, seats 6 - 15)

·       The number and range of economy class seats (i.e. 20 seats, seats 16 - 35)

 

Note: A particular class can have an arbitrary range of seats (i.e. first class, 5 seats, seats 1, 5, 9, 11, 21). Once the list of flights is given, you are ready to start scheduling passengers. The scheduling must handle several operations.

Once the list of flights is given, you are ready to start scheduling passengers. The scheduling must handle several operations.

Schedule a passenger for a flight: Choose a flight number. Choose a class. If all the seats are full, give the option to put the passenger on a wait list. There should be a wait list for every class (first, business, and economy).

Cancel a passenger from a flight: Choose a passenger. Choose a flight. If there are passengers on the wait list, print the name of the next passenger and give the option to schedule that passenger for the available seat.

Passenger status: print the status of a passenger; Choose a passenger. If the passenger is scheduled for a flight, print the flight information. If the passenger is on a wait list, print the flight information and the passenger's position on the wait list.

Flight information: print the information for a flight; Print the departure airport, the departure date, the arrival airport, and a list of all the seats and the name of the passenger in each seat.

Algorithm and Data Structure

There are many ways to implement this program, many different data structures and algorithms can be used, and many ways the project description can be extended and be more realistic. However, you are required to use:

·       at least one of the data structures (queues/graphs/trees) proposed in lectures;

·       at least one of the sorting algorithms studied during the lectures;

·       at least one of the searching algorithms studied during the lectures;

It will be interesting to think about these issues during the project and as we explore more sophisticated data structures in the next few weeks. For now, however, try to keep it as simple as possible. Once you have a working prototype and by then we have covered more data structures, you can extend this program to satisfy the needs of assessment brief by incorporating the advance algorithms we have covered.

Implementation environment

You can use any environment (Java/Python) to develop your code. Your final submission must be an executable along with the source code submitted in the zip file.

Submission Instructions

Students need to submit the following two components:

A.    Report (LO1, LO2, LO3, LO4)

The assignment will be an individual report consisting of:

·           a brief overview of the studied problem;

·           requirements specifications using relevant UML diagrams

·           a description of your adopted approach, including

o   Brief explanations of software functionalities; used analytical techniques; adopted assumptions; links to the state of the art; proposed method design;

o   Detailed explanations of the selected data structure and its use in the developed system. Provide analytical details and justify your choices.

o   For the algorithms, based on your application requirements make appropriate selection and justify your choices. Explain how the algorithm will work within your system and detail its steps.

 ·           Comments about the software implementation, parameters, and adopted software testing process and metrics;

·           A discussion about your results (reflection on testing approach, reflection on performance such as time, accuracy, etc., analysis of system performance using Big O-notation);

·           Conclusions (reflection on the adopted methods and alternatives, reflection on the development – what went right/wrong, reflection on Ethics, reflection on possible improvements).

·           The report should include relevant references to the source materials and tools used. Please note that appendices and references are not included in the word count.

 

B.    Code (LO1, LO2, LO3,LO4)

Debugged, structured and commented source code, in Java or Python.

The executable must be called airlines.exe

Submit the complete software code for your system, appropriate data and test-cases as a zip file.

Marks Distribution:

    Report 50% (Structure of the report, Coherence, Harvard Referencing, Discussion on Algorithms, Selection Justification, Diagrams, Critical Analysis)
    Implementation 40% (Implementation of System, Algorithms Implementation, Object Orientation, Flow of the System, Comments)
    Testing 10%

3. Arrangements for submission 
Your assessment will be submitted online via Moodle. Please name the files you are submitting using the convention:

MODULE CODE_ASSESSMENT NUMBER (if more than one)_STUDENT NUMBER (plus _FILE NUMBER if more than one file is being submitted)

Please ensure you do not use special characters (e.g. brackets, commas, speech marks, question marks, etc.) in the file name.

The Maximum file size for uploading is 100MB.  

4. How your assessment will be marked 

You need to achieve at least 40% to pass this assessment.

