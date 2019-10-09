-- There is an events table used to track different key activities taken on a website. For this task you need to filter the name field to only show "trained" events. Events should be grouped by the day they happened and counted. The description field is used to distinguish which items the events happened on.

-- "events" Table Schema
-- id
-- name (String)
-- created_at (DateTime)
-- description (String)

SELECT COUNT(name), created_at::date AS day, description
FROM events
WHERE name = 'trained'
GROUP BY day, description
;