// Dev Singh 04/23/2020 Files program (but in C++!)
#include <fstream> // import the fstream library to deal with files as a standard stream
#include <iostream> // import the iostream library which allows me to output to the console and recieve input.
#include <ctime> //allows me to get the current time to write to the file. 
#include<stdio.h> // allows me to get space seperated input
#include <vector> //allows for use of dynamically-sized arrays
using namespace std; // use the standard namespace which contains string, cout, etc. so i dont have to keep typing std::cout

// Prototype all the neccessary functions so I don't have to call them in order.
string readFile(string fileName);
void writeToFile(string name, string date);
void writeToFile(string method);
void option2a();
void option2b();
void option1();
string option2();
void bonus();
string getChoice();
void prompt();

string readFile (string fileName) {
    string iter_text;
    string output; // define 2 strings

    // Read from the text file
    ifstream f(fileName); // create a file with the type `ifstream` and read ReadMe.txt

    // Use a while loop together with the getline() function to read the file line by line
    while (getline (f, iter_text)) {
    // Output the text from the file
        output.append(iter_text);
        output.append("\n");
    }

    // Close the file
    f.close(); 
    return output;
}

void writeToFile(string name, string date) {
    ofstream f("ReadMe.txt", ios_base::app); // Open the file
    f << name << "     " << date << endl; // Write to the file
    f.close(); // close the file
} 

void writeToFile(string method) {
    ofstream f("Relax.txt", ios_base::app); // Open the file
    f << method << endl; // Write to the file
    f.close(); // close the file
} 
void writeToBonus(string file, string method) {
    ofstream f(file, ios_base::app); // Open the file
    f << method << endl; // Write to the file
    f.close(); // close the file
} 


void option2a() {
    int inc = 0;
    string inputs [5];
    for (int i = 0; i < 5; i++) {
        int ch;
        string hi;
        hi = "";
        if (i == 0) {
            while ((ch = cin.get()) != '\n' && ch != EOF);
        }
        cout << "Input one way you destress (lines seperated by Enter): ";
        cout.flush();
        getline(cin, hi);
        hi.append("\n");
        inputs[i] = hi;
    }
    for (int i = 0; i < 5; i++) {
        writeToFile(inputs[i]);
    }
    cout << readFile("Relax.txt");
    prompt();
}

void option2b() {
    string hi;
    cout << "Here is some strategies people have listed before: " << endl;
    cout << readFile("Relax.txt");
    int ch; 
    while ((ch = cin.get()) != '\n' && ch != EOF);
    cout << "Input one way you destress (lines seperated by Enter): ";
    cout.flush();
    getline(cin, hi);
    hi.append("\n");
    writeToFile(hi);
    cout << "Added!" << endl;
    cout << readFile("Relax.txt");
    prompt();
}

void option1 () {
    string fileOuptut = readFile("ReadMe.txt");
    cout << "Here is what is in the file: " << endl;
    cout << fileOuptut << endl;
    cout << "Now, I need to get what your name is for the visitor log. Please enter your first name: ";
    string userName;
    string dt;
    cin >> userName;
    time_t tnow = time(0);
    dt = ctime(&tnow);
    writeToFile(userName, dt);
    prompt();
}
string option2 () {
    string choice;
    char ch;
    do {
        cout <<"Choose menu option 2a or 2b: ";
        cin >> choice;
        if (choice == "2a" || choice == "2b") {
            break;
        }
        else {
            cout <<"Invalid option!"<<endl;
            'y' >> ch;
            choice = option2();
        }
    }while(ch=='y' || ch=='Y');
    if (choice == "2a") {
        option2a();
    } else if (choice == "2b") {
        option2b();
    }
    return choice;
}
string getnum1 () {
    string num1;
    cout << "Enter Number 1:" << endl;
    cin>>num1;
    try {
        stoi(num1);
    } catch(std::invalid_argument e1) {
        if (num1 != "stop"){
            cout << "Invalid input" << endl; 
            num1 = getnum1();
        }
    }
    return num1;
}
string getnum2 () {
    string num1;
    cout << "Enter Number 2:" << endl;
    cin>>num1;
    try {
        stoi(num1);
    } catch(std::invalid_argument e1) {
        if (num1 != "stop"){
            cout << "Invalid input" << endl; 
            num1 = getnum2();
        }
    }
    return num1;
}
void bonus () {
    string filename;
    cout << "Enter the filename of the file you would like to write to: " << endl;
    cin >> filename;
    vector<vector<string>> array;
    string num1;
    string num2;
    vector<string> interims;
    cout << "At any time, enter 'stop' for both values to exit" << endl;
    while(num1 != "stop"){
        interims.clear();
        num1 = getnum1();
        num2 = getnum2();
        if (num1 == "stop" || num2 == "stop") {
            break;
        } else {
            interims.push_back(num1);
            interims.push_back(num2);
            array.push_back(interims);
        }
    }
    string output;
    for (int i = 0; i < array.size(); i++) {
        string sum = to_string(stoi(array[i][0]) + stoi(array[i][1]));
        output = array[i][0] + "+" + array[i][1] + "=" + sum + "\n";
        writeToBonus(filename, output);
    }
    cout << readFile(filename);
    prompt();
}

string getChoice () {
    string choice; 
    char ch;
    do {
        cout <<"Choose menu option 1 2 or Bonus: ";
        cin >> choice;
        if (choice == "1" || choice == "2" || choice == "Bonus" || choice == "bonus") {
            break;
        }
        else {
            cout <<"Invalid option!"<<endl;
            'y' >> ch;
            choice = getChoice();
        }
    } while(ch=='y' || ch=='Y');
    return choice;
}
void prompt() {
    int ch;
    cout.flush();
    string choice = getChoice();
    if (choice == "1") {
        option1();
    } else if (choice == "2") {
        option2();
    } else {
        bonus();
    }
}
int main ()  {
    cout << "Hello and welcome to this program!" << endl;
    cout << "You see, I just came to the realization that the CSI assignment descriptions never actually specify that these programs must be done in python." << endl;
    cout << "Knowing me, I decided to exploit this loophole" << endl;
    cout << "Have fun!" << endl;
    cout << "----------------------------" << endl;
    prompt();
}