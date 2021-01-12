#pragma once
#include <vector>
#include <iostream>
#include <mutex>
using namespace std;

class Disponibilitate {
    vector<pair<string, vector<int>>> zile;
    mutex readWriteLock;
public:
    Disponibilitate() {
        vector<int> ore{ 8, 9, 10, 11, 12, 13, 14 };
        vector<string> numeZile{ "Luni", "Marti", "Miercuri", "Joi", "Vineri" };

        for (const auto& zi : numeZile) {
            zile.emplace_back(zi, ore);
        }
    };
    ~Disponibilitate() {
        cout << __FUNCTION__ << this << " has been destroyed " << endl;
    }
    bool isAvailable(const string& ziua, int ora) {
        readWriteLock.lock();
        bool isOk = false;

        for (auto& zi : zile) {
            if (zi.first == ziua) {
                for (auto iter = zi.second.begin(); iter != zi.second.end() && !isOk; iter++) {
                    if (*iter == ora) {
                        isOk = true;
                    }
                }
            }
            if (isOk == true)
                break;
        }
        readWriteLock.unlock();
        return isOk;
    }

    bool rezerva(const string& ziua, int ora) {
        bool isOk = false;
        readWriteLock.lock();
        for (auto& zi : zile) {
            if (zi.first == ziua) {
                int i = 0;
                for (auto iter = zi.second.begin(); iter != zi.second.end() && !isOk; iter++) {
                    if (*iter == ora) {
                        zi.second[i] = 20;
                        isOk = true;
                    }
                    i++;
                }
            }
            if (isOk == true)
                break;
        }
        readWriteLock.unlock();
        return isOk;
    }
};
