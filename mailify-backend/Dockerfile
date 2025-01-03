FROM rust:latest

RUN apt-get update && apt-get install -y libssl-dev pkg-config mysql-client

WORKDIR /app

COPY . .

RUN cargo build --release

CMD ["./target/release/mailify-backend"]
