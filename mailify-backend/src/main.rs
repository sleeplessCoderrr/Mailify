use sqlx::mysql::MySqlPool;
use std::env;
use dotenv::dotenv;
use tokio;

#[tokio::main]
async fn main() {
    dotenv().ok();

    let database_url = env::var("DATABASE_URL").expect("DATABASE_URL must be set");

    match MySqlPool::connect(&database_url).await {
        Ok(_) => println!("✅ Successfully connected to the database!"),
        Err(err) => eprintln!("❌ Failed to connect: {}", err),
    }
}
