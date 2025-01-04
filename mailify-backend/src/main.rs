fn main() {
    println!("Hello, world!");
}
mod db;
mod models;
mod routes;

use axum::{routing::post, Router};
use dotenvy::dotenv;
use routes::{auth::*, email::*};
use std::net::SocketAddr;

#[tokio::main]
async fn main() {
    dotenv().ok();
    let pool = db::establish_connection().await;

    let app = Router::new()
        .route("/register", post(register_user))
        .route("/login", post(login_user))
        .route("/emails", post(add_email))
        .route("/emails/:user_id", post(get_emails_by_user))
        .with_state(pool);

    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    println!("Server running at http://{}", addr);

    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}
