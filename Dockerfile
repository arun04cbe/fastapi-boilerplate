FROM python:3.12-bookworm

RUN pip install uv

WORKDIR /src

COPY pyproject.toml uv.lock ./
COPY src ./src

RUN uv sync

CMD ["uv", "run", "src/main.py"]

EXPOSE 8000