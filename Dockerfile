# Osnovna slika s katero zacnemo
FROM python:3.12-slim 

# nastavimo delovno mapo
WORKDIR /app 

# nalozimo meme font (DejaVuSans), run pomeni da zazane to 
RUN apt-get update && apt-get install -y \
    fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

# kopiraj datoteko iz lokalno mapo
COPY requirements.txt .
# nalozi potrebne knjiznice za uporabo aplikacije
RUN pip install --no-cache-dir -r requirements.txt
# kopira vse ostale dototeke v sliko 
COPY . .
# pove na katerem portu je
EXPOSE 5000
# zazene program
CMD ["python", "app.py"]