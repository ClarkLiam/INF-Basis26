--A2
--a: relativ wenige Dopplungen
--b: Datum/Note
--c: Name
--d: Nr einfügen

--A3
SELECT Name, Vorname, GebDat
FROM benutzer
ORDER BY GebDat DESC;

--A4
SELECT Name, Vorname, Email
FROM bwenutzer
WHERE ort = 'Pirmasens';

--A5
SELECT Nutzer
FROM bild
WHERE Name = 'bus.jpg';

--A6
SELECT Name, Vorname
FROM benutzer
WHERE Email LIKE '%@oohay.de' AND ort = 'Trier';

--A7
SELECT Name, Vorname
FROM benutzer
WHERE Strasse IS NULL OR HausNr IS NULL OR Ort IS NULL;

--A8
SELECT Name
FROM gruppe
WHERE Name Like '%FCK%'
ORDER By Name DESC;

--A9
SELECT Name, Vorname, Email, GebDat
FROM benutzer
WHERE GebDat < '1980-01-01';