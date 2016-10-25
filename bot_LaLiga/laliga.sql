-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-10-2016 a las 10:25:09
-- Versión del servidor: 5.5.50-0ubuntu0.14.04.1
-- Versión de PHP: 5.5.9-1ubuntu4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `laliga`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clasificacion`
--

CREATE TABLE IF NOT EXISTS `clasificacion` (
  `posicion` int(11) NOT NULL,
  `Equipo` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `Puntos` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`posicion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `clasificacion`
--

INSERT INTO `clasificacion` (`posicion`, `Equipo`, `Puntos`) VALUES
(1, 'Atlético', '18'),
(2, 'Real Madrid', '18'),
(3, 'Sevilla', '17'),
(4, 'Barcelona', '16'),
(5, 'Villarreal', '16'),
(6, 'Athletic', '15'),
(7, 'Las Palmas', '12'),
(8, 'Eibar', '11'),
(9, 'Betis', '11'),
(10, 'Alavés', '10'),
(11, 'R. Sociedad', '10'),
(12, 'Leganés', '10'),
(13, 'Celta', '10'),
(14, 'Málaga', '9'),
(15, 'Valencia', '9'),
(16, 'Deportivo', '8'),
(17, 'Espanyol', '7'),
(18, 'Sporting', '7'),
(19, 'Osasuna', '6'),
(20, 'Granada', '2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultados`
--

CREATE TABLE IF NOT EXISTS `resultados` (
  `partido` int(11) NOT NULL AUTO_INCREMENT,
  `local` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `marcador` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `visitante` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`partido`),
  UNIQUE KEY `partido` (`partido`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=11 ;

--
-- Volcado de datos para la tabla `resultados`
--

INSERT INTO `resultados` (`partido`, `local`, `marcador`, `visitante`) VALUES
(1, 'Osasuna', '                    1 - 2                    ', 'Betis'),
(2, 'Espanyol', '                    -                    ', 'Eibar'),
(3, 'Valencia', '                    -                    ', 'Barcelona'),
(4, 'R. Sociedad', '                    -                    ', 'Alavés'),
(5, 'Granada', '                    -                    ', 'Sporting'),
(6, 'Celta', '-', 'Deportivo'),
(7, 'Sevilla', '-', 'Atlético'),
(8, 'Málaga', '-', 'Leganés'),
(9, 'Villarreal', '-', 'Las Palmas'),
(10, 'Real Madrid', '-', 'Athletic');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
