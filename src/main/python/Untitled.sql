CREATE TABLE `paymentMethod` (
  `id`,
  `name` TEXT(255),
  PRIMARY KEY(id ASC)
);

CREATE TABLE `categoryEx` (
  `id` INTEGER,
  `name` TEXT(255),
  PRIMARY KEY(id ASC)
);

CREATE TABLE `Expences` (
  `id` INTEGER,
  `note` TEXT(255),
  `exp` REAL,
  `expid`INTEGER,
  `ex_date` INTEGER,
  `pay_meth`INTEGER,
  PRIMARY KEY(id ASC)
  FOREIGN KEY (`expid`) REFERENCES `categoryEx` (`id`),
  FOREIGN KEY (`pay_meth`) REFERENCES `paymentMethod` (`id`)
);

CREATE TABLE `categoryIn` (
  `id`INTEGER,
  `name` TEXT(255),
  PRIMARY KEY(id ASC)
);

CREATE TABLE `Intake` (
  `id`INTEGER,
  `note` TEXT(255),
  `intk` REAL,
  `inid`INTEGER,
  `in_date` INTEGER,
  `pay_meth`INTEGER,
  PRIMARY KEY(id ASC)
  FOREIGN KEY (`inid`) REFERENCES `categoryIn` (`id`),
  FOREIGN KEY (`pay_meth`) REFERENCES `paymentMethod` (`id`)
);
