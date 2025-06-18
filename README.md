# rocnikovy_projekt
Závěrečný projekt IT 4 : Aplikace pro vytvaření treninků. SmartTrainer

Hlavní funkce:
1. Registrace a přihlášení uživatele
→ Možnost uložit vlastní tréninky, progres.
2.Vytváření vlastních tréninkových plánů
-Výběr cviků (můžeš mít databázi cviků – název, popis, video/obrázek).
-Počet sérií a opakování, případně délka trvání cviku (např. plank 1 min).
3.Volba obtížnosti
-Začátečník, pokročilý, expert (mění se počet cviků, série, pauzy atd.).
4.Časovač
-Odpočítávání mezi sériemi / cviky (pauzy).
-Možnost pauzu / restart během cvičení.
5.Historie tréninků a statistiky
-Datum, dokončené tréninky, délka trvání, obtížnost.
-Možnost „zopakovat“ předchozí trénink.
6.Hotové šablony tréninků
-Např. „Trénink celého těla“, „Domácí HIIT“, „Protažení po běhu“

Cíle projektu:
Navrhnout a vytvořit uživatelsky přívětivou aplikaci, která umožní uživatelům vytvářet, upravovat a sledovat své tréninkové plány podle osobních preferencí, časových možností a úrovně obtížnosti.
Poskytnout databázi cviků s informacemi, jako je název, popis, typ (např. kardio, síla, protažení), doporučená délka nebo počet opakování, případně ilustrační obrázek nebo video.
Implementovat systém pro personalizaci tréninků na základě úrovně obtížnosti (začátečník, pokročilý, expert), typu tréninku (celé tělo, břicho, kardio atd.) a časových možností uživatele.
Zahrnout funkci časovače pro jednotlivé cviky i pauzy mezi nimi, s možností spuštění, pauznutí a restartu – ideální pro HIIT nebo kruhové tréninky.
Umožnit evidenci a historii tréninků, díky které může uživatel sledovat svůj pokrok, zobrazit minulé tréninky a snadno je znovu spustit.
Zajistit základní uživatelskou autentizaci, která umožní každému uživateli ukládat si své tréninky a mít k nim přístup odkudkoli.
Navrhnout responzivní a intuitivní uživatelské rozhraní, které bude použitelné na mobilních zařízeních nebo v prohlížeči.


Harmonogram:

Co se tím chci naučit:
Práce s databází, autentizací, UI/UX.
Plánování a rozvržení aplikace.
Práce s časem (časovač, trvání tréninku).
Volitelně: mobilní vývoj nebo webový framework.

zdroje:

Technologie (příklad):
Varianta A: Mobilní aplikace (Doporučeno)
Frontend: React Native nebo Flutter
Backend: Firebase (Realtime DB / Firestore, autentizace) nebo Node.js + MongoDB
Bonus: Možnost přehrávání videa ke cvikům

Varianta B: Webová aplikace
Frontend: React / Vue / HTML+CSS+JS
Backend: Express (Node.js) + MongoDB / PostgreSQL
Bonus: Responzivní design pro mobil i desktop

Technologie (příklad):
Frontend: React (webová aplikace) nebo React Native / Flutter (mobilní aplikace)
Backend: Node.js + Express, nebo Python Flask/Django
Databáze: MongoDB (NoSQL) nebo PostgreSQL (relational)
Autentizace: Firebase Authentication nebo JWT
Grafy: knihovna jako Chart.js nebo D3.js

