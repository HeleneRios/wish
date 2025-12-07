CREATE TABLE
    "games" (
        "game_id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "title" TEXT NOT NULL,
        "publisher" INTEGER NOT NULL,
        "main_hours" INTEGER,
        "side_hours" INTEGER,
        "lowest_price" INTEGER,
        "considered_price" INTEGER NOT NULL,
        "rating" TEXT NOT NULL,
        "notes" TEXT,
        FOREIGN KEY ("publisher") REFERENCES "publishers" ("publisher_id")
    );

CREATE TABLE
    "publishers" (
        "publisher_id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "name" TEXT NOT NULL UNIQUE
    );

CREATE TABLE
    "genres" (
        "genre_id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "genre" TEXT NOT NULL UNIQUE
    );

CREATE TABLE
    "genres_junction" (
        "game_id" INTEGER,
        "genre_id" INTEGER,
        PRIMARY KEY ("game_id", "genre_id"),
        FOREIGN KEY ("game_id") REFERENCES "games" ("game_id"),
        FOREIGN KEY ("genre_id") REFERENCES "genres" ("genre_id")
    );