# ResuNews

Aplicació per a resumir noticies en base a una url amb el model bart-large-cnn de Meta

## Com s'utilitza
1. pip install -r requirements.txt
2. python.exe .\main.py
3. uvicorn main:app --reload

## Aspectes de programació
### Llibreries utilitzades:
- **FastAPI**: Framework de Python per a crear APIs web d'alta velocitat. L'utilitzem per crear el servidor web i gestionar les peticions HTTP.
- **Uvicorn**: Servidor ASGI d'alt rendiment que permet executar aplicacions FastAPI. És necessari per executar la nostra aplicació web.
- **Transformers**: Llibreria de Hugging Face que proporciona accés a models pre-entrenats. En aquest cas, l'utilitzem per carregar i utilitzar el model BART per a la generació de resums.
- **Newspaper3k**: Llibreria especialitzada en l'extracció de contingut d'articles de notícies. Ens permet obtenir el text net d'una URL de notícia.
- **Torch**: Framework de deep learning necessari per executar els models de Transformers. És requereix per al model BART.

### Paràmetres del model:
- **max_length**: Longitud màxima (en tokens) del resum generat. En el nostre cas està configurat a 500 per obtenir resums detallats però concisos.
- **min_length**: Longitud mínima del resum. Establert a 100 per assegurar que el resum tingui prou contingut.
- **temperature**: Controla la creativitat/aleatorietat en la generació del text.
- **top_p**: Paràmetre de nucleus sampling que controla la diversitat del text generat, practicament com la temperatura.   
- **top_k**: Fa referència als tokens de resposta més probables, per exemple un top_k:50 fara que el model utilitze sols els 50 tokens més probables.

### FlowChart:
```mermaid
flowchart TD
    A[Objecte FastAPI app] -->|GET /| B[FastAPI Server]
    B -->|Retorna| C[summarizer.html]
    
    A -->|POST /resumir| D[FastAPI Endpoint]
    D -->|Crea Objecte article| E[newspaper.Article]
    E -->|Descarrega| F[article.download]
    F -->|Parseja| G[article.parse]
    G -->|Extrau el text| H{Text disponible ? }
    
    H -->|No| I[Retorna error]
    H -->|Yes| J[Objecte del model Bart summarizer]
    J -->|Procesa el text| K[Genera Resum]
    
    style B fill: #145a32 
    style D fill: #145a32 
    style J fill: #9a7d0a 
```

### Usar un model en local o una API:
En aquest cas estem treballant desde un model en local ja que l'us d'una API pot suposar un cost adicional ja que estaras utilitzant els recursos de una altra maquina per a processar les dades. L'us d'una API es necessari al utilitzar grans models que no poden correr a qualsevol maquina (model de raonament, de generacio d'imatges etc) pero per a aquest petit projecte de resumidor de noticies no es necessari ja que no consumeix gaire recursos i dona un bon rendiment.

### Recuros utilitzats:
El model facebook/bart-large-cnn pesa uns 2GB de memoria en disc i te 406M de parametres. Al executarlo per a resumir una noticia utilitza uns 2GB de RAM i utilitza la CPU en lloc de la GPU.

## Proves realitzades:
