use serde::{Deserialize, Serialize};

#[derive(Serialize, sqlx::FromRow)]
pub struct User {
    pub id: i32,
    pub username: String,
    pub password_hash: String,
}

#[derive(Deserialize)]
pub struct AuthRequest {
    pub username: String,
    pub password: String,
}

#[derive(Serialize, sqlx::FromRow)]
pub struct Email {
    pub id: i32,
    pub subject: Option<String>, 
    pub receiver: Option<String>,
    pub message: Option<String>,
}
