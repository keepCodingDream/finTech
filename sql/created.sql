CREATE TABLE `fin_tech_article` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created` datetime DEFAULT NULL,
  `domain` varchar(200) DEFAULT NULL,
  `title` varchar(500) DEFAULT NULL,
  `url` varchar(200) unique,
  `content` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `domain_ix` (`domain`),
  KEY `created_ix` (`created`),
  KEY `url_ix` (`url`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;