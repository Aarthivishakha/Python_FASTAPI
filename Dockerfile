FROM buildpack-deps:bookworm AS python-builder

RUN git clone --depth 1 https://github.com/python/cpython.git /usr/src/cpython
WORKDIR /usr/src/cpython
RUN ./configure --prefix=/opt/python --enable-shared --with-ensurepip=install \
    && make -j2 \
    && make install

FROM debian:bookworm-slim AS runtime

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates libbz2-1.0 libffi8 libgdbm6 liblzma5 libncursesw6 \
       libreadline8 libsqlite3-0 libssl3 tk zlib1g \
    && rm -rf /var/lib/apt/lists/*

COPY --from=python-builder /opt/python /opt/python

ENV PATH="/opt/python/bin:$PATH" \
    LD_LIBRARY_PATH="/opt/python/lib" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /service

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir --upgrade pip \
    && python3 -m pip install --no-cache-dir -r requirements.txt

COPY app ./app
RUN addgroup --system app && adduser --system --ingroup app app \
    && chown -R app:app /service
USER app

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python3 -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health')"

CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
