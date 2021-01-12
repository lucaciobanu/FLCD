#pragma once
#include "Disponibilitate.h"
#include <iostream>
class Profesor {
    Disponibilitate d;
    string nume;

public:
    Profesor(string nume) {
        this->nume = nume;
    }
    ~Profesor() {
        cout << __FUNCTION__ << this << " has been destroyed " << endl;
    }
    bool reservaProfesor(const string& ziua, int ora) {
        return d.rezerva(ziua, ora);
    }
    bool isAvailable(const string& ziua, int ora) {
        return d.isAvailable(ziua, ora);
    }
    string getName() {
        return this->nume;
    }
};
