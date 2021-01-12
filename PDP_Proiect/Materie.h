#pragma once
#include "Disponibilitate.h"
#include "Clasa.h"
#include <vector>
#include <iostream>
#include "Profesor.h"
using namespace std;

class Materie {
   
    string name;
    vector<Profesor*> profesori;
    vector<Clasa*> clase;

    int aparitiiPeSaptamana;

public:
    
    Materie(string nume, vector<Profesor*> profesori, vector<Clasa*> clase, int aparitii) {
        this->aparitiiPeSaptamana = aparitii;
        this->clase = clase;
        this->profesori = profesori;
        this->name = nume;
         
    }
    ~Materie() {
        cout << __FUNCTION__ << this << " has been destroyed " << endl;
    }
    //bool rezerva
    void rezolvaMateria() {

        
        vector<vector<int>> sarcini;
        for (int i = 0; i < profesori.size(); i++) {
            vector<int> sarcina;
            sarcina.push_back(i);
            sarcina.push_back(clase.size() / profesori.size());
            //[1,3]
            sarcini.push_back(sarcina);
        }

        if (clase.size() % profesori.size() != 0) {
            int remainder = clase.size() % profesori.size();
            int k = 0;
            while (remainder > 0) {
                sarcini[k][1] += 1;
                remainder -= 1;
                k += 1;
                if (k == sarcini.size()) {
                    k = 0;
                }
            }
        }

        for (int i = 0; i < clase.size(); i++) {
            vector<string> zile = { "Luni","Marti","Miercuri","Joi","Vineri" };
            Clasa* c = clase[i];
            Profesor* p = nullptr;
            for (int sarcina = 0; sarcina < sarcini.size(); sarcina++) {
                if (sarcini[sarcina][1] > 0) {
                    p = profesori[sarcina];
                    sarcini[sarcina][1] --;
                    break;
                }
            }

            int counter = this->aparitiiPeSaptamana;
            for (int ii = 8; ii < 15 && counter > 0; ii++) {
                for (auto zi : zile) {
                    if (c->isAvailable(zi, ii) && p->isAvailable(zi, ii))
                    {
                        string nume = this->name + "(" + p->getName() + ")";
                        c->rezervaClasa(zi, ii, nume);
                        p->reservaProfesor(zi, ii);
                        counter--;
                    }
                    if (counter == 0)
                        break;
                }
            }
        }
    }
};
