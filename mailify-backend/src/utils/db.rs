use std::env;
use sqlx::{MySqlPool, Error};

pub async fn connect_db() -> Result<MySqlPool, Error> {
    let database_url = env::var("DATABASE_URL")
        .map_err(|_| Error::Configuration("DATABASE_URL not set".into()))?;
    MySqlPool::connect(&database_url).await
}

