CREATE TABLE `servicesType`(
    `id` int AUTO_INCREMENT,
    `type_name` varchar(50) unique,
    PRIMARY KEY(`id`)    
);

CREATE TABLE `services`(
    `id` int AUTO_INCREMENT,
    `service_name` varchar(50) unique,
    `price` varchar(5) NOT NULL default '0.0',
    `description` varchar(300) default '',
    `service_type` int,
    FOREIGN KEY (`service_type`) REFERENCES `servicesType`(`id`),
    PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `form_data`(
    `id` int AUTO_INCREMENT,
    `full_name` varchar(100),
    `mobile_no` varchar(15),
    `mail` varchar(30),
    `pan` varchar(13),
    `business_name` varchar(30),
    `aadhar` varchar(15),
    `street_address` varchar(70),
    `locality` varchar(50),
    `city` varchar(50),
    `address` varchar(200),
    `state` varchar(50),
    `district` varchar(50),
    `pincode` varchar(10),
    `remark` varchar(400),
    `status` varchar(20) default 'PENDING',
    `service_id` int,
    `transactionNo` varchar(20),
    `user_id` int,
    `created_at` datetime default current_timestamp NOT NULL,
    `is_deleted` tinyint(1) default 0,
    CHECK (`is_deleted` IN (1, 0)),
    CHECK (`status` IN ('PENDING','ONGOING','COMPLETED')),
    PRIMARY KEY(`id`),
    FOREIGN KEY(`service_id`) REFERENCES `services`(`id`) ON DELETE CASCADE,
    FOREIGN KEY(`user_id`) REFERENCES `user`(`id`) ON DELETE CASCADE,
    FOREIGN KEY(`transactionNo`) REFERENCES `Transactions`(`transaction_number`) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `user`(
    `id` int AUTO_INCREMENT,
    `fname` varchar(50),
    `mname` varchar(50),
    `lname` varchar(50),
    `mail` varchar(50),
    `mobile` varchar(15),
    `password` varchar(15),
    `register_date` TIMESTAMP default CURRENT_TIMESTAMP,
    PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `wallete`(
    `id` int AUTO_INCREMENT,
    `amount` float default 0.0,
    `user_id` int,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`user_id`) REFERENCES `user`(`id`) ON DELETE CASCADE
);

CREATE TABLE `Transactions`(
    `transaction_number` varchar(20),
    `transaction_amount` varchar(10),
    `wallet_id` int,
    `user_id` int,
    `transaction_for` varchar(40),
    `transaction_type` varchar(15),
    `is_deleted` BOOLEAN DEFAULT 0, 
    `created_on` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(`transaction_number`),
    FOREIGN KEY (`user_id`) REFERENCES `user`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`wallet_id`) REFERENCES `wallete`(`id`) ON DELETE CASCADE    
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `documents`(
    `document_name` varchar(40),
    PRIMARY KEY(`document_name`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `service_documents`(
    `id` int AUTO_INCREMENT,
    `service_id` int,
    `document` varchar(40),
    PRIMARY KEY(`id`),
    FOREIGN KEY(`service_id`) REFERENCES `services`(`id`) ON DELETE CASCADE,
    FOREIGN KEY(`document`) REFERENCES `documents`(`document_name`) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `services_administrator` (
    `id` int AUTO_INCREMENT,
    `form_id` int NOT NULL,
    `activity` varchar(255) NOT NULL,
    `file_type` varchar(255) NOT NULL,
    `file` varchar(255) NOT NULL,
    `status` varchar(255) NOT NULL,
    `from_status` varchar(255) NOT NULL,
    `create_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`),
    FOREIGN KEY(`form_id`) REFERENCES `form_data`(`id`) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `sso`(
    `id` int NOT NULL AUTO_INCREMENT,
    `user_id` int,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `status` varchar(250),
    `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`),
    CHECK (`status` IN ('active', 'deactive')),
    CHECK (`is_deleted` IN (0,1)),
    FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;

