-- how to get the first tweet ffrom user id of 1
select * from users
left join tweets on users.id = tweets.user_id
where users.id = 1;

-- You can just grab the tweets by:
SELECT tweets.tweet FROM users
left JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;

-- Or rename the output column that you want as kobe_tweets by modifying the statement to look like the following:
SELECT tweets.tweet as kobe_tweets
FROM users
left JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;

-- 2. What query would return all the tweets that the user with id 2 has tagged as favorites?
SELECT first_name, tweet
FROM users
LEFT JOIN faves
ON users.id = faves.user_id
left JOIN tweets
ON faves.tweet_id = tweets.id
WHERE users.id = 2;

-- 3. What query would you run to get all the tweets that user with id 2, or user with id 1, has tagged as favorites?
SELECT first_name, tweet
FROM users
left JOIN faves
ON users.id = faves.user_id
left JOIN tweets
ON faves.tweet_id = tweets.id
WHERE users.id = 1 or users.id = 2;
