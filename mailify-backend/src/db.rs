use sqlx::MySqlPool;

pub async fn establish_connection() -> MySqlPool {
    let database_url = std::env::var("DATABASE_URL").expect("DATABASE_URL must be set");
    MySqlPool::connect(&database_url)
        .await
        .expect("Failed to connect to the database")
}
