FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-latex-extra \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.2
RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.in-project true \
    && poetry install --no-interaction --no-root

COPY generate_pdf.py .
COPY latex.py .
COPY usage.py .

RUN mkdir -p artifacts

CMD ["poetry", "run", "python", "generate_pdf.py"]