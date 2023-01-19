CREATE TABLE IF NOT EXISTS `parentservices`(
    `id` int NOT NULL AUTO_INCREMENT,
    `service` varchar(60),
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`),
    CHECK (`is_deleted` IN (0,1))
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `servicetypes`(
    `id` int NOT NULL AUTO_INCREMENT,
    `parent_service_id` int,
    `name` varchar(255) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
    `amount` float null default 0.0,
    PRIMARY KEY (`id`),
    CHECK (`is_deleted` IN (0,1)),
    FOREIGN KEY (`parent_service_id`) REFERENCES `parentservices` (`id`) ON DELETE CASCADE
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `subservices`(
    `id` int NOT NULL AUTO_INCREMENT,
    `servicetype_id` int,
    `name` varchar(255) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
    `amount` float null default 0.0,
    PRIMARY KEY (`id`),
    CHECK (`is_deleted` IN (0,1)),
    FOREIGN KEY (`servicetype_id`) REFERENCES `servicetypes` (`id`) ON DELETE CASCADE
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
