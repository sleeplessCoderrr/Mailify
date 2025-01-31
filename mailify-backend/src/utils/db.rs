use sqlx::{MySqlPool, Error}

pub async fn connect_db() -> MySqlPool{
    let database_url = std::env::var("DATABASE_URL").expect("DATABASE_URL must be set");
    MySqlPool::connect(&database_url).await.expect("Failed to connect to database")
}