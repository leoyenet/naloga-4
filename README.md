# Naloga 4 RO
To je projekt za 4 nalogo pri predmetu Razvoj programske opreme.

## Uporaba aplikacije
```sh
git clone https://github.com/leoyenet/naloga-4.git
cd naloga-4
docker build -t meme-generator .
docker run -p 5000:5000 meme-generator
```
- izberite sliko 
- izberite zgornji text
- izberite spodnji text
- pritisni generiraj 
- odpre se nova stran na kateri bo prikazana generirana slika

## Uporaba aplikacije docker-compose
- TODO problem s permissions

```sh
git clone https://github.com/leoyenet/naloga-4.git
cd naloga-4
docker compose up --build

# zaustavitev 
docker compose down
```