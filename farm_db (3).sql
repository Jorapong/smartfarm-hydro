-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2021 at 11:04 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `farm_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `fertilizer`
--

CREATE TABLE `fertilizer` (
  `fertilizer_id` int(10) NOT NULL,
  `fertilizer_name` varchar(100) NOT NULL,
  `fertilizer_value` float NOT NULL,
  `ratifer` int(11) NOT NULL,
  `ratiowater` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `fertilizer`
--

INSERT INTO `fertilizer` (`fertilizer_id`, `fertilizer_name`, `fertilizer_value`, `ratifer`, `ratiowater`) VALUES
(1, 'ปุ๋ยไข่', 0.1, 100, 1000),
(2, 'ปุ๋ยหมัก', 0.2, 100, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `sensor_value`
--

CREATE TABLE `sensor_value` (
  `sensorv_id` int(11) NOT NULL,
  `ph` float NOT NULL,
  `ec` float NOT NULL,
  `flow_pump` float NOT NULL,
  `light` float NOT NULL,
  `level` int(2) NOT NULL,
  `temp` float NOT NULL,
  `veget_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sensor_value`
--

INSERT INTO `sensor_value` (`sensorv_id`, `ph`, `ec`, `flow_pump`, `light`, `level`, `temp`, `veget_id`) VALUES
(11111111, 5, 6, 9.4, 350, 8, 26, 11111111),
(22222222, 7, 1.2, 22, 434, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `status_id` int(12) NOT NULL,
  `name` varchar(50) NOT NULL DEFAULT '',
  `status` int(1) NOT NULL DEFAULT 0,
  `veget_id` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`status_id`, `name`, `status`, `veget_id`) VALUES
(1111111, 'sever', 1, 11111111),
(11111111, 'process', 0, 11111111),
(0, 'sensor', 1, 11111111);

-- --------------------------------------------------------

--
-- Table structure for table `veget`
--

CREATE TABLE `veget` (
  `veget_id` int(11) NOT NULL,
  `veget_name` varchar(50) NOT NULL,
  `veget_old` int(3) NOT NULL,
  `date_start` date NOT NULL,
  `img` longtext NOT NULL,
  `status_id` int(13) NOT NULL,
  `sensorv_id` int(12) NOT NULL,
  `fertilizer_id` int(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `veget`
--

INSERT INTO `veget` (`veget_id`, `veget_name`, `veget_old`, `date_start`, `img`, `status_id`, `sensorv_id`, `fertilizer_id`) VALUES
(11111111, 'สลัด', 30, '2021-02-05', 'https://i1.bpic.cc/file/img-b1/2021/04/07/IMG_20210216_181446-1ce7750d70ddae56d.jpg\" alt=\"IMG_20210216_181446-1ce7750d70ddae56d.jpg', 11111111, 11111111, 1);

-- --------------------------------------------------------

--
-- Table structure for table `veget_value`
--

CREATE TABLE `veget_value` (
  `vegetv_id` int(15) NOT NULL,
  `ec` float NOT NULL,
  `date` date NOT NULL,
  `ph` float NOT NULL,
  `veget_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `veget_value`
--

INSERT INTO `veget_value` (`vegetv_id`, `ec`, `date`, `ph`, `veget_id`) VALUES
(22, 0, '2021-02-18', 7.8, 11111111),
(33, 0, '2021-02-19', 8, 11111111),
(44, 0, '2021-02-20', 7.9, 11111111),
(11111111, 0, '0000-00-00', 5, 0),
(11111112, 0, '2021-02-18', 1, 11111111),
(11111113, 0, '2021-02-19', 0.8, 11111111);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fertilizer`
--
ALTER TABLE `fertilizer`
  ADD PRIMARY KEY (`fertilizer_id`);

--
-- Indexes for table `veget`
--
ALTER TABLE `veget`
  ADD PRIMARY KEY (`veget_id`);

--
-- Indexes for table `veget_value`
--
ALTER TABLE `veget_value`
  ADD PRIMARY KEY (`vegetv_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fertilizer`
--
ALTER TABLE `fertilizer`
  MODIFY `fertilizer_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `veget_value`
--
ALTER TABLE `veget_value`
  MODIFY `vegetv_id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11111114;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
