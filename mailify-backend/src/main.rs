mod utils;
mod routes;
mod models;

use tokio;
use dotenv::dotenv;

use routes::auth::login;
use utils::db::connect_db;

use sqlx::mysql::MySqlPool;
use axum::{Router, routing::post};
use tower::ServiceBuilder;
use tower_http::add_extension::AddExtensionLayer;


#[tokio::main]
async fn main() {
    dotenv().ok();

    let pool = connect_db()
        .await.expect("Failed to connect to the database");  

    let app = Router::new()
        .route("/login", post(login))
        .layer(AddExtensionLayer::new(pool));

    axum::Server::bind(&"127.0.0.1:3000".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();

    println!("Server running at http://127.0.0.1.3000");
}
