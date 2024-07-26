-- List all tables in the database passed as an argument
SELECT TABLE_NAME
FROM information_schema.tables
WHERE table_schema = DATABASE();
