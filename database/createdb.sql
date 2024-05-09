\set QUIET true
SET client_min_messages TO WARNING; -- Less talk please.
-- This script deletes everything in your database
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO CURRENT_USER;
-- This line makes psql stop on the first error it encounters
-- You may want to remove this when running tests that are intended to fail


\ir tables.sql
\ir exampleinserts.sql
\ir views.sql

SELECT * FROM Farms;
SELECT * FROM Farm_Location;
SELECT * FROM Tags;
SELECT * FROM Weekdays