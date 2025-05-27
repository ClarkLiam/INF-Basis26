-- A1
-- Mehrere Attribute in einer Zelle

--A2

--A3
SELECT Name, Vorname, GebDat
FROM benutzer
ORDER BY GebDat DESC;

--A4
SELECT Name, Vorname, Email
FROM benutzer
WHERE ort = 'Pirmasens';

--A5
Select Name, Nutzer
FROM bild
WHERE Name = 'bus.jpg';

--A6
SELECT Name, Vorname, Email, Ort
FROM benutzer
WHERE EMail LIKE '%@oohay.de' and ort = 'Trier';

--A7
SELECT Name, Vorname, Strasse, HausNr, Ort
FROM benutzer
WHERE Strasse IS NULL OR HausNr IS NULL OR Ort IS NULL;
