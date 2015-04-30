# dmoz_csv
A python script to convert DMOZ content.rdf.u8.gz into a CSV file. It also includes the output CSV file generated from it. 

The structure of the file is
<URL><Category1 for the URL><Category2 for the URL><Category1 for the URL>............<CategoryN for the URL>

Example:

http://www.demus.it/

is in

DMOZ Categories (1-4 of 4)
Business: Food and Related Products: Beverages: Coffee (1)
Regional: Europe: Italy: Regions: Friuli-Venezia Giulia: Localities: Trieste: Business and Economy (1)
World: Italiano: Affari: Alimentazione e Prodotti Correlati: Bevande: Caffè (1)
World: Italiano: Regionale: Europa: Italia: Friuli-Venezia Giulia: Provincia di Trieste: Località: Trieste: Affari e Economia (1)

The corresponding line for it will be generated as:

"http://www.demus.it/","Top/Regional/Europe/Italy/Friuli-Venezia_Giulia/Localities/Trieste/Business_and_Economy","Top/World/Italiano/Affari/Alimentazione_e_Prodotti_Correlati/Bevande/Caffè","Top/World/Italiano/Regionale/Europa/Italia/Friuli-Venezia_Giulia/Provincia_di_Trieste/Località/Trieste/Affari_e_Economia","Top/Business/Food_and_Related_Products/Beverages/Coffee"
