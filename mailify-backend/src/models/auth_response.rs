use serde::{Serialize};

#[derive(Serialize)]
pub struct AuthResponse {
    pub message: String,
}