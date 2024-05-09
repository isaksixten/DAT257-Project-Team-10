CREATE TABLE Farms (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    rating FLOAT, 
    latitude REAL,
    longitude REAL,
    address TEXT,
    website TEXT,
    phonenumber TEXT
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

--Här under finns en bas för att senare kunna lägga in öppettider--

CREATE TABLE Weekdays(
    weekday INT PRIMARY KEY,
    CHECK (weekday = 1 OR weekday = 2 OR weekday = 3 OR weekday = 4 OR weekday = 5 OR weekday = 6 OR weekday = 7)
);

INSERT INTO Weekdays (weekday) VALUES 
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7);

CREATE TABLE Opening_Hours(
    farm TEXT,
    weekday INT,
    open_time INT,
    close_time INT,
    PRIMARY KEY (farm,weekday),
    FOREIGN KEY (farm) REFERENCES Farms(id),
    FOREIGN KEY (weekday) REFERENCES Weekdays(weekday)    
);

--Och här under finns en bas för att kunna lägga in produkter--

CREATE TABLE Products(
    product TEXT PRIMARY KEY
);

CREATE TABLE Farm_Products(
    farm TEXT,
    product TEXT,
    PRIMARY KEY (farm,product),
    FOREIGN KEY (farm) REFERENCES Farms(id),
    FOREIGN KEY (product) REFERENCES Products(product)
);