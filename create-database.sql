CREATE DATABASE comic_collector;

CREATE USER comic_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE comic_collector TO comic_admin;