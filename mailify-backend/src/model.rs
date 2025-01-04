use serde::{Deserialize, Serialize};

#[derive(Serialize, sqlx::FromRow)]
pub struct User {
    pub id: i32,
    pub username: String,
}

#[derive(Deserialize)]
pub struct RegisterRequest {
    pub username: String,
    pub password: String,
}

#[derive(Deserialize)]
pub struct LoginRequest {
    pub username: String,
    pub password: String,
}

#[derive(Serialize, sqlx::FromRow)]
pub struct Email {
    pub id: i32,
    pub subject: String,
    pub receiver: String,
    pub message: String,
}
