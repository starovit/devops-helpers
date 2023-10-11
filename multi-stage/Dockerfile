# build stage
FROM python:3.8-slim AS builder

WORKDIR /app

COPY generate_data.py .

RUN pip install --no-cache-dir pandas
RUN python generate_data.py

# run stage
FROM python:3.8-slim AS runtime

WORKDIR /app

COPY --from=builder /app/random_data.csv .

CMD ["cat", "random_data.csv"]
