CREATE TABLE Farms (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    latitude REAL,
    longitude REAL
);

CREATE TABLE Tags (
    tag TEXT PRIMARY KEY
);

CREATE TABLE Farm_Tags(
    farm TEXT,
    tag TEXT,
    PRIMARY KEY (farm, tag),
    FOREIGN KEY (farm) REFERENCES Farms(id),
    FOREIGN KEY (tag) REFERENCES Tags(tag)
);

CREATE TABLE Farm_Information(
    farm TEXT PRIMARY KEY,
    adress TEXT,
    phone_nr TEXT,
    rating FLOAT,
    website TEXT,
    FOREIGN KEY (farm) REFERENCES Farms(id)
);
