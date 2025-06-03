--A1
--Version A
SELECT BildNr, Kategorie, Name, Inhalt, Nutzer
FROM bild
WHERE Nutzer = 'Vicco von Bülow';
--Version B
SELECT BildNr, Kategorie, Name, Inhalt, Nutzer
FROM bild
WHERE Nutzer LIKE '%Bülow'; --Problem: mehrere Nutzer mit Bülow