-- Quick DBD code
CREATE TABLE "Crime_table" (
    "ID" VARCHAR(255),
    "CNTYFIPS" VARCHAR(255),
    "Ori" VARCHAR(30),
    "State" VARCHAR(255),
    "Agency" VARCHAR(255),
    "Agentype" VARCHAR(255),
    "Source" VARCHAR(255),
    "Solved" VARCHAR(30),
    "Year" INT,
    "StateName" VARCHAR(255),
    "Month" VARCHAR(30),
    "Incident" VARCHAR(255),
    "ActionType" VARCHAR(255),
    "Homicide" VARCHAR(255),
    "Situation" VARCHAR(255),
    "VicAge" INT,
    "VicSex" VARCHAR(30),
    "VicRace" VARCHAR(255),
    "VicEthnic" VARCHAR(255),
    "OffAge" INT,
    "OffSex" VARCHAR(30),
    "OffRace" VARCHAR(255),
    "OffEthnic" VARCHAR(255),
    "Weapon" VARCHAR(255),
    "Relationship" VARCHAR(255),
    "Circumstance" VARCHAR(255),
    "Subcircum" VARCHAR(255),
    "VicCount" BIGINT,
    "OffCount" BIGINT,
    "FileDate" VARCHAR(255),
    "MSA" VARCHAR(255)
);

CREATE TABLE "Location_table" (
	"state" VARCHAR(255),
	"latitude" Decimal(8,6) ,
	"longitude" Decimal(9,6),
	"name" VARCHAR(255),
	CONSTRAINT "pk_Location_table" PRIMARY KEY (
    "state" 
		)
);

SELECT ct."State",
	ct."CNTYFIPS",
	ct."Solved",
	ct."Year",
	ct."Month",
	ct."Incident",
	ct."Homicide",
	ct."VicAge",
	ct."VicRace",
	ct."OffAge",
	ct."OffSex",
	ct."Weapon",
	ct."Relationship",
	ct."VicCount",
	ct."OffCount",
	lt."state",
	lt."latitude",
	lt."longitude",
	lt."name"
INTO "Combined_table"
FROM "Location_table" AS lt
INNER JOIN "Crime_table" AS ct
ON lt."name" = ct."State"
