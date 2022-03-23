DROP TABLE IF EXISTS messages;

CREATE TABLE messages(
  message_id    TEXT UNIQUE NOT NULL,
  message_text  TEXT NOT NULL,
  PRIMARY KEY(message_id)
)WITHOUT ROWID;