DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    segment TEXT
);

CREATE TABLE transactions (
    tx_id INT PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    tx_time TIMESTAMP,
    amount INT,
    category TEXT
);
CREATE INDEX idx_tx_user ON transactions(user_id);