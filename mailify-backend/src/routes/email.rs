use axum::{
    extract::{Path, State},
    http::StatusCode,
    Json,
};
use sqlx::MySqlPool;

use crate::models::Email;

pub async fn add_email(
    State(pool): State<MySqlPool>,
    Json(payload): Json<Email>,
) -> Result<Json<Email>, StatusCode> {
    let result = sqlx::query_as!(
        Email,
        "INSERT INTO emails (user_id, subject, receiver, message) VALUES (?, ?, ?, ?)
         RETURNING id, subject, receiver, message",
        payload.user_id, payload.subject, payload.receiver, payload.message
    )
    .fetch_one(&pool)
    .await
    .map_err(|_| StatusCode::BAD_REQUEST)?;

    Ok(Json(result))
}

pub async fn get_emails_by_user(
    State(pool): State<MySqlPool>,
    Path(user_id): Path<i32>,
) -> Result<Json<Vec<Email>>, StatusCode> {
    let emails = sqlx::query_as!(
        Email,
        "SELECT id, subject, receiver, message FROM emails WHERE user_id = ?",
        user_id
    )
    .fetch_all(&pool)
    .await
    .map_err(|_| StatusCode::NOT_FOUND)?;

    Ok(Json(emails))
}
