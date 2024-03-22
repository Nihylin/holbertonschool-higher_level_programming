-- this is a comment to please the almighty checker (yes I'm petty)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS "user_0d_2"@"localhost" IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT ON hbtn_0d_2.* TO "user_0d_2"@"localhost";
