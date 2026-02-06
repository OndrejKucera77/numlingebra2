# Projekt z předmětu Numerická lineární algebra 2
**Číslo projektu:** 2\
**Téma:** Srovnání SVD a randomizovaného SVD\
**Autor:** Ondřej Kučera KUC0436

Kód je ve formě Jupyter notebooku (*kod.ipynb*). V něm jsou provedena všechna měření na 5 maticích ze SuiteSparse Matrix Collection, všechny buňky už jsou proběhnuté.
Podrobné informace jsou k dispozici v reportu (*report.pdf*).

V případě, že by si uživatel chtěl vyzkoušet měření na vlastní matici, pak musí:
1. Stáhnout matici ze [SuiteSparse Matrix Collection](https://sparse.tamu.edu/) v .mtx formátu, tj. odkazem přes Matrix Market.
2. Přesunout ji do složky *mat*
3. Zde spustit program *preved_matici.py*, ve kterém je potřeba nejprve změnit název matice (bez přípony) a typ matice. Tento program přetvoří matici v .mtx formátu do .npz formátu.
4. V *kod.ipynb* načíst matici v .npz formátu funkcí *load_npz*
5. Provést měření funkcí *process_matrix*.
