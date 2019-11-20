CREATE TABLE "USER" (
	"UserID"	INTEGER,
	"Name"	TEXT,
	"Email"	TEXT,
	PRIMARY KEY("UserID")
);

CREATE TABLE "LOCATIONS" (
	"LocationID"	INTEGER,
	"UserID"	INTEGER,
	"Latitude"	NUMERIC,
	"Longitude"	NUMERIC,
	"Rating"	INTEGER,
	PRIMARY KEY("LocationID")
);
