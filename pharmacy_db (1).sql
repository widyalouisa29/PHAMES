-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2024 at 08:54 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pharmacy_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `obat`
--

CREATE TABLE `obat` (
  `id_obat` int(11) NOT NULL,
  `nama_obat` varchar(90) NOT NULL,
  `tanggal_expiry_obat` date NOT NULL,
  `jumlah_stok_obat` int(11) NOT NULL,
  `minimum_stock` int(11) NOT NULL,
  `jenis_obat` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `obat`
--

INSERT INTO `obat` (`id_obat`, `nama_obat`, `tanggal_expiry_obat`, `jumlah_stok_obat`, `minimum_stock`, `jenis_obat`) VALUES
(1, 'Agrylin', '2025-12-20', 30, 10, 'Obat Keras'),
(3, 'Thrombo aspilets', '2024-04-01', 15, 10, 'Obat Bebas Terbatas'),
(4, 'Bodrex migrain', '2024-01-20', 100, 10, 'Obat Bebas Terbatas'),
(5, 'Arthrifen', '2025-04-25', 80, 10, 'Obat Bebas Terbatas'),
(6, 'Valtrex', '2024-05-29', 90, 10, 'Obat Bebas Terbatas'),
(7, 'Bodrex ekstra', '2025-03-15', 100, 10, 'Obat Bebas Terbatas'),
(8, 'Reso-hin', '2025-02-02', 10, 10, 'Obat Bebas Terbatas'),
(9, 'Histaklor', '2025-03-23', 25, 10, 'Obat Bebas Terbatas'),
(10, 'Mexaquin', '2025-04-18', 40, 10, 'Obat Bebas Terbatas'),
(11, 'CTM', '2025-02-28', 90, 10, 'Obat Bebas Terbatas'),
(12, 'Alleron', '2028-02-15', 300, 10, 'Obat Bebas Terbatas'),
(13, 'Coredryl', '2024-09-10', 40, 10, 'Obat Bebas Terbatas'),
(14, 'Allergen', '2027-02-20', 35, 10, 'Obat Bebas Terbatas'),
(15, 'Alermax', '2025-02-25', 50, 10, 'Obat Bebas Terbatas'),
(16, 'Zacoldin', '2025-05-22', 600, 10, 'Obat Bebas Terbatas'),
(17, 'Tifalsic', '2026-01-15', 90, 10, 'Obat Bebas Terbatas'),
(18, 'Tiafen', '2025-03-05', 300, 10, 'Obat Bebas Terbatas'),
(19, 'Reanal', '2024-09-20', 200, 10, 'Obat Bebas Terbatas'),
(20, 'procold', '2027-02-12', 220, 10, 'Obat Bebas Terbatas'),
(21, 'profen', '2026-03-30', 85, 10, 'Obat Bebas Terbatas'),
(22, 'selmetor', '2025-03-28', 59, 10, 'Obat Bebas Terbatas'),
(23, 'ascardia ', '2028-04-10', 70, 10, 'Obat Bebas Keras'),
(24, 'simvastain 10mg', '2027-04-20', 150, 10, 'Obat Keras'),
(25, 'salbutamol 2mg', '2025-03-15', 260, 10, 'Obat Keras'),
(26, 'levofloxacin', '2024-03-13', 54, 10, 'Obat Keras'),
(27, 'albotyl concentrate', '2026-05-29', 78, 10, 'Obat Keras'),
(28, 'furosemide 40mg', '2028-02-15', 50, 10, 'Obat Keras'),
(29, 'omeprazol 20mg', '2024-02-15', 20, 10, 'Obat Keras'),
(30, 'Bisoprolol', '2024-08-13', 40, 10, 'Obat Keras'),
(31, 'Betahistin', '2025-06-09', 30, 10, 'Obat Keras'),
(32, 'ceffotaxime', '2026-08-15', 45, 10, 'Obat Keras'),
(33, 'Dobrizol', '2025-10-01', 49, 10, 'Obat Keras'),
(34, 'Dexametasone 5mg', '2024-05-15', 56, 10, 'Obat Keras'),
(35, 'Hexavask 5mg', '2024-09-15', 90, 10, 'Obat Keras'),
(36, 'Histapan', '2024-12-30', 60, 10, 'Obat Keras'),
(37, 'Irbesatan 150mg', '2024-06-15', 190, 10, 'Obat Keras'),
(38, 'Kalmeco', '2025-05-30', 30, 10, 'Obat Keras'),
(39, 'Lerzin', '2024-05-21', 550, 10, 'Obat Keras'),
(40, 'Kasa Hidrofil', '2024-05-17', 300, 10, 'Obat Keras'),
(41, 'Voltadex', '2025-11-15', 40, 10, 'Obat Keras'),
(42, 'Muzoral', '2025-12-25', 10, 10, 'Obat Keras'),
(43, 'Digest 30mg', '2023-12-20', 80, 10, 'Obat Keras'),
(44, 'Cetrin 10mg', '2024-07-07', 120, 10, 'Obat Keras'),
(45, 'Erlamycetin TT', '2025-11-06', 450, 10, 'Obat Keras'),
(46, 'Alprazolam 0,5mg', '2024-05-01', 240, 10, 'Obat Narkotika'),
(47, 'Analsik', '2024-06-29', 100, 10, 'Obat Narkotika'),
(48, 'Anesfar 1mg', '2024-05-02', 90, 10, 'Obat Narkotika'),
(49, 'Asabium 10mg', '2024-05-25', 30, 10, 'Obat Narkotika'),
(50, 'Braxidin', '2025-08-17', 40, 10, 'Obat Narkotika'),
(51, 'Cliad', '2025-07-08', 35, 10, 'Obat Narkotika'),
(52, 'Clobazam', '2025-07-10', 150, 10, 'Obat Narkotika'),
(53, 'Danalgin', '2025-06-15', 170, 10, 'Obat Narkotika'),
(54, 'Esilgan', '2025-10-30', 590, 10, 'Obat Narkotika'),
(55, 'frisium', '2025-11-29', 400, 10, 'Obat Narkotika'),
(56, 'Librax', '2025-08-25', 60, 10, 'Obat Narkotika'),
(57, 'Merlopam 2mg', '2025-05-22', 300, 10, 'Obat Narkotika'),
(58, 'Miloz 1mg', '2024-05-22', 500, 10, 'Obat Narkotika'),
(59, 'Opineuron', '2025-04-22', 300, 10, 'Obat Narkotika'),
(60, 'Prohiper', '2025-01-15', 140, 10, 'Obat Narkotika'),
(61, 'Riklona', '2025-01-17', 20, 10, 'Obat Narkotika'),
(62, 'Sanmag', '2025-03-29', 95, 10, 'Obat Narkotika'),
(63, 'Sedacum', '2025-02-15', 20, 10, 'Obat Narkotika'),
(64, 'Sibital', '2025-02-15', 500, 10, 'Obat Narkotika'),
(65, 'Stesolid', '2025-03-20', 300, 10, 'Obat Narkotika'),
(66, 'codipront', '2025-04-20', 200, 10, 'Obat Narkotika'),
(67, 'Duragesic', '2024-07-20', 350, 10, 'Obat Narkotika'),
(68, 'Fentanyl', '2024-05-13', 150, 10, 'Obat Narkotika'),
(69, 'Morfina', '2024-06-10', 100, 10, 'Obat Narkotika'),
(70, 'Mst Continus', '2024-06-01', 50, 10, 'Obat Narkotika'),
(71, 'Pethidin', '2025-04-30', 146, 10, 'Obat Narkotika'),
(72, 'Xanax', '2024-07-20', , 10, 'Obat Narkotika'),
(73, 'Valisanbe', '2025-05-20', 123, 10, 'Obat Narkotika'),
(74, 'Zypraz', '2024-04-20', 500, 10, 'Obat Narkotika');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'admin', '000'),
(2, 'halo', '123'),
(3, 'abcd', '111'),
(4, 'hehe', '456'),
(5, 'irka', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `obat`
--
ALTER TABLE `obat`
  ADD PRIMARY KEY (`id_obat`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `obat`
--
ALTER TABLE `obat`
  MODIFY `id_obat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
