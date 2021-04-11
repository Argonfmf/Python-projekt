import requests
import re

def pretvornik_casa(a):
    if 'years' in a or 'yrs' in a:
        b = r'[0-9]+[\.]?[0-9]*'
        c = re.findall(b, a)
        d = 0
        for i in range(len(c)):
            d += float(c[i])
        if d == 0:
            d = None
        else:
            d = round(float(d/len(c)), 1)
    elif 'months' in a:
        b = r'[0-9]+[\.]?[0-9]*'
        c = re.findall(b, a)
        d = round(float(c[0])//12, 1)
    else:
        d = None
    return(d)


def pretvornik_mase(a):
    if ',' in a:
        a = a.replace(',', '')
    b = r'[0-9]+[\.]?[0-9]*'
    c = re.findall(b, a)
    d = 0
    if len(c) != 0:
        for i in range(len(c)):
            d += float(c[i])
        if 'kg' in a or 'kilograms' in a:
            d = d/len(c)
        elif 'g' in a or 'grams' in a:
            d = d/len(c)*0.001
        elif 'ton' in a or 'tons' in a or 'tonnes' in a or 'tonne' in a:
            d = d/len(c)*1000
        elif 'pounds' in a or 'lbs' in a:
            d = d/len(c)*0.453592
        elif 'ounces' in a or 'oz' in a:
            d = d/len(c)*0.02835
        d = round(d, 4)
    else:
        d = None
    return(d)


def pretvornih_hitrosti(a):
    b = r'[0-9]+[\.]?[0-9]*'
    c = re.findall(b, a)
    if len(c) != 0:
        d = round(float(c[0])*1.6, 3)
    else:
        d = None
    return(d)


def pretvornik_dolzinskih_enot(a):
    if ',' in a:
        a = a.replace(',', '')
    b = r'[0-9]+[\.]?[0-9]*'
    c = re.findall(b, a)
    d = 0
    if len(c) != 0:
        for i in range(len(c)):
            d += float(c[i])
        if 'cm' in a or 'centimeters' in a:
            d = d/len(c)*0.01
        elif 'mm' in a:
            d = d/len(c)*0.001
        elif '’' in a and '”' in a:
            d = 0
            for i in range(len(c)):
                if i % 2 == 0:
                    d += float(c[i]) * 0.3048
                else:
                    d += float(c[i]) * 0.0254
            d = d / (len(c)/2)
        elif 'in' in a or 'inches' in a or "”" in a:
            d = d/len(c)*0.0254
        elif 'ft' in a or 'feet' in a or "’" in a:
            d = d/len(c)*0.3048
        elif 'm' in a:
            d = d/len(c)
        d = round(d, 4)
    else:
        d = None
    return(d)


url = 'https://a-z-animals.com/animals/'
html = requests.get(url).text
a = html.split('Animals that start with A</a></h3><div class="container"><ul class="list-unstyled row"><li class="list-item col-md-4 col-sm-6"><a href="')[1]
b = a.split('</li></ul></div><h2 id="h-our-most-popular-wild-animal-list">')[0]
tabela_url = re.findall(r'https://a-z-animals.com/animals/[^"]+', b)



zivali = dict()

for i in range(len(tabela_url)):
    url1 = tabela_url[i]
    html1 = requests.get(url1).text
    tab = []
    plenilci, prehrana, vrsta_koze, najvisja_hitrost, zivljenjska_doba, teza, visina, dolzina, vrsta_vode = None, None, None, None, None, None, None, None, None
    if ('Breeds</a></li><li class' not in html1) and ('Chordata</dd>' in html1) and 'Family' in html1 and 'Class</dt>' in html1:
        a1 = re.findall(r'<div class="col-lg-8"><h2>[^<]+', html1)
        ime = a1[0].split('<h2>')[1].split(' Facts')[0]
        
        b1 = re.findall(r'Class</dt><dd class="col-sm-9">[^<]+', html1)
        kategorija = b1[0].split('">')[1]
        
        c1 = re.findall(r'<a href="/animals/location/[^<]+', html1)
        lokacija = []
        for j in range(len(c1)):
            lokacija.append(c1[j].split('">')[1])
        if 'Lifespan</dt>' in html1:
            d1 = re.findall(r'Lifespan</dt><dd class="col-sm-6">[^<]+', html1)
            zivljenjska_doba = d1[0].split('">')[1]
            zivljenjska_doba = pretvornik_casa(zivljenjska_doba)
        if 'Skin Type</dt>' in html1:
            e1 = re.findall(r'Skin Type</dt><dd class="col-sm-6">[^<]+', html1)
            vrsta_koze = e1[0].split('">')[1]
        if 'Diet</dt>' in html1:
            f1 = re.findall(r'Diet</dt><dd class="col-sm-6">[^<]+', html1)
            prehrana = f1[0].split('">')[1]
        if 'Predators</dt>' in html1:
            g1 = re.findall(r'Predators</dt><dd class="col-sm-6">[^6]+', html1)
            if 'a href' in g1[0]:
                aa = g1[0].replace('Predators</dt><dd class="col-sm-6">', '').replace('<a href="https://a-z-animals.com/animals/', '').replace('</a>', '').replace('</dd><dt class="col-sm-', '').replace('</dd', '').split(',')
                plenilci = ''
                for j  in range(len(aa)):
                    if '>' in aa[j]:
                        aa[j] = aa[j].split('>')[1]
                    plenilci += aa[j].lower().strip() + ', '
                plenilci = plenilci[:-2]
            else:
                g1 = re.findall(r'Predators</dt><dd class="col-sm-6">[^<]+', html1)
                plenilci = g1[0].split('">')[1].lower()
            plenilci = plenilci.replace(' and', ',')
        if 'Weight</dt>' in html1:
            h1 = re.findall(r'Weight</dt><dd class="col-sm-6">[^(<]+', html1)
            teza = h1[0].split('">')[1]
            teza = pretvornik_mase(teza)
        if 'Top Speed</dt>' in html1:
            i1 = re.findall(r'Top Speed</dt><dd class="col-sm-6">[^<]+', html1)
            najvisja_hitrost = i1[0].split('">')[1]
            najvisja_hitrost = pretvornih_hitrosti(najvisja_hitrost)
        if 'Height</dt>' in html1: 
            j1 = re.findall(r'Height</dt><dd class="col-sm-6">[^(<]+', html1)
            visina = j1[0].split('">')[1]
            visina = pretvornik_dolzinskih_enot(visina)
        if 'Length</dt>' in html1: 
            k1 = re.findall(r'Length</dt><dd class="col-sm-6">[^(<]+', html1)
            dolzina = k1[0].split('">')[1]
            dolzina = pretvornik_dolzinskih_enot(dolzina)
        if 'Water Type</dt>' in html1: 
            l1 = re.findall(r'Water Type</dt><dd class="col-sm-6"><ul class="list-unstyled"><li class="list-item">[^<]+', html1)
            vrsta_vode = l1[0].split('">')[3]
        tab = [kategorija, lokacija, zivljenjska_doba, vrsta_koze, prehrana, plenilci, teza, najvisja_hitrost, visina, dolzina, vrsta_vode]
        zivali[ime] = tab