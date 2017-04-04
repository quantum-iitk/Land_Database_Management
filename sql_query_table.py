query = """--
-- Table structure for table `ch form 1-a`
--

CREATE TABLE `ch form 1-a` (
  `Serial No` int(11) DEFAULT NULL,
  `Villages` varchar(255) DEFAULT NULL,
  `Name of the villages` varchar(255) DEFAULT NULL,
  `Name od District` varchar(255) DEFAULT NULL,
  `Name of Tehsil` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 2-a`
--

CREATE TABLE `ch form 2-a` (
  `Plot No` varchar(255) DEFAULT NULL,
  `Area as recorded in column of the basic Khasara` varchar(255) DEFAULT NULL,
  `Area as recorded in the current settlement` varchar(255) DEFAULT NULL,
  `Area as found on spot` varchar(255) DEFAULT NULL,
  `No of Khata Khatauni of the basic year` varchar(255) DEFAULT NULL,
  `Name of tenure holder` varchar(255) DEFAULT NULL,
  `Name ofAsami` varchar(255) DEFAULT NULL,
  `Name of Asami` varchar(255) DEFAULT NULL,
  `Details od dispute of possesssion` varchar(255) DEFAULT NULL,
  `Discription` varchar(255) DEFAULT NULL,
  `Measurements and age` varchar(255) DEFAULT NULL,
  `Estimeted value` varchar(255) DEFAULT NULL,
  `Name of the owner,his address and share in the property` varchar(255) DEFAULT NULL,
  `Nature` varchar(255) DEFAULT NULL,
  `Area` varchar(255) DEFAULT NULL,
  `Details of uncultivated area (Nature)` varchar(255) DEFAULT NULL,
  `Details of uncultivated area (Included in holding)` varchar(255) DEFAULT NULL,
  `Details of uncultivated area (not included in holding)` varchar(255) DEFAULT NULL,
  `Details of irrigation (Source and method)` varchar(255) DEFAULT NULL,
  `Details of irrigation (Irrigable area)` varchar(255) DEFAULT NULL,
  `Kharif` varchar(255) DEFAULT NULL,
  `Rabi` varchar(255) DEFAULT NULL,
  `Zaid` varchar(255) DEFAULT NULL,
  `Physical features of the plot` varchar(255) DEFAULT NULL,
  `Area (Solid class as recorded in current settlement)` varchar(255) DEFAULT NULL,
  `Area (Non consolidable)` varchar(255) DEFAULT NULL,
  `Area (Consolidable)` varchar(255) DEFAULT NULL,
  `Exchange ratio in annas (in words)` varchar(255) DEFAULT NULL,
  `Valutaion of the consolidable area of the plot (col27 x col28)` varchar(255) DEFAULT NULL,
  `Modified exchange ratio` varchar(255) DEFAULT NULL,
  `Valuation as modified by superior authorities (col27 X col30)` varchar(255) DEFAULT NULL,
  `Khata no (As proposed by ACO )` varchar(255) DEFAULT NULL,
  `Khata no (As modified by CO)` varchar(255) DEFAULT NULL,
  `Khata no (As modified in appeals and revisions)` varchar(255) DEFAULT NULL,
  `Remarks` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 4`
--

CREATE TABLE `ch form 4` (
  `ID` int(11) DEFAULT NULL,
  `No of Khata Khatauni of the basic year` int(11) DEFAULT NULL,
  `Plot Nos where mistakes and disputes donot relate to the whole K` int(11) DEFAULT NULL,
  `Areas of plots recorded in column 2` int(11) DEFAULT NULL,
  `Serial No (Deatails of mistakes and disputes)` int(11) DEFAULT NULL,
  `Details` mediumtext,
  `Details of shares claimed in the holding by each tenure-holder` varchar(255) DEFAULT NULL,
  `Orders od Assistant Consolidation Office` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 5 (extract)`
--

CREATE TABLE `ch form 5 (extract)` (
  `No of Khata in the current Annual Register` varchar(255) DEFAULT NULL,
  `Name of tenure-holder` varchar(255) DEFAULT NULL,
  `Claass of tenure` varchar(255) DEFAULT NULL,
  `Year of commencement of tenre` varchar(255) DEFAULT NULL,
  `Plot no` varchar(255) DEFAULT NULL,
  `Total` varchar(255) DEFAULT NULL,
  `Area (Consolidable)` varchar(255) DEFAULT NULL,
  `Area (Non-Consolidable)` varchar(255) DEFAULT NULL,
  `Exchange ratio in annas (in words) of consolidable areas (Col 8)` varchar(255) DEFAULT NULL,
  `Valuation in annasof the consolidable area` varchar(255) DEFAULT NULL,
  `Description (Details of improvement)` varchar(255) DEFAULT NULL,
  `Measurement (Details of improvement)` varchar(255) DEFAULT NULL,
  `Estimated value (Details of improvement)` varchar(255) DEFAULT NULL,
  `Name of the owner,address and share in the property` varchar(255) DEFAULT NULL,
  `Land revenue payable by the tenure holder` varchar(255) DEFAULT NULL,
  `Name with percentage and residance (Details of Asami)` varchar(255) DEFAULT NULL,
  `Year of commencement of tenure (Details of Asami)` varchar(255) DEFAULT NULL,
  `Rent payable` varchar(255) DEFAULT NULL,
  `Details of mistakes and disputes discovered and share recorded` varchar(255) DEFAULT NULL,
  `Remarks` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 5-b`
--

CREATE TABLE `ch form 5-b` (
  `ID` int(11) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `No of Khata of current Annual Register` int(11) DEFAULT NULL,
  `Name of the person recorded in annual register` varchar(255) DEFAULT NULL,
  `Name of the person alleged to be in possession` varchar(255) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL,
  `Non-consolidable` int(11) DEFAULT NULL,
  `Consolidable` int(11) DEFAULT NULL,
  `Exchange ratio in annas (in words)in consolidable area` int(11) DEFAULT NULL,
  `Annual valuation` int(11) DEFAULT NULL,
  `Class` int(11) DEFAULT NULL,
  `Measurements and age` int(11) DEFAULT NULL,
  `Estimated value` double DEFAULT NULL,
  `Name and the owner, his address and share in property` varchar(255) DEFAULT NULL,
  `Details of mistakes of area,if any` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 6`
--

CREATE TABLE `ch form 6` (
  `ID` int(11) DEFAULT NULL,
  `Case no` int(11) DEFAULT NULL,
  `Village and pragana` varchar(255) DEFAULT NULL,
  `Name of parties` varchar(255) DEFAULT NULL,
  `Description of the case` varchar(255) DEFAULT NULL,
  `Date of instituition` datetime DEFAULT NULL,
  `Date of order` datetime DEFAULT NULL,
  `Gist of orders passes regarding (Partition and amalgamation)` varchar(255) DEFAULT NULL,
  `Gist of orders passes regarding (Other matters)` varchar(255) DEFAULT NULL,
  `Dates of Amaldaramad of orders mentioned in (Column 7)` datetime DEFAULT NULL,
  `Dates of Amaldaramad of orders mentioned in (Column 8)` datetime DEFAULT NULL,
  `No and date of chalan` varchar(255) DEFAULT NULL,
  `Official's signature and date of dilivery` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 6-b`
--

CREATE TABLE `ch form 6-b` (
  `Serial no` int(11) DEFAULT NULL,
  `Page no of the record` int(11) DEFAULT NULL,
  `Column of the record` int(11) DEFAULT NULL,
  `Line` int(11) DEFAULT NULL,
  `Incorrect or doubtful Entries` int(11) DEFAULT NULL,
  `Correct Entries` int(11) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 6-c`
--

CREATE TABLE `ch form 6-c` (
  `Village` varchar(255) DEFAULT NULL,
  `Pargana` varchar(255) DEFAULT NULL,
  `No of Khata Khatauni` int(11) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Details of rights claimed` varchar(255) DEFAULT NULL,
  `Name and percentage with residance` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 7`
--

CREATE TABLE `ch form 7` (
  `Serial no` int(11) DEFAULT NULL,
  `No of Khata Khatauni of the basic year (13 Fasli)` int(11) DEFAULT NULL,
  `Plot nos` int(11) DEFAULT NULL,
  `Area of each plot` int(11) DEFAULT NULL,
  `Soil class` varchar(255) DEFAULT NULL,
  `Heriditary rent rates` double DEFAULT NULL,
  `Valuation of each plot of heriditary rent rates (Col 4 X 6 )` double DEFAULT NULL,
  `Total rental value of all the plots` double DEFAULT NULL,
  `Land revenue of the Khata` double DEFAULT NULL,
  `Plot No espunged from the holding or excluded from consolidation` int(11) DEFAULT NULL,
  `Area of each plot shown in Col 10` int(11) DEFAULT NULL,
  `Rental value of each plot shown in Col 10 at rate shown in Col 6` double DEFAULT NULL,
  `Total rental value of plots shown in col 10` double DEFAULT NULL,
  `Amount of proportionate land revenue (Col 9 X Col 13 / Col 8 )` double DEFAULT NULL,
  `Fasli year from which the proportioante land (Col 14) is payable` datetime DEFAULT NULL,
  `Amount of land revenue (Col 9 - 14)` double DEFAULT NULL,
  `Fasli year with effect from which revenue (col16) is payable` datetime DEFAULT NULL,
  `Wether Sections 245,246,247 of ZALR act applies for assessment` varchar(255) DEFAULT NULL,
  `Amount of land revenue` double DEFAULT NULL,
  `Fasli year with effect from which land revenue col19 is payable` datetime DEFAULT NULL,
  `Signature of the Settlement Officer` varchar(255) DEFAULT NULL,
  `No of Khata of the revised Khatauni` int(11) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 7-b`
--

CREATE TABLE `ch form 7-b` (
  `Plot no` int(11) DEFAULT NULL,
  `Soil class as recorded in the last settlement` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 10`
--

CREATE TABLE `ch form 10` (
  `Class of tenure` varchar(255) DEFAULT NULL,
  `No of Khatauni Khata` int(11) DEFAULT NULL,
  `Name of tenure-holders` varchar(255) DEFAULT NULL,
  `Plot no` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Land Revenue` double DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 10-a`
--

CREATE TABLE `ch form 10-a` (
  `Serial No` int(11) DEFAULT NULL,
  `Name of tenure-holder with percentage and residance` varchar(255) DEFAULT NULL,
  `No of Khata Khatauni` int(11) DEFAULT NULL,
  `Class of tenure` varchar(255) DEFAULT NULL,
  `Land revenue` double DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 11`
--

CREATE TABLE `ch form 11` (
  `Serial No` int(11) DEFAULT NULL,
  `Name of tenure-holder with percentage and residance` varchar(255) DEFAULT NULL,
  `Year of commencement of tenure` int(11) DEFAULT NULL,
  `No of each plot of the holding` int(11) DEFAULT NULL,
  `Area of each plot in bighas or acres` int(11) DEFAULT NULL,
  `Land revenue or rent payable by the tenure-holder` double DEFAULT NULL,
  `Serial Number in basic Khatauni` int(11) DEFAULT NULL,
  `Name of the tenure hollder` varchar(255) DEFAULT NULL,
  `Land revenue payable by the tenure-holder shown in column 8` double DEFAULT NULL,
  `Number of tenure-holder` int(11) DEFAULT NULL,
  `Number of each plot/area` int(11) DEFAULT NULL,
  `Land revenue payable by the tenure-holder shown in column 10` double DEFAULT NULL,
  `Date of order and case number >>` varchar(255) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Land revenue payable` double DEFAULT NULL,
  `Serial nnumber (Col 1)cof Khatas amalgamated` int(11) DEFAULT NULL,
  `Name of tenure-holders anddetails of shares in amalgamated Khata` varchar(255) DEFAULT NULL,
  `Date of order and case number` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 18`
--

CREATE TABLE `ch form 18` (
  `Seral No` int(11) DEFAULT NULL,
  `Number od plot` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Number of Khata Khatauni` int(11) DEFAULT NULL,
  `Remarks showing cause of exclusion` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 21 part iii`
--

CREATE TABLE `ch form 21 part iii` (
  `Si No` int(11) DEFAULT NULL,
  `Purpose for each emarked` varchar(255) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `Area revised from (Holding area)` int(11) DEFAULT NULL,
  `Area revised from (Non-holding area)` int(11) DEFAULT NULL,
  `Vluation  in terms of annas for area shown in Col 4` int(11) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 23 (part i)`
--

CREATE TABLE `ch form 23 (part i)` (
  `Serial No` int(11) DEFAULT NULL,
  `Name and percentage of tenure-holder with residance` varchar(255) DEFAULT NULL,
  `Class of tenure` varchar(255) DEFAULT NULL,
  `Year of commencement of tenure` int(11) DEFAULT NULL,
  `Khata number of the revised Annulal Register in CH Form 11` int(11) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL,
  `Area (Excluded from consolidation)` int(11) DEFAULT NULL,
  `Area (Included in consolidation)` int(11) DEFAULT NULL,
  `Exchange ratio of the plot or its part to be consolidated` int(11) DEFAULT NULL,
  `Anna valuatioin of the plot or its part to be consolidated` double DEFAULT NULL,
  `Land Revenue of the holding` double DEFAULT NULL,
  `Contribution inn terms of Anna valuation for public purposes` double DEFAULT NULL,
  `Contribution for public purposes in terms of area (Col 13X9/11)` double DEFAULT NULL,
  `Land revenue to be reduced` double DEFAULT NULL,
  `Amount of compensation` double DEFAULT NULL,
  `Net valuation to be alloted (Col 11X13)(on totals of holding)` double DEFAULT NULL,
  `Class of tenure (Proposed Holding)` varchar(255) DEFAULT NULL,
  `Plot no (Proposed Holding)` int(11) DEFAULT NULL,
  `Area (Proposed Holding)` int(11) DEFAULT NULL,
  `Exchange ratio (Proposed Holding)` int(11) DEFAULT NULL,
  `Annual valuation (Proposed Holding)` double DEFAULT NULL,
  `Land revenue payable by tenure-holder after reduction` double DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 23 (part ii)`
--

CREATE TABLE `ch form 23 (part ii)` (
  `Si No of CH FORM 3 (Part I)` int(11) DEFAULT NULL,
  `Number and kind of trees,wells and other improvements` varchar(255) DEFAULT NULL,
  `Plot No on which tree etc exist` int(11) DEFAULT NULL,
  `Compensation Pyable` double DEFAULT NULL,
  `Name and percentage of Asami with residence` varchar(255) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Valuation` double DEFAULT NULL,
  `Rent payable` double DEFAULT NULL,
  `Reduction in area` int(11) DEFAULT NULL,
  `Reduction in rent of the asami` double DEFAULT NULL,
  `Compensation payable to asami` double DEFAULT NULL,
  `Plot No(Proposed holding of Asami)` int(11) DEFAULT NULL,
  `Area (Proposed holding of Asami)` int(11) DEFAULT NULL,
  `Valuation (Proposed holding of Asami)` double DEFAULT NULL,
  `Rent payable (Col9-Col11)` double DEFAULT NULL,
  `Name of encumbrancer and nature of encumbrances` varchar(255) DEFAULT NULL,
  `Amount` double DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 23 (part iii)`
--

CREATE TABLE `ch form 23 (part iii)` (
  `Si No` int(11) DEFAULT NULL,
  `Purposes (From holding area)` varchar(255) DEFAULT NULL,
  `Plot No (From holding area)` int(11) DEFAULT NULL,
  `Area (From holding area)` int(11) DEFAULT NULL,
  `Purposes (From non-holding area)` varchar(255) DEFAULT NULL,
  `Plot No (From non-holding area)` int(11) DEFAULT NULL,
  `Area (From non-holding area)` int(11) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Particulars` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 23-a (part i)`
--

CREATE TABLE `ch form 23-a (part i)` (
  `Serial No` int(11) DEFAULT NULL,
  `Name and percentage of tenure-holder with residance` varchar(255) DEFAULT NULL,
  `Class of tenure` varchar(255) DEFAULT NULL,
  `No of Khata Khatauni` int(11) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Land revenue` double DEFAULT NULL,
  `Name of encumbrancer and nature  of encumbrance` varchar(255) DEFAULT NULL,
  `Amount` double DEFAULT NULL,
  `Name and percentage with residance` varchar(255) DEFAULT NULL,
  `Plot No (Asami)` int(11) DEFAULT NULL,
  `Area (Asami)` int(11) DEFAULT NULL,
  `Rent payable (Asami)` double DEFAULT NULL,
  `Class of tenure (Proposed Holding)` varchar(255) DEFAULT NULL,
  `Plot No (Proposed Holding)` int(11) DEFAULT NULL,
  `Area alloted (Proposed Holding)` int(11) DEFAULT NULL,
  `Land Revenue (Proposed Holding)` double DEFAULT NULL,
  `Name of encumbrancer and nature of encumbrances` varchar(255) DEFAULT NULL,
  `Amount (Proposed Holding)` double DEFAULT NULL,
  `Name and percentage with residance >>` varchar(255) DEFAULT NULL,
  `Plot No(Assami ,if any,under tenure holder)` varchar(255) DEFAULT NULL,
  `Area (Assami ,if any,under tenure holder)` int(11) DEFAULT NULL,
  `Rent payable (Assami ,if any,under tenure holder)` double DEFAULT NULL,
  `No and kinds of trees,wellor other improvements` varchar(255) DEFAULT NULL,
  `Plot No on which trees etc exist` int(11) DEFAULT NULL,
  `Compensation` double DEFAULT NULL,
  `To whom payable` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 23-a (part ii)`
--

CREATE TABLE `ch form 23-a (part ii)` (
  `Serial No` int(11) DEFAULT NULL,
  `Purposes (From Holding Area)` varchar(255) DEFAULT NULL,
  `Plot No (From Holding Area)` int(11) DEFAULT NULL,
  `Area (From Holding Area)` int(11) DEFAULT NULL,
  `Purposes (From non-holding Area)` varchar(255) DEFAULT NULL,
  `Plot No  (From non-holding Area)` int(11) DEFAULT NULL,
  `Area  (From non-holding Area)` int(11) DEFAULT NULL,
  `Plot No (Details ohther than land belonging to Gaon Sabha)` int(11) DEFAULT NULL,
  `Area  (Details ohther than land belonging to Gaon Sabha)` int(11) DEFAULT NULL,
  `Particulars  (Details ohther than land belonging to Gaon Sabha)` varchar(255) DEFAULT NULL,
  `Remarks  (Details ohther than land belonging to Gaon Sabha)` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 23-b (part i)`
--

CREATE TABLE `ch form 23-b (part i)` (
  `Serial No of chak roads and chak guls` int(11) DEFAULT NULL,
  `Plot No (From Holding Area)` int(11) DEFAULT NULL,
  `Area (From Holding Area)` int(11) DEFAULT NULL,
  `Exchange ratio` int(11) DEFAULT NULL,
  `Anna valuation` double DEFAULT NULL,
  `Plot No (From Non-holding Area)` int(11) DEFAULT NULL,
  `Area (From Non-holding Area)` int(11) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 23-b (part ii)`
--

CREATE TABLE `ch form 23-b (part ii)` (
  `Serial No` int(11) DEFAULT NULL,
  `Name and percentage of tenure-holder with residance` varchar(255) DEFAULT NULL,
  `Khata No of current Khatauni` int(11) DEFAULT NULL,
  `Tenure` int(11) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Exchange Ratio` int(11) DEFAULT NULL,
  `Anna valuation` double DEFAULT NULL,
  `Tenure (alloted)` int(11) DEFAULT NULL,
  `Plot No (alloted)` int(11) DEFAULT NULL,
  `Area (alloted)` int(11) DEFAULT NULL,
  `Exchange raio (alloted)` int(11) DEFAULT NULL,
  `Anna Valuation (alloted)` double DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 23-b (part iii)`
--

CREATE TABLE `ch form 23-b (part iii)` (
  `Serial No` int(11) DEFAULT NULL,
  `Name and percentage of tenure-holders with residance` varchar(255) DEFAULT NULL,
  `Khata No current Khatauni` int(11) DEFAULT NULL,
  `Total area of the holdings as per Khatauni` int(11) DEFAULT NULL,
  `Land revenue of the holding as per Khatauni` double DEFAULT NULL,
  `Contribution for chak roads and chak guls in terms of area` int(11) DEFAULT NULL,
  `Land revenue to be reduced for contributing for chak roads/guls` double DEFAULT NULL,
  `Land revenue payable` double DEFAULT NULL,
  `Compensation Payable` double DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 23-c`
--

CREATE TABLE `ch form 23-c` (
  `Serial No` int(11) DEFAULT NULL,
  `Name and percentage of tenure-holder with residance` varchar(255) DEFAULT NULL,
  `Class of tenure` varchar(255) DEFAULT NULL,
  `Year of commencement of tenure` int(11) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Land revenue` double DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 26`
--

CREATE TABLE `ch form 26` (
  `ID` int(11) DEFAULT NULL,
  `Plot No on which the trees etc exist` int(11) DEFAULT NULL,
  `No and kind of trees,wells or other improvements` int(11) DEFAULT NULL,
  `Amount of compensation payable` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 26-a`
--

CREATE TABLE `ch form 26-a` (
  `Serial No of the list` int(11) DEFAULT NULL,
  `Serial No of entry in CH form 23` int(11) DEFAULT NULL,
  `Name of the tenure-holder` varchar(255) DEFAULT NULL,
  `Amount of compensation` double DEFAULT NULL,
  `Amount adjusted towards cost of consolidation` double DEFAULT NULL,
  `Amount payable in cash` double DEFAULT NULL,
  `Date of payement` datetime DEFAULT NULL,
  `Amount paid` double DEFAULT NULL,
  `Signature of recipient` varchar(255) DEFAULT NULL,
  `Signature of Assistant Consolidation Officer who paid the amount` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 27`
--

CREATE TABLE `ch form 27` (
  `ID` int(11) DEFAULT NULL,
  `serial number` int(11) DEFAULT NULL,
  `Name,parentage and address of tenure-holders` varchar(255) DEFAULT NULL,
  `Area of holding as shown in column 7 of C` int(11) DEFAULT NULL,
  `Rate of Cost of consolidation applicable` int(11) DEFAULT NULL,
  `Total demand of cost of consolidation` int(11) DEFAULT NULL,
  `Amount of compensation payable to the tenure-holder` int(11) DEFAULT NULL,
  `Net amount of cost of consolidation` int(11) DEFAULT NULL,
  `Amount of Instalment` int(11) DEFAULT NULL,
  `Amount Realised` int(11) DEFAULT NULL,
  `Date of deposit in Treasury  with Challan number` datetime DEFAULT NULL,
  `Signature of Naib-Tahsildar` varchar(255) DEFAULT NULL,
  `Balance` int(11) DEFAULT NULL,
  `Amount of Instalment-2` int(11) DEFAULT NULL,
  `Total amount to be realised including arrears,` int(11) DEFAULT NULL,
  `Amount realised-2` int(11) DEFAULT NULL,
  `Date of deposit in Treasurey with Challan number` datetime DEFAULT NULL,
  `Signature of Naib-Tahsildar-2` varchar(255) DEFAULT NULL,
  `Remarks-2` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 27-b`
--

CREATE TABLE `ch form 27-b` (
  `ID` int(11) DEFAULT NULL,
  `serial number` int(11) DEFAULT NULL,
  `Name of tenure holder` varchar(255) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Side` int(11) DEFAULT NULL,
  `Length or volume of boundary erected` int(11) DEFAULT NULL,
  `Total length of boundary line erected` int(11) DEFAULT NULL,
  `Demand to be realised` varchar(255) DEFAULT NULL,
  `Number of receipt and date` varchar(255) DEFAULT NULL,
  `Serial Number of daily register` varchar(255) DEFAULT NULL,
  `Amount` varchar(255) DEFAULT NULL,
  `Date of deposit in Treasury with Number of Challan` varchar(255) DEFAULT NULL,
  `Signature of Naib-Tahsildar` varchar(255) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 29`
--

CREATE TABLE `ch form 29` (
  `ID` int(11) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `Name of members of consolidation Committee present` varchar(255) DEFAULT NULL,
  `Descriptionof proceedings` varchar(255) DEFAULT NULL,
  `Signature of members` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 30`
--

CREATE TABLE `ch form 30` (
  `ID` int(11) DEFAULT NULL,
  `Date;` datetime DEFAULT NULL,
  `Place of halt at night` varchar(255) DEFAULT NULL,
  `Description of works done` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ch form 30`
--

INSERT INTO `ch form 30` (`ID`, `Date;`, `Place of halt at night`, `Description of works done`) VALUES
(1, '2013-06-03 00:00:00', 'kanpur', 'nothing special');

-- --------------------------------------------------------

--
-- Table structure for table `ch form 31`
--

CREATE TABLE `ch form 31` (
  `ID` int(11) DEFAULT NULL,
  `Serial Number of service` int(11) DEFAULT NULL,
  `Description of document to be served` varchar(255) DEFAULT NULL,
  `On whom to be served` varchar(255) DEFAULT NULL,
  `Date of service` datetime DEFAULT NULL,
  `Signature of thumb impression` varchar(255) DEFAULT NULL,
  `Signature of serving officer with date` varchar(255) DEFAULT NULL,
  `Name of designation of serving officer` varchar(255) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 32`
--

CREATE TABLE `ch form 32` (
  `ID` int(11) DEFAULT NULL,
  `Serial Number` int(11) DEFAULT NULL,
  `Name of tenure-holders with parentage` int(11) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Name of crop with its area` varchar(255) DEFAULT NULL,
  `Final hereditary rate applicable` int(11) DEFAULT NULL,
  `Rental value of cropeed area` int(11) DEFAULT NULL,
  `Multiple of compensation fixed` int(11) DEFAULT NULL,
  `Amount of compensation for the plot` int(11) DEFAULT NULL,
  `Name of tenure-holder to whom the plot is alloted` varchar(255) DEFAULT NULL,
  `Plot Number-2` int(11) DEFAULT NULL,
  `Name of crop with area` varchar(255) DEFAULT NULL,
  `Final hereditary rate applicable-2` int(11) DEFAULT NULL,
  `Rental value of cropped area` varchar(255) DEFAULT NULL,
  `Multiple of compensation fixed-2` int(11) DEFAULT NULL,
  `Amount of compensation for the plot-2` int(11) DEFAULT NULL,
  `Name,of tenure holder,who reatins to tend crop in the  plot-2` varchar(255) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 33`
--

CREATE TABLE `ch form 33` (
  `ID` int(11) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Name or relevant crop` varchar(255) DEFAULT NULL,
  `Cropped area` int(11) DEFAULT NULL,
  `Estimated yeild in maunds per acre or Bigha` int(11) DEFAULT NULL,
  `Total yeild of the plot in maund` int(11) DEFAULT NULL,
  `Market value of produce per maund` int(11) DEFAULT NULL,
  `Estimated price of crop in plots` int(11) DEFAULT NULL,
  `Cost of cultivation per are or bigha till harvesting` int(11) DEFAULT NULL,
  `Total cost of cultivation of plot` int(11) DEFAULT NULL,
  `Present value of the produce of the plot` int(11) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 34`
--

CREATE TABLE `ch form 34` (
  `ID` int(11) DEFAULT NULL,
  `Serial Number` int(11) DEFAULT NULL,
  `Name of tenure holder with parentage` varchar(255) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Value of crops of the plot` int(11) DEFAULT NULL,
  `Amount of compensation for the plot` varchar(255) DEFAULT NULL,
  `Name of the tenure-holder to whom crop in plot is delivered` int(11) DEFAULT NULL,
  `Khasra Number` int(11) DEFAULT NULL,
  `Value of crops of the plot-2` int(11) DEFAULT NULL,
  `Amount of compensation for the plot-2` int(11) DEFAULT NULL,
  `Name of the tenure-holder who originally tended the crop` varchar(255) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 35`
--

CREATE TABLE `ch form 35` (
  `ID` int(11) DEFAULT NULL,
  `Serial Number` varchar(255) DEFAULT NULL,
  `Name of paying compensation tenure-holder colum 16 of CH Form 32` int(11) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Amount of Compensation Payable` int(11) DEFAULT NULL,
  `Serial Number-2` int(11) DEFAULT NULL,
  `Name of paying compensation tenure-holder Column 18 of CH Form32` int(11) DEFAULT NULL,
  `Plot Number-2` int(11) DEFAULT NULL,
  `Amount of compensation payable-2` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 36`
--

CREATE TABLE `ch form 36` (
  `ID` int(11) DEFAULT NULL,
  `Serial Number` int(11) DEFAULT NULL,
  `Name of tenure-holder` varchar(255) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Standing Crop` varchar(255) DEFAULT NULL,
  `Amount of compensation` int(11) DEFAULT NULL,
  `Serial or certificate issued to recipient` int(11) DEFAULT NULL,
  `Serial Number-2` int(11) DEFAULT NULL,
  `Name of tenure-holder-2` varchar(255) DEFAULT NULL,
  `Plot Number-2` int(11) DEFAULT NULL,
  `Standing Crop-2` varchar(255) DEFAULT NULL,
  `Amount of compensation-2` int(11) DEFAULT NULL,
  `Serial or certificate issued to recipient-2` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ch form 36`
--

INSERT INTO `ch form 36` (`ID`, `Serial Number`, `Name of tenure-holder`, `Plot Number`, `Standing Crop`, `Amount of compensation`, `Serial or certificate issued to recipient`, `Serial Number-2`, `Name of tenure-holder-2`, `Plot Number-2`, `Standing Crop-2`, `Amount of compensation-2`, `Serial or certificate issued to recipient-2`) VALUES
(2, 1, 'garvit', 34, 'cdre', 2345, 34, 3, 'dfsddss', 36, 'dfrr', 45775, 345);

-- --------------------------------------------------------

--
-- Table structure for table `ch form 41`
--

CREATE TABLE `ch form 41` (
  `ID` int(11) DEFAULT NULL,
  `New Number` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Old Number` int(11) DEFAULT NULL,
  `Area-2` int(11) DEFAULT NULL,
  `New Khata-Khatauni Number` int(11) DEFAULT NULL,
  `Soil Class of last settlement` varchar(255) DEFAULT NULL,
  `Source of irrigation` varchar(255) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 44`
--

CREATE TABLE `ch form 44` (
  `ID` int(11) DEFAULT NULL,
  `Serial Number` int(11) DEFAULT NULL,
  `Name of tenure-holder with parentage and residence` varchar(255) DEFAULT NULL,
  `Class of Tenure` varchar(255) DEFAULT NULL,
  `Name of villages where holdings situated` varchar(255) DEFAULT NULL,
  `Khata number of the basic Khatauni of each village` int(11) DEFAULT NULL,
  `Land revenue payable in each villages in the class` int(11) DEFAULT NULL,
  `Total Land revenue payable in the class in all the villages` int(11) DEFAULT NULL,
  `Class of tenure-2` varchar(255) DEFAULT NULL,
  `Name of the villages where holdings alotted` varchar(255) DEFAULT NULL,
  `Anna Value of the land allotted in the class in each village` int(11) DEFAULT NULL,
  `Total anna value allotted in all the village in the class` int(11) DEFAULT NULL,
  `Future land revenue payable in the class` int(11) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 45`
--

CREATE TABLE `ch form 45` (
  `ID` int(11) DEFAULT NULL,
  `Serial Number of Khatauni Khata` int(11) DEFAULT NULL,
  `Name of tenure-holder with parentage and residence` varchar(255) DEFAULT NULL,
  `Year of commencement of tenure` int(11) DEFAULT NULL,
  `New plot Numbers` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Land Revenue of rent payable by the tenure-holder` int(11) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ch form 291`
--

CREATE TABLE `ch form 291` (
  `ID` int(11) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `Name of memebers of consolodation committee present` varchar(255) DEFAULT NULL,
  `Description of proceedings` varchar(255) DEFAULT NULL,
  `Signature of memebers` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `khatauni`
--

CREATE TABLE `khatauni` (
  `Number of Khata Khatauni of the basic year` varchar(255) DEFAULT NULL,
  `Name of tenure-holder` varchar(255) DEFAULT NULL,
  `Parent's name of tenure holder` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Village` varchar(255) DEFAULT NULL,
  `Paragana` varchar(255) DEFAULT NULL,
  `Tehsil` varchar(255) DEFAULT NULL,
  `District` varchar(255) DEFAULT NULL,
  `year of commencement of tenure` varchar(255) DEFAULT NULL,
  `Plot no` varchar(255) DEFAULT NULL,
  `Area of plot in hectare` varchar(255) DEFAULT NULL,
  `Land revenue of rent payable by the tenure holder` varchar(255) DEFAULT NULL,
  `Crop Year 1` varchar(255) DEFAULT NULL,
  `Crop Year 2` varchar(255) DEFAULT NULL,
  `Crop Year 3` varchar(255) DEFAULT NULL,
  `Crop Year 4` varchar(255) DEFAULT NULL,
  `Crop Year 5` varchar(255) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
"""