## Where to upload
Once you have some files related to your problem make a folder in /Challenges with your problem name or a temporary name and place the files there.

## When to upload
Obviously by the Codeathon date, but perferably you should have everything uploaded a week in advance so that other problem writers can review your work and 
make sure there are no issues.

## Hackerrank
See below for the files needed to be uploaded to the Github. Those files are the majority of the work needed to make a problem. The rest of the work is creating the 
problem on Hackerank and uploading the test cases. If you've worked on the Code-a-thon or attended in the past, you know there is usually a little backstory for the 
problem to make it unique and memorable. This is also done to bury the lead on the algorithm you used in your solution if its somewhat noticeable. All this is done on
hackerank itself which will be linked in the README.md once the divisions are created. You will create the problem on Hackerrank individually and then add them to the
proper divisions. It is too much to explain here, so feel free to reach out to other problem writers on how to make a problem on Hackerank. There will also be example
problems from previous semesters linked in the README.md

## What to upload
The 2 main things you will need to upload, either in seperate files or together, is an I/O generator and a Solution in whatever language you choose. There is more information 
on the google drive which is linked in the README.md along with a template generator to help you generate test cases.

### I/O Generator
This will produce a folder containing subdirectories ./input and ./output. The .txt files in these directories will be labeled input<tid>.txt and output<tid>.txt. 
The test case id "tid", is a number starting from 0 and going up for each consecutive test case, input and output files with the same tid are linked. For example, 
when the correct solution is fed input from file "input0.txt", it should produce the data stored in the file "output0.txt". This zipped folder can easily be uploaded
to Hackerrank to create the test cases for your problem there. <b> Do not upload the .txt files to the Github, <i> only the generator itself. </i></b>

  
### Solution
This will be a code file in any language that you choose, although one of Java, Python, C/C++ is recommended. This file will read from the standard input stream in your
given langauge and send out the corresponding anwser to the standard output stream. The reason for this format is sp that input information can be fed directly to the 
file to produce the output. 
  
  
  
Lets imagine a simple problem in which we read in a single number N and print out a single number N + 6. 
  
#### input0.txt
---------------
        2
  
#### output0.txt
----------------
        8
  
#### Sol.py
-----------
        N = int(input()) 
        print(N + 6)

#### Sol.cpp
------------
        #include <iostream>
        int main() {
          int N;
          std::cin >> N;
          std::cout << N+6 << std::endl;
        }
  
#### Sol.java
-------------
        ... void main ... {
          Scanner scanner = new Scanner(System.in);
          int N;
          N = Integer.parseInt(scanner.nextLine());
          System.out.println(N+6);
          scanner.close();
        }
        
  
  
  
  
  
  
 
