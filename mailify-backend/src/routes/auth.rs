use serde::Serialize;
use sqlx::mysql::MySqlPool;
use axum::response::IntoResponse;
use axum::extract::{Json, Extension};

use crate::models::auth_request::{AuthRequest};
use crate::models::auth_response::{AuthResponse};

pub async fn login(
    Json(payload): Json<AuthRequest>,
    Extension(pool): Extension<MySqlPool>
) -> impl IntoResponse {
    if payload.email == "admin" && payload.password == "password" {
        Json(AuthResponse{
            message: "Login successful".to_string()
        }).into_response()
    } else {
        Json(AuthResponse{
            message: "Login failed".to_string()
        }).into_response()
    }
}