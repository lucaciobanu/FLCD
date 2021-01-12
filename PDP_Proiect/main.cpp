#include <iostream>
#include "Clasa.h"
#include "Orar.h"
#include "Disponibilitate.h"
#include "Materie.h"
#include "Profesor.h"
#include "Controller.h"
#include <fstream>
#include <string>
vector<Profesor*> getProfesori() {
    vector<Profesor*> prof;
    ifstream fin("names.txt");
    string name;
    while (fin >> name) {
        prof.push_back(new Profesor{ name });
    }
    fin.close();
    return prof;
}

vector<Clasa*> getClase() {
    vector<string> litere{ "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F","G","H","J","K","L","Z","X","C","V","B","N","M" };
    vector<Clasa*> clase;
    for (int i = 1; i <= 12; i++) {
        for (int j = litere.size() - 1; j >= 0; j--) {
            string n = "Clasa a ";
            n.append(to_string(i));
            n.append("-a ");
            n.append(litere[j]);
            clase.push_back(new Clasa{ n });
        }
    }
    return clase;
}
vector<Materie*> getMaterii(vector<Profesor*> prof, vector<Clasa*> clase) {
    vector<Materie*> materii;
    vector<string> numeMaterii{ "Matematica", "Romana", "Istorie", "Geografie", "Biologie", "Sport", "Muzica", "Desen", "Engleza", "Germana", "Franceza", "Chimie", "Fizica" };
    vector<int> aparitii{ 4, 5, 2, 1, 3, 1, 3, 3, 3, 3, 3, 3, 1 };

    int k = 0;
    for (int i = 0; i < 13; i++) {
        vector<Profesor*> profi;
        for (int j = 0; j < 12; j++) {
            profi.push_back(prof[k + j]);
        }
        k += 12;
        materii.push_back(new Materie{ numeMaterii[i], profi, clase, aparitii[i] });
    }
    return materii;
}
int main()
{
    auto x = getProfesori();
    auto y = getClase();
    auto z = getMaterii(x, y);

    Controller c{ z };
    //c.saiDamBataieBaieti();
    c.saiDamBataieBaietiAsync();
    y[0]->printOrarClasa();
    cout.flush();
}
