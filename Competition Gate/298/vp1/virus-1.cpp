#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Virus
{
private:
    string name;
    int malignancy;
    int age;
public:
    Virus()
    {
    };

    void SetName(string _name)
    {
        name = _name;
    };

    void SetMalignancy(int _malignancy)
    {
        malignancy = _malignancy;
    };

    void SetAge(int _age)
    {
        age = _age;
    };

    void Update()
    {
        age++;

        if(age%3 == 0)
        {
            malignancy++;
        }

        if(malignancy < 0)
        {
            malignancy = 0;
        }
        if(malignancy > 99)
        {
            malignancy = 99;
        }

        cout << "Nama: " << name << "; Usia: " << age << "; Tingkat Keganasan: " << malignancy << endl;
    };
};

int main()
{
    int numberOfVirus;
    int numberOfDay;

    string virusName;
    int virusAge;
    int virusMalignancy;

    vector<Virus*> viruses;

    cin >> numberOfVirus;
    cin >> numberOfDay;

    for(int i=0; i<numberOfVirus; i++)
    {
        cin >> virusName;
        cin >> virusAge;
        cin >> virusMalignancy;

        Virus *virus = new Virus();
        virus->SetName(virusName);
        virus->SetAge(virusAge);
        virus->SetMalignancy(virusMalignancy);

        viruses.push_back(virus);
    }

    for(int day=1; day<=numberOfDay; day++)
    {
        cout << "Hari #" << day << endl;
        for(int i=0; i<(int)viruses.size(); i++)
        {
            viruses[i]->Update();
        }
    }
}
