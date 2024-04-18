CREATE TABLE Farms (
    id INT PRIMARY KEY,
    name TEXT,
    description TEXT,
    latitude REAL,
    longitude REAL
);

CREATE TABLE Tags (
    tag TEXT PRIMARY KEY
);

CREATE TABLE Farm_Tags(
    farm INT,
    tag TEXT,
    PRIMARY KEY (farm, tag),
    FOREIGN KEY (farm) REFERENCES Farms(id),
    FOREIGN KEY (tag) REFERENCES Tags(tag)
);

CREATE TABLE Owner(
    personalnr INT PRIMARY KEY,
    name TEXT,
    phonenr INT,
    email TEXT
);

CREATE TABLE Farm_Owner(
    farm INT PRIMARY KEY,
    owner INT,
    FOREIGN KEY (farm) REFERENCES Farms(id),
    FOREIGN KEY (owner) REFERENCES Owner(personalnr)
);

CREATE TABLE Products(
    productname TEXT PRIMARY KEY
);

CREATE TABLE Farm_Produces(
    farm INT,
    product TEXT,
    PRIMARY KEY (farm, product),
    FOREIGN KEY (farm) REFERENCES Farms(id),
    FOREIGN KEY (product) REFERENCES Products(productname)
);
