-- Query to list all tables in the specified database
SELECT TABLE_NAME
FROM information_schema.tables
WHERE table_schema = 'alx_book_store';
