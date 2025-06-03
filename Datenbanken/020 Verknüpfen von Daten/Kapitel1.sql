-- Einstieg
SELECT Name, Vorname, Titel, Strasse, HausNr, Ort, Email, GebDat
FROM benutzer
WHERE Name = 'Lindemann' AND Vorname = 'Erwin';

-- A1
SELECT Name, Vorname, Titel, Strasse, HausNr, Ort, Email, GebDat
FROM benutzer
WHERE Name = 'Lindemann' AND Vorname = 'Erwin' AND ort LIKE 'Bingen%';

-- A2
SELECT Name, Vorname, Titel, Strasse, HausNr, Ort, Email, GebDat
FROM benutzer
WHERE Name = 'Maier' AND Vorname = 'Werner';
-- Problem: es gibt mehrere Einträge in Mainz

