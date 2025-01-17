/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - smart_attendance
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`smart_attendance` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `smart_attendance`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add camera_table',7,'add_camera_table'),
(26,'Can change camera_table',7,'change_camera_table'),
(27,'Can delete camera_table',7,'delete_camera_table'),
(28,'Can view camera_table',7,'view_camera_table'),
(29,'Can add college_table',8,'add_college_table'),
(30,'Can change college_table',8,'change_college_table'),
(31,'Can delete college_table',8,'delete_college_table'),
(32,'Can view college_table',8,'view_college_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add notification_table',10,'add_notification_table'),
(38,'Can change notification_table',10,'change_notification_table'),
(39,'Can delete notification_table',10,'delete_notification_table'),
(40,'Can view notification_table',10,'view_notification_table'),
(41,'Can add staff_table',11,'add_staff_table'),
(42,'Can change staff_table',11,'change_staff_table'),
(43,'Can delete staff_table',11,'delete_staff_table'),
(44,'Can view staff_table',11,'view_staff_table'),
(45,'Can add student_table',12,'add_student_table'),
(46,'Can change student_table',12,'change_student_table'),
(47,'Can delete student_table',12,'delete_student_table'),
(48,'Can view student_table',12,'view_student_table'),
(49,'Can add stud_complaint_table',13,'add_stud_complaint_table'),
(50,'Can change stud_complaint_table',13,'change_stud_complaint_table'),
(51,'Can delete stud_complaint_table',13,'delete_stud_complaint_table'),
(52,'Can view stud_complaint_table',13,'view_stud_complaint_table'),
(53,'Can add rating_table',14,'add_rating_table'),
(54,'Can change rating_table',14,'change_rating_table'),
(55,'Can delete rating_table',14,'delete_rating_table'),
(56,'Can view rating_table',14,'view_rating_table'),
(57,'Can add feedback_table',15,'add_feedback_table'),
(58,'Can change feedback_table',15,'change_feedback_table'),
(59,'Can delete feedback_table',15,'delete_feedback_table'),
(60,'Can view feedback_table',15,'view_feedback_table'),
(61,'Can add complaint_table',16,'add_complaint_table'),
(62,'Can change complaint_table',16,'change_complaint_table'),
(63,'Can delete complaint_table',16,'delete_complaint_table'),
(64,'Can view complaint_table',16,'view_complaint_table'),
(65,'Can add collegenotification_table',17,'add_collegenotification_table'),
(66,'Can change collegenotification_table',17,'change_collegenotification_table'),
(67,'Can delete collegenotification_table',17,'delete_collegenotification_table'),
(68,'Can view collegenotification_table',17,'view_collegenotification_table'),
(69,'Can add department',18,'add_department'),
(70,'Can change department',18,'change_department'),
(71,'Can delete department',18,'delete_department'),
(72,'Can view department',18,'view_department');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'smart_app','camera_table'),
(8,'smart_app','college_table'),
(17,'smart_app','collegenotification_table'),
(16,'smart_app','complaint_table'),
(18,'smart_app','department'),
(15,'smart_app','feedback_table'),
(9,'smart_app','login_table'),
(10,'smart_app','notification_table'),
(14,'smart_app','rating_table'),
(11,'smart_app','staff_table'),
(13,'smart_app','stud_complaint_table'),
(12,'smart_app','student_table');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-10-09 09:04:40.513665'),
(2,'auth','0001_initial','2023-10-09 09:04:40.828326'),
(3,'admin','0001_initial','2023-10-09 09:04:40.928209'),
(4,'admin','0002_logentry_remove_auto_add','2023-10-09 09:04:40.937285'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-10-09 09:04:40.944719'),
(6,'contenttypes','0002_remove_content_type_name','2023-10-09 09:04:40.996270'),
(7,'auth','0002_alter_permission_name_max_length','2023-10-09 09:04:41.030487'),
(8,'auth','0003_alter_user_email_max_length','2023-10-09 09:04:41.047393'),
(9,'auth','0004_alter_user_username_opts','2023-10-09 09:04:41.055392'),
(10,'auth','0005_alter_user_last_login_null','2023-10-09 09:04:41.100695'),
(11,'auth','0006_require_contenttypes_0002','2023-10-09 09:04:41.106118'),
(12,'auth','0007_alter_validators_add_error_messages','2023-10-09 09:04:41.114076'),
(13,'auth','0008_alter_user_username_max_length','2023-10-09 09:04:41.166091'),
(14,'auth','0009_alter_user_last_name_max_length','2023-10-09 09:04:41.204812'),
(15,'auth','0010_alter_group_name_max_length','2023-10-09 09:04:41.222865'),
(16,'auth','0011_update_proxy_permissions','2023-10-09 09:04:41.232579'),
(17,'auth','0012_alter_user_first_name_max_length','2023-10-09 09:04:41.269922'),
(18,'sessions','0001_initial','2023-10-09 09:04:41.299047'),
(19,'smart_app','0001_initial','2023-10-09 09:04:41.723953'),
(20,'smart_app','0002_auto_20231009_1433','2023-10-09 09:04:41.822844'),
(21,'smart_app','0003_department','2023-10-10 06:01:28.581072'),
(22,'smart_app','0004_department_college','2023-10-10 06:27:06.043479');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('m1k122dcf20p2q6yh7qshev7zu4gabrp','eyJsaWQiOjR9:1qq89a:SRW57dOXY4OrjDQXuvEktq1m2dy1VSr_zPLyqDEWx18','2023-10-24 08:31:46.861215');

/*Table structure for table `smart_att_camera_table` */

DROP TABLE IF EXISTS `smart_att_camera_table`;

CREATE TABLE `smart_att_camera_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `no` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_camera_table` */

insert  into `smart_att_camera_table`(`id`,`name`,`no`) values 
(1,'kmocamera',12);

/*Table structure for table `smart_att_college_table` */

DROP TABLE IF EXISTS `smart_att_college_table`;

CREATE TABLE `smart_att_college_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `place` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(20) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_att_college_ta_LOGIN_id_21452216_fk_smart_att` (`LOGIN_id`),
  CONSTRAINT `smart_att_college_ta_LOGIN_id_21452216_fk_smart_att` FOREIGN KEY (`LOGIN_id`) REFERENCES `smart_att_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_college_table` */

insert  into `smart_att_college_table`(`id`,`name`,`place`,`post`,`pin`,`phone`,`email`,`LOGIN_id`) values 
(1,'.kj','sf','rg',222,345456,'rg',4);

/*Table structure for table `smart_att_collegenotification_table` */

DROP TABLE IF EXISTS `smart_att_collegenotification_table`;

CREATE TABLE `smart_att_collegenotification_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notification` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `COLLEGE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_att_collegenot_COLLEGE_id_d12754ae_fk_smart_att` (`COLLEGE_id`),
  CONSTRAINT `smart_att_collegenot_COLLEGE_id_d12754ae_fk_smart_att` FOREIGN KEY (`COLLEGE_id`) REFERENCES `smart_att_college_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_collegenotification_table` */

/*Table structure for table `smart_att_complaint_table` */

DROP TABLE IF EXISTS `smart_att_complaint_table`;

CREATE TABLE `smart_att_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(300) NOT NULL,
  `date` varchar(300) NOT NULL,
  `reply` varchar(300) NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_att_complaint__STUDENT_id_8a7b251d_fk_smart_att` (`STUDENT_id`),
  CONSTRAINT `smart_att_complaint__STUDENT_id_8a7b251d_fk_smart_att` FOREIGN KEY (`STUDENT_id`) REFERENCES `smart_att_student_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_complaint_table` */

/*Table structure for table `smart_att_department` */

DROP TABLE IF EXISTS `smart_att_department`;

CREATE TABLE `smart_att_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `department` varchar(40) NOT NULL,
  `COLLEGE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_att_department_COLLEGE_id_cef1d684_fk_smart_att` (`COLLEGE_id`),
  CONSTRAINT `smart_att_department_COLLEGE_id_cef1d684_fk_smart_att` FOREIGN KEY (`COLLEGE_id`) REFERENCES `smart_att_college_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_department` */

insert  into `smart_att_department`(`id`,`department`,`COLLEGE_id`) values 
(1,'bca',1),
(2,'commerce',1);

/*Table structure for table `smart_att_feedback_table` */

DROP TABLE IF EXISTS `smart_att_feedback_table`;

CREATE TABLE `smart_att_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_att_feedback_t_LOGIN_id_10c71e5e_fk_smart_att` (`LOGIN_id`),
  CONSTRAINT `smart_att_feedback_t_LOGIN_id_10c71e5e_fk_smart_att` FOREIGN KEY (`LOGIN_id`) REFERENCES `smart_att_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_feedback_table` */

insert  into `smart_att_feedback_table`(`id`,`feedback`,`date`,`LOGIN_id`) values 
(1,'sfwr','2023-10-10',4),
(2,'mjyfy','2023-10-10',4);

/*Table structure for table `smart_att_login_table` */

DROP TABLE IF EXISTS `smart_att_login_table`;

CREATE TABLE `smart_att_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(70) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_login_table` */

insert  into `smart_att_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(4,'wef','wefg','college'),
(5,'123','123','staff'),
(6,'minhaj','123','staff'),
(7,'minhaj','123','staff'),
(8,'jazmiya','123','student'),
(9,'jazmiya','123','student'),
(10,'jasmiya','123','student');

/*Table structure for table `smart_att_notification_table` */

DROP TABLE IF EXISTS `smart_att_notification_table`;

CREATE TABLE `smart_att_notification_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notification` varchar(200) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_notification_table` */

insert  into `smart_att_notification_table`(`id`,`notification`,`date`) values 
(1,'DG','2023-10-10');

/*Table structure for table `smart_att_rating_table` */

DROP TABLE IF EXISTS `smart_att_rating_table`;

CREATE TABLE `smart_att_rating_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_att_rating_tab_LOGIN_id_495f8080_fk_smart_att` (`LOGIN_id`),
  CONSTRAINT `smart_att_rating_tab_LOGIN_id_495f8080_fk_smart_att` FOREIGN KEY (`LOGIN_id`) REFERENCES `smart_att_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_rating_table` */

insert  into `smart_att_rating_table`(`id`,`rating`,`date`,`LOGIN_id`) values 
(1,4,'2023-10-10',4);

/*Table structure for table `smart_att_staff_table` */

DROP TABLE IF EXISTS `smart_att_staff_table`;

CREATE TABLE `smart_att_staff_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `place` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(30) NOT NULL,
  `age` int NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_att_staff_tabl_LOGIN_id_d7466fbd_fk_smart_att` (`LOGIN_id`),
  CONSTRAINT `smart_att_staff_tabl_LOGIN_id_d7466fbd_fk_smart_att` FOREIGN KEY (`LOGIN_id`) REFERENCES `smart_att_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_staff_table` */

insert  into `smart_att_staff_table`(`id`,`name`,`place`,`post`,`pin`,`phone`,`email`,`age`,`LOGIN_id`) values 
(1,'mnn','mb','b',673582,9645963294,'jazmiyajaz@gmail.com',20,6),
(2,'mnn','mb','b',673582,9645963294,'jazmiyajaz@gmail.com',20,7);

/*Table structure for table `smart_att_stud_complaint_table` */

DROP TABLE IF EXISTS `smart_att_stud_complaint_table`;

CREATE TABLE `smart_att_stud_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(300) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(200) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_att_stud_compl_STAFF_id_8bb0f975_fk_smart_att` (`STAFF_id`),
  KEY `smart_att_stud_compl_STUDENT_id_125f2773_fk_smart_att` (`STUDENT_id`),
  CONSTRAINT `smart_att_stud_compl_STAFF_id_8bb0f975_fk_smart_att` FOREIGN KEY (`STAFF_id`) REFERENCES `smart_att_staff_table` (`id`),
  CONSTRAINT `smart_att_stud_compl_STUDENT_id_125f2773_fk_smart_att` FOREIGN KEY (`STUDENT_id`) REFERENCES `smart_att_student_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_stud_complaint_table` */

/*Table structure for table `smart_att_student_table` */

DROP TABLE IF EXISTS `smart_att_student_table`;

CREATE TABLE `smart_att_student_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `post` varchar(30) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `department` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_att_student_ta_LOGIN_id_c1998ac0_fk_smart_att` (`LOGIN_id`),
  CONSTRAINT `smart_att_student_ta_LOGIN_id_c1998ac0_fk_smart_att` FOREIGN KEY (`LOGIN_id`) REFERENCES `smart_att_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smart_att_student_table` */

insert  into `smart_att_student_table`(`id`,`fname`,`lname`,`place`,`post`,`pin`,`phone`,`department`,`email`,`LOGIN_id`) values 
(1,'jazmiya','jaz','omassery\r\ncalicut','kobh',123344,987765652,'2','jazmiyajaz@gmail.com',10);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
