use axum::{
    extract::State,
    http::StatusCode,
    Json,
};

use bcrypt::{hash, verify};
use sqlx::MySqlPool;
use crate::models::{AuthRequest, User};

pub async fn register_user(                 
    State(pool): State<MySqlPool>,
    Json(payload): Json<AuthRequest>,
) -> Result<Json<User>, StatusCode> {
    let hashed_password = hash(payload.password, 4).map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;

    let result = sqlx::query!(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        payload.username,
        hashed_password
    )
    .execute(&pool)
    .await
    .map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;
    
    
    let last_insert_id = result.last_insert_id();  
    

    Ok(Json(result))
}

pub async fn login_user(
    State(pool): State<MySqlPool>,
    Json(payload): Json<AuthRequest>,
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
