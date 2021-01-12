#pragma once
#include <iostream>
#include "Disponibilitate.h"
#include "Orar.h"
class Clasa {
    string name;
    Disponibilitate d;
    Orar orar;

public:
    Clasa(string name) {
        this->name = name;
    }
    ~Clasa() {
        cout << __FUNCTION__ << this << " has been destroyed " << endl;
    }
    bool rezervaClasa(const string& ziua, int ora, const string& materie) {
        bool ok = d.rezerva(ziua, ora);
        if (ok)
        {
            orar.adaugaMaterie(ziua, ora, materie);
        }
        //else
        //    cout << "Am dat si un false, atata am putut :(";
        return ok;
    }
    bool isAvailable(const string& ziua, int ora) {
        return d.isAvailable(ziua, ora);
    }
    void printOrarClasa() {
        cout << this->name << ":\n";
        orar.printOrar();
    }
};
