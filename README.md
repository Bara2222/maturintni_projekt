# Maturitní projekt
# **Závěrečný projekt IT4 – SmartTrainer**

**Aplikace pro tvorbu a sledování tréninkových plánů**

---

## 🔍 **Popis projektu**

**SmartTrainer** je interaktivní aplikace zaměřená na uživatele, kteří si chtějí vytvářet vlastní tréninkové plány, sledovat svůj progres a mít přehled o svých aktivitách. Cílem je vytvořit moderní, uživatelsky přívětivý nástroj dostupný na mobilních zařízeních nebo ve webovém prohlížeči.

---

## 🎯 **Cíle projektu**

* Navrhnout a vytvořit přehlednou a intuitivní aplikaci pro plánování tréninků.
* Umožnit uživatelům personalizovat si své tréninky dle:

  * obtížnosti (začátečník, pokročilý, expert),
  * typu cvičení (kardio, síla, protažení atd.),
  * časových možností.
* Poskytnout databázi cviků s informacemi jako:

  * název, popis, kategorie (typ cviku), video nebo obrázek, doporučený počet opakování nebo čas.
* Implementovat časovač pro řízení tréninkových jednotek (intervaly, pauzy).
* Zajistit historii tréninků a statistiky – sledování pokroku, opakování tréninků.
* Zavést uživatelskou autentizaci (registrace/přihlášení) a ukládání dat v cloudu.
* Optimalizovat UI pro mobilní i desktopová zařízení (responzivní design).

---

## 🔧 **Hlavní funkce aplikace**

1. ### **Registrace a přihlášení**

   * Vytvoření účtu / přihlášení.
   * Ukládání osobních tréninků, historie a statistik.

2. ### **Tvorba tréninkových plánů**

   * Výběr cviků z databáze (název, popis, obrázek/video).
   * Možnost zadat:

     * Počet sérií, počet opakování, délku trvání (pro cviky typu plank apod.).

3. ### **Nastavení obtížnosti**

   * Výběr úrovně: **Začátečník / Pokročilý / Expert**.
   * Úroveň ovlivňuje:

     * Počet cviků, série, délku pauzy, intenzitu tréninku.

4. ### **Časovač (Timer)**

   * Spouštění odpočítávání mezi sériemi a cviky.
   * Možnost **pauzy / restartu** během tréninku.
   * Režim pro **HIIT** a **kruhové tréninky**.

5. ### **Historie tréninků a statistiky**

   * Záznam: datum, délka tréninku, obtížnost, dokončené tréninky.
   * Možnost zopakovat předchozí trénink jedním kliknutím.
   * Statistické grafy pokroku (volitelně).

6. ### **Přednastavené šablony tréninků**

   * Rychlý výběr hotových plánů:

     * „Celé tělo“, „Domácí HIIT“, „Protažení po běhu“, atd.

---

## 🗓 **Harmonogram práce**

| Fáze | Popis                              | Termín  |
| ---- | ---------------------------------- | ------- |
| 1.   | Návrh UI/UX, struktura databáze    |         |
| 2.   | Autentizace uživatelů              |         |
| 3.   | Databáze cviků, tvorba tréninku    |         |
| 4.   | Implementace časovače              |         |
| 5.   | Historie, statistiky               |         |
| 6.   | Testování a opravy                 |         |
| 7.   | Finalizace, dokumentace, odevzdání |         |

---

## 🧠 **Co se chci naučit**

* **Práce s databází** (strukturování, CRUD operace)
* **Autentizace uživatelů**
* **Návrh a vývoj UI/UX**
* **Práce s časem v aplikaci** (časovač, délka tréninku)
* Volitelně: základy mobilního vývoje (React Native / Flutter) 

---

## 🛠 **Použité technologie**

### ✅ Doporučená varianta: **Mobilní aplikace**

* **Frontend:** React Native nebo Flutter
* **Backend:** Firebase (Firestore + Auth)
* **Bonus:** Možnost přehrávání videí u cviků

---

## 📚 **Zdroje a inspirace**

* Open-source workout aplikace na GitHubu
* YouTube tutoriály pro tvorbu React Native aplikací
* Firebase dokumentace
* Figma / Canva pro návrh UI
* Weby jako [Exercisedb.io](https://exercisedb.io) – pro inspiraci u databáze cviků

---




