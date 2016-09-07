# pythonlab
Marias #100tjejerkodar Python-lab.

Uppgift:
Tutorial: Onsdag: Python
Programmet du ska skriva:
Du har precis startat företag som säljer robotar som du byggt hemma. Du har räknat ut hur mycket du måste sälja dem för för att gå med vinst, nu saknas bara att summera priset för alla varor och lägga på momsen. Skriv ett program för detta.
En kund vill köpa: Två robotar (900 kr/st),  en instruktionsbok (100 kr/st)
När du räknar ut det, kom ihåg att böcker har 6% moms, inte 25%

Att göra:
*Nu vill jag att ni gör samma sak som jag gjorde, och börjar med det enkla enradsprogrammet och sedan lägger till en sak i taget*
Glöm inte att köra programmet mellan varje steg för att upptäcka fel 
på en gång
Titta noga på felmeddelandena, ofta så finns det ledtrådar i form av radnummer om vad som har gått fel och på vilken rad
Börja med att göra ett nytt repository på Github. Lättast är att göra det på webbplatsen, och sedan kör clone till en ny mapp precis som förut
Github.com -> Skapa ett repo med plustecknet längst upp till höger
Hitta på ett namn, välj att du vill ha en README
Lägg till en .gitignore för Python
Starta sedan Github-programmet, och välj plustecknet uppe till vänster
Välj clone, välj ditt repo, och välj var på hårddisken du vill lägga filerna

#1 Startprogrammet:
print(900 * 2 * 1.25 + 100 * 1.06)
Lägg in det i en pythonfil och kör den i terminalen, vad blir resultatet?


När vi behöver ändra siffrorna in är det svårt att komma ihåg var alla siffror betyder, så vi ska förbättra vårt program genom att lägga till variabler:
Ge alla variabler beskrivande namn (t.ex. robot_price)
Variabler försvinner så fort programmet har kört klart, finns bara temporärt som en hjälp för oss
#2 Skriv om programmet med variabler!
Exempel:
robot_price = 900
print(robot_price * 2 * 1.25 + 100 * 1.06)
Se till att alla siffror på sista raden är borta och att du använder variabler för dem istället


Problem: Blir lätt väldigt många variabler. Istället kan man lagra flera värden i en variabel med Listor och Dictionaries:
Listor: spara flera värden i en variabel: all_customers = [22, 32, 52]
Hämta ut det första värdet: all_customers[0]
Du får tillbaka 22
Hämta ut det andra värdet: all_customers[1]
Du får tillbaka 32
Hämta ut det tredje värdet: all_customers[2]
Du får tillbaka 52
Dictionaries: lika listor men istället för siffror använder man strängar för att slå upp ett värde:
Vad är en sträng?
"Det här är en sträng" <- citattecken runt om
'Det här är en sträng' <- går lika bra med enkla citattecken
Strängar kan lagras i variabler precis lika lätt som siffror:
message = "Hej programmerare!"
Exempel på en dictionary:
customers_by_name = { "bob": "45", "anne": "25" }
Vad har bob för kundnummer? customers_by_name["bob"]
Vad har anne för kundnummer? customers_by_name["anne"]
#3 Skriv om programmet med dictionaries
Exempel:
robot = {"price": 900, "count": 2, "tax": 1.25}
print(robot["price"] * 2 * 1.25 + 100 * 1.06)
Se till att alla siffror på sista raden är borta och att du använder en dictionary per vara istället


Problem: Att använda dictionaries för något som alltid har exakt samma värden känns lite onödigt. Finns det inte någon struktur som är lite mer fast, där man bara har just de tre värdena vi har att välja bland? Klasser to the rescue!
Klass: ett slags recept som man kan skapa större behållare av. Lika dictionaries, men ännu mer flexibla.
#4 Skriv om programmet med en klass
Exempel:
class Product:
    price = 0
    count = 0
    tax = 1
robot = Product()
robot.price = 900
robot.count = 2 …
Se till att du använder ett objekt för alla värden på sista raden.


Problem: Snyggare om produkten själv kunde räkna ut sitt pris, så vi bara kunde hämta det, skulle göra det enklare att lägga till nya produkter. Därför ska vi lägga till en metod
En metod är en behållare, inte för data som vi tidigare sett, utan för kod. Ett sätt att samla kod man vill köra flera gånger. Gör att köra koden "anropar" man den. 
En metod kan vara hur många rader kod som helst (men försök att inte ha dem så långa)
#5 Skriv om programmet med klass och metod
Exempel:
class Product:
    def price_with_tax(self):
        return self.price * self.count * self.tax
Se till att alla siffror på sista raden är borta och att du anropar en metod på ditt produktobjekt istället


Problem: Många rader för att skapa en produkt och sätta alla värden rätt. Istället för att först skapa objektet, och sen sätta värden på det, skicka med värdena när objektet skapas. Kan göras genom att man definierar en speciellt metod som heter __init__ (två understreck före och efter säger att den är "magisk").
#6 Skriv om programmet med klass med konstruktor
Exempel:
class Product:
    def __init__(self, price, count, tax):
        self.price = price
        …
robot = Product(price=900, count=2, tax=1.25) …
Se till att alla du skapar dina objekt med __init__ istället för att sätta dem en och efter i efterhand


Problem: Fortfarande lite jobbigt att lägga till en produkt. Borde vi inte kunna använda en lista för produkterna istället för en massa variabler?
#7 Skriv om programmet med lista av produkter
Exempel:
products = [Product(price=900, …), Product(price=100, …)]
total_price = products[0].price_with_tax() + …
Se till att dina produkter lagras i en lista istället för att ha en variabel per produkt


Problem: Jobbigt att komma ihåg att lägga till produkten på total_price-raden. Vi lägger till en for-loop istället
Loopar är till för att göra något för varje sak i en lista eller dictionary. Vi har en lista med produkter, vi vill räkna ut priset för varje produkt, det är perfekt användning av en loop. Några exempel på loopar:
items = [1, 2, 5]
for item in items:
    print(item)
dictionary = {"nyckel1": "värde1", "nyckel2": "värde2"}
for key, value in dictionary.items():
    print(key + " / " + value)
#8 Skriv om programmet med for-loop
Exempel:
products = [...]
total_price = 0
for product in products:
    total_price += product.price_with_tax()
print(total_price)


Problem: Säg att vi kommer på att vi vill ha 10% rabatt på alla varor som kostar mer än 500 kr. Vi behöver på något sätt göra en extra beräkning om ett värde är större än en viss gräns. Det är ett typexempel på en if-sats.
Exempel på if-satser:
if variable > 5: print("variabel är för stor!")
if variable > 5 or variable2 < 10: print("variabel är precis lagom!")
if x < 5: print("x är för liten")
elif x > 5: print("x är för stor")
else: print("x är lagom")
#9 Skriv om programmet med rabatt
Exempel:
def price_with_tax(self):
    total = self.price * self.count * self.tax
    if total > 500:
        return 0.9 * total
    else:
        return total
Använd en if-sats för att ge 10% rabatt om en varas pris är mer än 500


Men förstår ni programmet såhär långt så kan ni python. BRA JOBBAT!



Som vanligt är extrauppgifterna frivilliga, om du istället vill jobba vidare på HTML och CSS så går det förstås finfint. Välj själv!

Extrauppgift 1: Lägg till en produkt
Hitta på en ny produkt, med pris, antal och momssats och lägg till den.
Stämmer det nya totalpriset med vad du trodde?

Extrauppgift 2: Ge produkterna namn
Börja med att ge varje produkt ett namn, genom att lägga till "name" i Product-klassen
När du skapar en ny Product, se till att du sätter name="produktens namn" på varje produkt i listan
Lägg till en extra loop längst ner i programmet som skriver ut namnet på varje produkt plus priset för just den produkten:
for product in products:
    print(product.name, product.price_with_tax())
Kör programet, får du en lista på de produkter du förväntar dig?

Extrauppgift 3: Använd en "list comprehension" för att summera totalpriset snyggare
Googla på "python list comprehension" och läs på vad det är
Genom att använda en list comprehension kan du skapa en lista med alla priser som olika produkter har. Prova att skriva ut den listan i terminalen, det borde bli något i stil med: [2025.0, 106.0]
Ersätt raden med total_price, med:
total_price = sum( [din list comprehension här] )
Blev det snyggare? Lättare att läsa?

