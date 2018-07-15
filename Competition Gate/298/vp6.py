from math import ceil
class Virus:
    def __init__(self, _name, _age, _malignancy):
        self.name = _name
        self.age = _age
        self.malignancy = _malignancy

        _is_immortal = False
        if _name.startswith("D"):
            _is_immortal = True
        self.is_immortal = _is_immortal

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

        if self.is_immortal or self.age < 365:
            return True
        
        return False
    
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

class AbabilV2Virus(AbabilVirus):
    def update_malignancy(self):
        self.malignancy += 1

        super().update_malignancy()

class DargombesVirus(Virus):
    def update_malignancy(self):
        self.malignancy += 3
    
    def cutoff_malignancy(self):
        if self.malignancy < 0:
            self.malignancy = 0
        if self.malignancy > 9999:
            self.malignancy = 9999

class DewaruciVirus(Virus):
    def update_malignancy(self):
        if self.age % 2 == 0:
            self.malignancy -= 5
    
    def cutoff_malignancy(self):
        if self.malignancy < -9999:
            self.malignancy = -9999
        if self.malignancy > 0:
            self.malignancy = 0

class DobbyVirus(Virus):
    def __init__(self, _name, _age, _malignancy):
        super(DobbyVirus, self).__init__(_name, _age, _malignancy)

        self.is_immortal = False

    def update_malignancy(self):
        if self.malignancy > 0:
            if self.age >= 200:
                if self.malignancy > 300:
                    self.malignancy -= 15
                elif self.age >= 300:
                    self.malignancy //= 2
                else:
                    self.malignancy -= 3
            else:
                self.malignancy -= 3
        else:
            if self.age >= 100:
                if self.malignancy < -600:
                    if self.age >= 110:
                        self.malignancy = ceil(self.malignancy / 2)
                    else:
                        self.malignancy += 15
                else:
                    self.malignancy += 7
            else:
                self.malignancy += 2
    
    def cutoff_malignancy(self):
        if self.malignancy < -666:
            self.malignancy = -666
        if self.malignancy > 666:
            self.malignancy = 666

if __name__ == "__main__":
    tmp = input().split()
    number_of_virus = int(tmp[0])
    number_of_day = int(tmp[1])

    virus_types = {
        "4L4Y": AlayVirus,
        "B41K": BaikVirus,
        "M4G3R": MagerVirus,
        "LBHB41K": LebihBaikVirus,
        "ABA81L": AbabilVirus,
        "ABA81LV2": AbabilV2Virus,
        "DARGOMBES": DargombesVirus,
        "DEWARUCI": DewaruciVirus,
        "DOBBYTHEHOUSEELF": DobbyVirus,
        "DOBBY": DobbyVirus
    }

    viruses = []
    for index_of_virus in range(number_of_virus):
        tmp = input().split()
        virus_name = str(tmp[0])
        virus_age = int(tmp[1])
        virus_malignancy = int(tmp[2])

        virus_class = virus_types.get(virus_name, Virus)

        tmp_virus = virus_class(virus_name, virus_age, virus_malignancy)

        viruses.append(tmp_virus)

    for day in range(1, number_of_day + 1):
        print("Hari #{}".format(str(day)))

        for virus in viruses:
            is_updated = virus.update()

            if is_updated:
                print(virus)
