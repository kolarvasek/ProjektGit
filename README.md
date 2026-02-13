# Práce s Git a GitHub
## Zadání práce
Tento repozitář si zkopírujte do svého počítače, bude sloužit jako základ projektu. 
Vytvořte si veřejný repozitář na GitHub a propojte ho s lokálním repozitářem, tím co jste si zkopírovali. 
Vypracujte **zadání programu**, zkuste v průbehu trackovat změny pomocí **git commit**. Po vypracování programu napište vlastní README dokument, který bude sloužit jako návod pro zprovoznění vašeho programu (zapojení, stažení souborů, upravení konfiguračního souboru, nahrání na RPI pico...), nezapomeňte na soubor .gitignore, jelikož se v programu nacházi **API klíč, který nesmí být zveřejněn!!**, případně ignoruje soubory generované vývojovým prostředím jako například .vscode . 
Váš výsledek nahrajte do GitHub repozitáře.

### Zadání programu
Program bude zahrnovat práci s API a LCD displejem, soubor **CONFIGURATION.txt** bude ukládat v json formátu údaje pro přihlášení k WiFi a API klíč. Spouštěcí soubor pro program bude main.py, program zhotovte pro platformu raspberry pi pico w.

Každých 10 minut zjišťujte aktuální počasí na aktuální lokaci pomocí API OpenWeatherMap, klíč, který dostanete je omezen na 1000 za den, při testování ostatních částí programu si prosím zkopírujte ukázková JSON data z dokumentace. Aktuální geologickou lokaci si zjistěte pomocí veřejné IP adresy prostřednicvím [IP API](https://ip-api.com), toto API je zdarma a nevyžaduje klíč.

Po zapnutí zařízení se ukáže "Connecting to WiFi", po připojení k síti se na displeji zobrazí na pár sekund aktuální souřadnice, poté bude displej ukazovat data o počasí, která vám přijdou vhodná. 

Zařiďte základní robustnost programu jako automatické připojení k síti po výpadku, či upozornění na špatná data z API.

### Úprava programu
Pomocí funkce fork na GitHub přidejte do kódu vaší dvojice funkcionalitu aktuálního času, na displej přidejte aktuální čas v sekundách synchronizovaného pomocí NTP, případně uvolněte pro tento údaj místo na displeji, poté využijte funkci contribute pro aktualizování repozitáře autora. Ověřte funkčnost.

### Hodnocení
Bude hodnoceno za 5 pouze při neplnění činosti na hodínách Dpr.













### pozor
v github máte tlačítko copilot, umí programovat lépe než chatgpt, tak alespoň využívejte ty správné nástroje.
