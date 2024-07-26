-- List all tables in the database provided as an argument
SELECT TABLE_NAME
FROM information_schema.tables
WHERE table_schema = DATABASE();
