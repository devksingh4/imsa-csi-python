#include <fstream> // import the fstream library to deal with files as a standard stream
#include <iostream> // import the iostream library which allows me to output to the console and recieve input.
#include <ctime> //allows me to get the current time to write to the file. 
#include<stdio.h> // allows me to get space seperated input
using namespace std; // use the standard namespace which contains string, cout, etc. so i dont have to keep typing std::cout

// Prototype all the functions so I don't have to call them in order.
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
  // Create and open a text file
  ofstream f("ReadMe.txt", std::ios_base::app);

  // Write to the file
  f << name << "     " << date << "\n";

  // Close the file
  f.close();
} 

void writeToFile(string method) {
  // Create and open a text file
  ofstream f("Relax.txt", std::ios_base::app);

  // Write to the file
  f << method << "\n";

  // Close the file
  f.close();
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
    cout << "Added!" << "\n";
    cout << readFile("Relax.txt");
    prompt();
}

void option1 () {
    string fileOuptut = readFile("ReadMe.txt");
    cout << "Here is what is in the file: " << "\n";
    cout << fileOuptut << "\n";
    cout << "Now, I need to get what your name is for the visitor log. Please enter your name: ";
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

void bonus () {
    cout << "not implemented" << endl;
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
    cout << "Hello and welcome to this program!" << "\n";
    cout << "You see, I just came to the realization that the CSI assignment descriptions never actually specify that these programs must be done in python." << "\n";
    cout << "Knowing me, I decided to exploit this loophole" << "\n";
    cout << "Have fun!" << "\n";
    cout << "----------------------------" << "\n";
    prompt();
}




