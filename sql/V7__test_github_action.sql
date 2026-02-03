CREATE TABLE IF NOT EXISTS test_verification (
    id SERIAL PRIMARY KEY,
    test_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO test_verification (test_name)
VALUES ('github_action_test');