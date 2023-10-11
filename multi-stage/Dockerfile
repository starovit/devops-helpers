# build stage
FROM python:3.8-slim AS build

WORKDIR /app

COPY generate_data.py .
COPY requirements-build.txt .

RUN pip install --user -r requirements-build.txt
RUN python generate_data.py



# run stage
FROM python:3.8-slim AS run

WORKDIR /app

COPY --from=build /app/random_data.csv .
COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
