use axum::{
    extract::State,
    http::StatusCode,
    Json,
};
use bcrypt::{hash, verify};
use sqlx::MySqlPool;

use crate::models::{LoginRequest, RegisterRequest, User};

pub async fn register_user(
    State(pool): State<MySqlPool>,
    Json(payload): Json<RegisterRequest>,
) -> Result<Json<User>, StatusCode> {
    let hashed_password = hash(payload.password, 4).map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;

    let result = sqlx::query_as!(
        User,
        "INSERT INTO users (username, password_hash) VALUES (?, ?) RETURNING id, username",
        payload.username,
        hashed_password
    )
    .fetch_one(&pool)
    .await
    .map_err(|_| StatusCode::CONFLICT)?;

    Ok(Json(result))
}

pub async fn login_user(
    State(pool): State<MySqlPool>,
    Json(payload): Json<LoginRequest>,
) -> Result<Json<User>, StatusCode> {
    let user = sqlx::query_as!(
        User,
        "SELECT id, username, password_hash FROM users WHERE username = ?",
        payload.username
    )
    .fetch_one(&pool)
    .await
    .map_err(|_| StatusCode::UNAUTHORIZED)?;

    if verify(payload.password, &user.password_hash).unwrap_or(false) {
        Ok(Json(user))
    } else {
        Err(StatusCode::UNAUTHORIZED)
    }
}
