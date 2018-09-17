
## 30 < porter < 50
## 30 < stout  < 70
## 30 < APA < 45
## 40 < EnglishIPA < 60
## 60 < IPA < 120
## 20 < Belgian < 40




class Hop:
    styles=(("Porter",30,50),("Stout",30,70),("APA",30,45),("EnglishIPA",40,60),("ImperialIPA",60,150),("Belgian",20,40))
    boil_time=0
    weight=0
    aa=0
    volume=0
    kind=0
    ## 0 FIORI, 1 PELLETS
    def __init__(self,boil_time,weight,aa,boil_volume,kind):
        self.boil_time=boil_time
        self.weight=weight
        self.aa=aa
        self.volume=boil_volume
        self.kind=kind

    def calculate_ibu(self):
        if self.boil_time==0:
            return self.boil_time

        if self.kind==0:
            util=1.5779+(0.6261*self.boil_time)-(0.0041*self.boil_time*self.boil_time)
        else:
            util=1.9348+(0.7835*self.boil_time)-(0.0051*self.boil_time*self.boil_time)

        return round(self.weight*self.aa*util*0.1 / self.volume, 2)

    def calculate_style(self,ibu):
        style_str=""
        for l in self.styles:
            if ibu>=int(l[1]) and ibu<=int(l[2]):
                style_str+=str(l[0])+","
        return style_str[:-1]


if __name__ == "__main__":
    BOIL_VOL=10
    bitter=Hop(60,15,12,BOIL_VOL,1)
    taste=Hop(20,20,6,BOIL_VOL,0)
    flav=Hop(0,10,4,BOIL_VOL,0)

    ibu_bitter=bitter.calculate_ibu()
    ibu_taste=taste.calculate_ibu()
    ibu_flav=flav.calculate_ibu()

    ibu=ibu_bitter+ibu_taste+ibu_flav

    print "IBU value -bitter- : "+str(ibu_bitter)
    print "IBU value -taste-  : "+str(ibu_taste)
    print "IBU value -flavour-: "+str(ibu_flav)

    print "TOTAL IBU: "+str((ibu))
    style_str=""
    for l in bitter.styles:
            if ibu>=int(l[1]) and ibu<=int(l[2]):
                style_str+=str(l[0])+","

    print " Suitable for styles: "+style_str[:-1]

    ## 30 < porter < 50
    ## 30 < stout  < 70
    ## 30 < APA < 45
    ## 40 < EnglishIPA < 60
    ## 60 < IPA < 120
    ## 20 < Belgian < 40


