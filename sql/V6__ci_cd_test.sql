-- CI/CD approval test
ALTER TABLE users
ADD COLUMN ci_test BOOLEAN DEFAULT true;
