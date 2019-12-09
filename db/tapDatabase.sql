CREATE TABLE "Locations" (
	"LocationID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Email"	TEXT NOT NULL,
	"TapName"	TEXT NOT NULL DEFAULT 'New Location',
	"Latitude"	INTEGER NOT NULL,
	"Longitude"	INTEGER NOT NULL,
	"IMG"	TEXT,
	"Approved"	BOOL NOT NULL DEFAULT 0,
	CONSTRAINT UniqueCoordinates UNIQUE (Latitude, Longitude)
);

CREATE TABLE "Sessions" (
	"sessionID"	VARCHAR(43) NOT NULL UNIQUE,
	"email"	VARCHAR(255) NOT NULL,
	"IP"	VARCHAR(50) NOT NULL,
	"expiryDT"	DATETIME DEFAULT (datetime(CURRENT_TIMESTAMP,'+60 minutes')),
	PRIMARY KEY("sessionID")
)

CREATE TABLE 'Users' (
'userID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
'accessLevel' VARCHAR(10) NOT NULL DEFAULT 'Standard',
'firstName' VARCHAR(20) NOT NULL,
'lastName' VARCHAR(20) NOT NULL,
'email' VARCHAR(255) NOT NULL UNIQUE,
'hashedPW' CHAR(60) NOT NULL UNIQUE
)

INSERT INTO "main"."Users" ("userID", "accessLevel", "firstName", "lastName", "email", "hashedPW") VALUES ('1', 'Admin', 'Daniel', 'Sparrow', 'sparrowD@cardiff.ac.uk', '$2b$12$0I.qmNymrZNHbWs9OnmZXekiB1eLR9OZYXTv9k.6T63OX6WfyZyOm');
INSERT INTO "main"."Users" ("userID", "accessLevel", "firstName", "lastName", "email", "hashedPW") VALUES ('2', 'Standard', 'Matthew', 'Barnett', 'BarnettMD@cardiff.ac.uk', '$2b$12$.mVYrAaN7kJt4QJE2n/QjeS6zWxXcEhV.5ESaxKq2b.Aph/RfwgTa');
