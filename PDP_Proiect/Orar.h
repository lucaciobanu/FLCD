#pragma once

#include <vector>
#include <iostream>
using namespace std;

class Orar
{
	vector<pair<string, vector<pair<int, string>>>> orar;
	
public:
	Orar() {
		vector<string> zileleSaptamanii = { "Luni","Marti","Miercuri","Joi","Vineri" };
		vector<int> oreDinZi = { 8 ,9, 10, 11, 12, 13, 14 };
		for (auto zi : zileleSaptamanii) {
			pair<string, vector<pair<int, string>>> ziOrar;
			ziOrar.first = zi;

			for (auto ora : oreDinZi) {
				pair<int, string> oraOrar;
				oraOrar.first = ora;
				oraOrar.second = "";
				ziOrar.second.push_back(oraOrar);
			}
			orar.push_back(ziOrar);
		}
	}
	void adaugaMaterie(const string& ziua, int ora, const string& materie) {
		for (auto& zi : orar) {
			if (zi.first == ziua) {
				for (auto& oraDinZi : zi.second) {
					if (oraDinZi.first == ora) {
						oraDinZi.second = materie;
					}
				}
			}
		}
	}
	void printOrar() {
		for (auto i : orar) {
			cout << i.first << ": ";
			for (auto j : i.second) {
				cout << "|||Ora: " << j.first << ", Materie:" << j.second << "|||";
			}
			cout << '\n';
		}
	}
};
