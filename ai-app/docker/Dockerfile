FROM ubuntu:22.04

# System deps
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    g++ cmake \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python deps
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy source
COPY api ./api
COPY cpp_model ./cpp_model

# Build C++ model
RUN cd cpp_model && \
    mkdir -p build && \
    cd build && \
    cmake .. && \
    make

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
