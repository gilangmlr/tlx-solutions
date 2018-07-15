
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

        if self.age % 3 == 0:
            self.malignancy += 1

        if self.malignancy < 0:
            self.malignancy = 0

        if self.malignancy > 99:
            self.malignancy = 99
    
    def __str__(self):
        return "Nama: {}; Usia: {}; Tingkat Keganasan: {}".format(self.name, str(self.age), str(self.malignancy))

if __name__ == "__main__":
    tmp = input().split()
    number_of_virus = int(tmp[0])
    number_of_day = int(tmp[1])

    viruses = []
    for index_of_virus in range(0, number_of_virus):
        tmp = input().split()
        virus_name = tmp[0]
        virus_age = int(tmp[1])
        virus_malignancy = int(tmp[2])

        tmp_virus = Virus(virus_name, virus_age, virus_malignancy)

        viruses.append(tmp_virus)

    for day in range(1, number_of_day + 1):
        print("Hari #{}".format(str(day)))

        for index_of_virus in range(0, len(viruses)):
            viruses[index_of_virus].update()
            
            print(viruses[index_of_virus])
