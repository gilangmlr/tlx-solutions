
class Virus:
    def __init__(self, _name, _age, _malignancy):
        self.name = _name
        self.age = _age
        self.malignancy = _malignancy

    def set_name(self, _name):
        self.name = _name
    
    def set_age(self, _age):
        self.age = _age

    def set_malignancy(self, _malignancy):
        self.malignancy = _malignancy

    def update(self):
        self.age += 1

        self.update_malignancy()
        self.cutoff_malignancy()
    
    def cutoff_malignancy(self):
        if self.malignancy < 0:
            self.malignancy = 0
        if self.malignancy > 99:
            self.malignancy = 99

    def update_malignancy(self):
        if self.age >= 200:
            # LebayEffect
            if self.age % 5 == 0:
                self.malignancy += 2
        else:
            if self.age % 3 == 0:
                self.malignancy += 1
    
    def __str__(self):
        return "Nama: {}; Usia: {}; Tingkat Keganasan: {}".format(self.name, str(self.age), str(self.malignancy))

class AlayVirus(Virus):
    def update_malignancy(self):
        self.malignancy += 2

class BaikVirus(Virus):
    def update_malignancy(self):
        if self.age % 100 == 0:
            self.malignancy += 1

class MagerVirus(Virus):
    def update_malignancy(self):
        pass

class LebihBaikVirus(Virus):
    def update_malignancy(self):
        if self.age % 5 == 0:
            self.malignancy -= 1

class AbabilVirus(Virus):
    def update_malignancy(self):
        if self.age < 100:
            if self.age % 4 == 0:
                self.malignancy += 7
        elif self.age > 100 and self.age % 10 == 0:
                self.malignancy //= 2

if __name__ == "__main__":
    tmp = input().split()
    number_of_virus = int(tmp[0])
    number_of_day = int(tmp[1])

    virus_types = {
        "4L4Y": AlayVirus,
        "B41K": BaikVirus,
        "M4G3R": MagerVirus,
        "LBHB41K": LebihBaikVirus,
        "ABA81L": AbabilVirus
    }

    viruses = []
    for index_of_virus in range(0, number_of_virus):
        tmp = input().split()
        virus_name = tmp[0]
        virus_age = int(tmp[1])
        virus_malignancy = int(tmp[2])

        virus_class = virus_types.get(virus_name, Virus)

        tmp_virus = virus_class(virus_name, virus_age, virus_malignancy)

        viruses.append(tmp_virus)

    for day in range(1, number_of_day + 1):
        print("Hari #{}".format(str(day)))

        for index_of_virus in range(0, len(viruses)):
            viruses[index_of_virus].update()
            
            print(viruses[index_of_virus])
