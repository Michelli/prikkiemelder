# Wanneer mag ik me vaccineren?

Geschreven naar aanleiding van de [vaccinatiemelder van Nu.nl](https://www.nu.nl/coronavaccins/6136069/wanneer-word-ik-gevaccineerd-krijg-een-melding-als-je-aan-de-beurt-bent.html), omdat ik geen zin had in pushmeldingen van Nu.nl.

Het is een simpel script dat de RSS feed van het RIVM uitleest. Tot nu toe gebruikt het RIVM in de titels van deze berichten steeds hetzelfde patroon, dus heb ik ervoor gekozen om een regular expression te gebruiken met een positive lookahead. Vervolgens checkt het script wat het hoogste jaartal is (bijvoorbeeld 1975). Deze waarde wordt vervolgens gepubliceerd naar een MQTT server. 

## Hoe te gebruiken

Vul de gegevens van je MQTT server in in een .env file. Er staat een voorbeeld in deze repo.

## Takenlijst

- [ ] TLS ondersteuning