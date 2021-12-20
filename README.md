# Readme for Koodoo Technical challange

This file lists and describes the developed code and steps to run the code for the challange

## 1. The Solution
I have used python as a programming language to approach this solution.

### Python Packages used
1. **requests** - to get the response from the xml endpoint
2. **ElementTree** - to parse the XML data received from the endpoint
3. **traceback** - to handle the exceptions and print the trackbacks for error handling

## 2. Packages installation
while ElementTree and Tarceback already come with a distribution of python already installed. However in the case they are not available, they can be installed with the use of pip(which also comes with python disribution).

1. Make sure python is intsalled and path to python is mapped to system variables. Also make sure that pip is intalled.
2. To verify any package is installed and available, open the python prompt on terminal and write the command `<package name>.__version__`, it will display the package version, if it throws an error , it means the package is not available on the system and needs to be installed.
2. Install the packages using the command `pip install <package name>`
3. if the package is already installed, it will just skip the installation process and print a generic message on the termial/prompt as requirement already satisfied

## 3. Working
The code is able to fetch the requried data from the xml i.e. the *Top stories* but there are a few things to consider here 
1. The code is subject to that the format of the response do not change, a chnage in the format of the XML data(depends on the change) may require a change in the code itslef.
2. The code does handle if the end point is down or the code is unable to retieve the data from the end point, using the `response code` returned by the end point.
3. if the data is malformed or any change in the format of the data will lead the code to raise an exception.

Since the code is a python file, it can run on any platofrm with a python support i.e. Unix/Linux, windows and mac

## 4. Running the code

The code can be executed with the below steps
1. Open a terminal/prompt and navigate to the directory where the file is located
2. To execute the code type the following command `python TopStories-koodoo.py` and press enter
3. Which will procude an output similar to below

## 5. Output

```
Top stories below

********************
Top stories - European Parliament
1 )  Top story - Transparent taxation - The fight for a fair and transparent tax system
2 )  Top story - Culture - How the EU supports culture
3 )  Top story - European Parliament’s Sakharov Prize 2021 - Alexei Navalny
4 )  Top story - Food and agriculture - Ensuring a safe, sustainable and secure food supply
5 )  Top story - State of the European Union Debate 2021 - Addressing Europeans' concerns
6 )  Top story - Digital transformation in the EU - Benefitting people, the economy and the environment
7 )  Top story - LUX Audience Award 2021 - The best of European cinema
8 )  Top story - The future is in your hands - Conference on the Future of Europe
9 )  Top story - International Women’s Day 2021 - Women leading the fight against Covid-19
10 )  Top story - Vaccines against Covid-19 - Ensuring safe vaccines for EU citizens
```