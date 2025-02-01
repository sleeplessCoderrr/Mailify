use serde::{Deserialize};

#[derive(Deserialize)]
pub struct AuthRequest {
    pub email: String,
    pub password: String,
}