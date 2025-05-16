# Projecte de Resum Automàtic amb IA

## Índex
1. [Definicions Bàsiques](#definicions-bàsiques)
   - [IA Generativa](#ia-generativa)
   - [Model](#model)
   - [Dataset](#dataset)
   - [Entrenar una IA](#entrenar-una-ia)
   - [Fer Inferència d'una IA](#fer-inferència-duna-ia)
   - [RAG](#rag-retrieval-augmented-generation)
   - [Fine-tuning](#fine-tuning)
2. [Aspectes de Programació](#aspectes-de-programació)
   - [Llibreries Python Utilitzades](#llibreries-python-utilitzades)
   - [Paràmetres del Model](#paràmetres-del-model)
   - [Diagrama de Flux](#diagrama-de-flux)
   - [Model Local vs API](#model-local-vs-api)
   - [Recursos Hardware Utilitzats](#recursos-hardware-utilitzats)
3. [Possibilitats i Limitacions](#possibilitats-i-limitacions)
   - [Limitacions del Model BART-CNN](#limitacions-del-model-bart-cnn)
   - [Aplicacions Pràctiques](#aplicacions-pràctiques)
4. [Conclusions](#conclusions)
5. [Referències](#referències)
6. [Ús de la IA en el Desenvolupament](#ús-de-la-ia-en-el-desenvolupament)

## Definicions Bàsiques

### IA Generativa
La Intel·ligència Artificial Generativa és un tipus d'IA capaç de crear contingut nou (text, imatges, música, etc.) a partir de l'aprenentatge de patrons en dades existents. En el nostre cas, utilitzem IA generativa per crear resums de text.

### Model
Un model és una representació matemàtica entrenada per realitzar una tasca específica. En aquest projecte, utilitzem el model BART de Facebook (facebook/bart-large-cnn) especialitzat en resum de text.

### Dataset
Un conjunt de dades estructurat utilitzat per entrenar models d'IA. El model BART que fem servir va ser entrenat amb el dataset CNN/Daily Mail, que conté articles de notícies i els seus resums corresponents.

### Entrenar una IA
El procés d'ajustar els paràmetres d'un model utilitzant un dataset per optimitzar el seu rendiment en una tasca específica. En aquest projecte no entrenem el model, sinó que utilitzem un model pre-entrenat.

### Fer Inferència d'una IA
És el procés d'utilitzar un model entrenat per generar prediccions o outputs. En el nostre cas, fem inferència quan utilitzem el model BART per generar resums de text.

### RAG (Retrieval-Augmented Generation)
Tot i que no l'implementem directament en aquest projecte, RAG és una tècnica que combina la recuperació d'informació amb la generació de text, permetent que els models accedeixin a fonts externes d'informació.

### Fine-tuning
El procés de re-entrenar un model pre-entrenat amb dades específiques del domini. No realitzem fine-tuning en aquest projecte, utilitzem el model tal com ve pre-entrenat.

## Aspectes de Programació

### Llibreries Python Utilitzades
- `fastapi`: Framework per crear APIs web ràpides
- `transformers`: Biblioteca de Hugging Face per accedir i utilitzar models de llenguatge
- `newspaper`: Per extreure contingut d'articles web
- `pydantic`: Per validació de dades
- `uvicorn` (implícit): Servidor ASGI per executar l'aplicació

### Paràmetres del Model
En la nostra implementació utilitzem:
- `max_length`: 500 (longitud màxima del resum)
- `min_length`: 100 (longitud mínima del resum)
- `do_sample`: False (generació determinista)

### Diagrama de Flux
```
URL -> Article (newspaper) -> Text -> Model BART -> Resum
```

### Model Local vs API
En aquest projecte, utilitzem el model localment, el que significa:
- Avantatges:
  - No depenem de serveis externs
  - No tenim costos per ús
  - Menor latència
- Desavantatges:
  - Requereix més recursos locals
  - Limitat a la capacitat del hardware

### Recursos Hardware Utilitzats
- CPU per processar les peticions
- RAM per carregar el model (aproximadament 1.5GB pel model BART)
- Disc dur per emmagatzemar el model

## Possibilitats i Limitacions

### Limitacions del Model BART-CNN
- Límit de 1024 tokens d'entrada
- Optimitzat per articles de notícies
- No manté context complet en textos llargs
- Dependent del domini d'entrenament (notícies)

### Aplicacions Pràctiques
1. **Àmbit Domèstic**
   - Resum de notícies diàries
   - Síntesi de documents llargs

2. **Àmbit Professional**
   - Resum d'informes i documents
   - Monitorització de mitjans
   - Anàlisi de competència

3. **Àmbit Educatiu**
   - Resum de materials d'estudi
   - Síntesi d'articles acadèmics

## Conclusions
El projecte demostra la viabilitat d'implementar un sistema de resum automàtic utilitzant models pre-entrenats. Tot i les limitacions en la longitud del text d'entrada, el sistema proporciona resums útils i coherents, especialment per articles de notícies.

## Referències
- [HuggingFace BART Documentation](https://huggingface.co/facebook/bart-large-cnn)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Newspaper3k Documentation](https://newspaper.readthedocs.io/)

## Ús de la IA en el Desenvolupament
Durant el desenvolupament d'aquest projecte, hem utilitzat models pre-entrenats de HuggingFace, específicament el BART-CNN. La implementació s'ha centrat en la integració d'aquest model en una aplicació web funcional, demostrant l'aplicació pràctica de la IA en el desenvolupament de software.