import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
from app import app
import pandas as pd

pipeline = load('assets/pipeline.joblib')

all_options = {
'AL': ['Autauga', 'Baldwin', 'Barbour', 'Bibb', 'Blount', 'Bullock', 'Butler', 'Calhoun', 'Chambers', 'Cherokee', 'Chilton', 'Choctaw', 'Clarke', 'Clay', 'Cleburne', 'Coffee', 'Colbert', 'Conecuh', 'Coosa', 'Covington', 'Crenshaw', 'Cullman', 'Dale', 'Dallas', 'DeKalb', 'Elmore', 'Escambia', 'Etowah', 'Fayette', 'Franklin', 'Geneva', 'Greene', 'Hale', 'Henry', 'Houston', 'Jackson', 'Jefferson', 'Lamar', 'Lauderdale', 'Lawrence', 'Lee', 'Limestone', 'Lowndes', 'Macon', 'Madison', 'Marengo', 'Marion', 'Marshall', 'Mobile', 'Monroe', 'Montgomery', 'Morgan', 'Perry', 'Pickens', 'Pike', 'Randolph', 'Russell', 'St. Clair', 'Shelby', 'Sumter', 'Talladega', 'Tallapoosa', 'Tuscaloosa', 'Walker', 'Washington', 'Wilcox', 'Winston'],
'AK': ['Aleutians East', 'Aleutians West', 'Anchorage', 'Bethel', 'Bristol Bay', 'Denali', 'Dillingham', 'Fairbanks North Star', 'Haines', 'Hoonah-Angoon', 'Juneau', 'Kenai Peninsula', 'Ketchikan Gateway', 'Kodiak Island', 'Lake and Peninsula', 'Matanuska-Susitna', 'Nome', 'North Slope', 'Northwest Arctic', 'Petersburg', 'Prince of Wales-Hyder', 'Sitka', 'Skagway', 'Southeast Fairbanks', 'Valdez-Cordova', 'Wade Hampton', 'Wrangell', 'Yakutat', 'Yukon-Koyukuk'],
'AZ': ['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee', 'La Paz', 'Maricopa', 'Mohave', 'Navajo', 'Pima', 'Pinal', 'Santa Cruz', 'Yavapai', 'Yuma'],
'AR': ['Arkansas', 'Ashley', 'Baxter', 'Benton', 'Boone', 'Bradley', 'Calhoun', 'Carroll', 'Chicot', 'Clark', 'Clay', 'Cleburne', 'Cleveland', 'Columbia', 'Conway', 'Craighead', 'Crawford', 'Crittenden', 'Cross', 'Dallas', 'Desha', 'Drew', 'Faulkner', 'Franklin', 'Fulton', 'Garland', 'Grant', 'Greene', 'Hempstead', 'Hot Spring', 'Howard', 'Independence', 'Izard', 'Jackson', 'Jefferson', 'Johnson', 'Lafayette', 'Lawrence', 'Lee', 'Lincoln', 'Little River', 'Logan', 'Lonoke', 'Madison', 'Marion', 'Miller', 'Mississippi', 'Monroe', 'Montgomery', 'Nevada', 'Newton', 'Ouachita', 'Perry', 'Phillips', 'Pike', 'Poinsett', 'Polk', 'Pope', 'Prairie', 'Pulaski', 'Randolph', 'St. Francis', 'Saline', 'Scott', 'Searcy', 'Sebastian', 'Sevier', 'Sharp', 'Stone', 'Union', 'Van Buren', 'Washington', 'White', 'Woodruff', 'Yell'],
'CA': ['Alameda', 'Alpine', 'Amador', 'Butte', 'Calaveras', 'Colusa', 'Contra Costa', 'Del Norte', 'El Dorado', 'Fresno', 'Glenn', 'Humboldt', 'Imperial', 'Inyo', 'Kern', 'Kings', 'Lake', 'Lassen', 'Los Angeles', 'Madera', 'Marin', 'Mariposa', 'Mendocino', 'Merced', 'Modoc', 'Mono', 'Monterey', 'Napa', 'Nevada', 'Orange', 'Placer', 'Plumas', 'Riverside', 'Sacramento', 'San Benito', 'San Bernardino', 'San Diego', 'San Francisco', 'San Joaquin', 'San Luis Obispo', 'San Mateo', 'Santa Barbara', 'Santa Clara', 'Santa Cruz', 'Shasta', 'Sierra', 'Siskiyou', 'Solano', 'Sonoma', 'Stanislaus', 'Sutter', 'Tehama', 'Trinity', 'Tulare', 'Tuolumne', 'Ventura', 'Yolo', 'Yuba'],
'CO': ['Adams', 'Alamosa', 'Arapahoe', 'Archuleta', 'Baca', 'Bent', 'Boulder', 'Broomfield', 'Chaffee', 'Cheyenne', 'Clear Creek', 'Conejos', 'Costilla', 'Crowley', 'Custer', 'Delta', 'Denver', 'Dolores', 'Douglas', 'Eagle', 'Elbert', 'El Paso', 'Fremont', 'Garfield', 'Gilpin', 'Grand', 'Gunnison', 'Hinsdale', 'Huerfano', 'Jackson', 'Jefferson', 'Kiowa', 'Kit Carson', 'Lake', 'La Plata', 'Larimer', 'Las Animas', 'Lincoln', 'Logan', 'Mesa', 'Mineral', 'Moffat', 'Montezuma', 'Montrose', 'Morgan', 'Otero', 'Ouray', 'Park', 'Phillips', 'Pitkin', 'Prowers', 'Pueblo', 'Rio Blanco', 'Rio Grande', 'Routt', 'Saguache', 'San Juan', 'San Miguel', 'Sedgwick', 'Summit', 'Teller', 'Washington', 'Weld', 'Yuma'],
'CT': ['Fairfield', 'Hartford', 'Litchfield', 'Middlesex', 'New Haven', 'New London', 'Tolland', 'Windham'],
'DE': ['Kent', 'New Castle', 'Sussex'],
'DC': ['District of Columbia'],
'FL': ['Alachua', 'Baker', 'Bay', 'Bradford', 'Brevard', 'Broward', 'Calhoun', 'Charlotte', 'Citrus', 'Clay', 'Collier', 'Columbia', 'DeSoto', 'Dixie', 'Duval', 'Escambia', 'Flagler', 'Franklin', 'Gadsden', 'Gilchrist', 'Glades', 'Gulf', 'Hamilton', 'Hardee', 'Hendry', 'Hernando', 'Highlands', 'Hillsborough', 'Holmes', 'Indian River', 'Jackson', 'Jefferson', 'Lafayette', 'Lake', 'Lee', 'Leon', 'Levy', 'Liberty', 'Madison', 'Manatee', 'Marion', 'Martin', 'Miami-Dade', 'Monroe', 'Nassau', 'Okaloosa', 'Okeechobee', 'Orange', 'Osceola', 'Palm Beach', 'Pasco', 'Pinellas', 'Polk', 'Putnam', 'St. Johns', 'St. Lucie', 'Santa Rosa', 'Sarasota', 'Seminole', 'Sumter', 'Suwannee', 'Taylor', 'Union', 'Volusia', 'Wakulla', 'Walton', 'Washington'],
'GA': ['Appling', 'Atkinson', 'Bacon', 'Baker', 'Baldwin', 'Banks', 'Barrow', 'Bartow', 'Ben Hill', 'Berrien', 'Bibb', 'Bleckley', 'Brantley', 'Brooks', 'Bryan', 'Bulloch', 'Burke', 'Butts', 'Calhoun', 'Camden', 'Candler', 'Carroll', 'Catoosa', 'Charlton', 'Chatham', 'Chattahoochee', 'Chattooga', 'Cherokee', 'Clarke', 'Clay', 'Clayton', 'Clinch', 'Cobb', 'Coffee', 'Colquitt', 'Columbia', 'Cook', 'Coweta', 'Crawford', 'Crisp', 'Dade', 'Dawson', 'Decatur', 'DeKalb', 'Dodge', 'Dooly', 'Dougherty', 'Douglas', 'Early', 'Echols', 'Effingham', 'Elbert', 'Emanuel', 'Evans', 'Fannin', 'Fayette', 'Floyd', 'Forsyth', 'Franklin', 'Fulton', 'Gilmer', 'Glascock', 'Glynn', 'Gordon', 'Grady', 'Greene', 'Gwinnett', 'Habersham', 'Hall', 'Hancock', 'Haralson', 'Harris', 'Hart', 'Heard', 'Henry', 'Houston', 'Irwin', 'Jackson', 'Jasper', 'Jeff Davis', 'Jefferson', 'Jenkins', 'Johnson', 'Jones', 'Lamar', 'Lanier', 'Laurens', 'Lee', 'Liberty', 'Lincoln', 'Long', 'Lowndes', 'Lumpkin', 'McDuffie', 'McIntosh', 'Macon', 'Madison', 'Marion', 'Meriwether', 'Miller', 'Mitchell', 'Monroe', 'Montgomery', 'Morgan', 'Murray', 'Muscogee', 'Newton', 'Oconee', 'Oglethorpe', 'Paulding', 'Peach', 'Pickens', 'Pierce', 'Pike', 'Polk', 'Pulaski', 'Putnam', 'Quitman', 'Rabun', 'Randolph', 'Richmond', 'Rockdale', 'Schley', 'Screven', 'Seminole', 'Spalding', 'Stephens', 'Stewart', 'Sumter', 'Talbot', 'Taliaferro', 'Tattnall', 'Taylor', 'Telfair', 'Terrell', 'Thomas', 'Tift', 'Toombs', 'Towns', 'Treutlen', 'Troup', 'Turner', 'Twiggs', 'Union', 'Upson', 'Walker', 'Walton', 'Ware', 'Warren', 'Washington', 'Wayne', 'Webster', 'Wheeler', 'White', 'Whitfield', 'Wilcox', 'Wilkes', 'Wilkinson', 'Worth'],
'HI': ['Hawaii', 'Honolulu', 'Kalawao', 'Kauai', 'Maui'],
'ID': ['Ada', 'Adams', 'Bannock', 'Bear Lake', 'Benewah', 'Bingham', 'Blaine', 'Boise', 'Bonner', 'Bonneville', 'Boundary', 'Butte', 'Camas', 'Canyon', 'Caribou', 'Cassia', 'Clark', 'Clearwater', 'Custer', 'Elmore', 'Franklin', 'Fremont', 'Gem', 'Gooding', 'Idaho', 'Jefferson', 'Jerome', 'Kootenai', 'Latah', 'Lemhi', 'Lewis', 'Lincoln', 'Madison', 'Minidoka', 'Nez Perce', 'Oneida', 'Owyhee', 'Payette', 'Power', 'Shoshone', 'Teton', 'Twin Falls', 'Valley', 'Washington'],
'IL': ['Adams', 'Alexander', 'Bond', 'Boone', 'Brown', 'Bureau', 'Calhoun', 'Carroll', 'Cass', 'Champaign', 'Christian', 'Clark', 'Clay', 'Clinton', 'Coles', 'Cook', 'Crawford', 'Cumberland', 'DeKalb', 'De Witt', 'Douglas', 'DuPage', 'Edgar', 'Edwards', 'Effingham', 'Fayette', 'Ford', 'Franklin', 'Fulton', 'Gallatin', 'Greene', 'Grundy', 'Hamilton', 'Hancock', 'Hardin', 'Henderson', 'Henry', 'Iroquois', 'Jackson', 'Jasper', 'Jefferson', 'Jersey', 'Jo Daviess', 'Johnson', 'Kane', 'Kankakee', 'Kendall', 'Knox', 'Lake', 'LaSalle', 'Lawrence', 'Lee', 'Livingston', 'Logan', 'McDonough', 'McHenry', 'McLean', 'Macon', 'Macoupin', 'Madison', 'Marion', 'Marshall', 'Mason', 'Massac', 'Menard', 'Mercer', 'Monroe', 'Montgomery', 'Morgan', 'Moultrie', 'Ogle', 'Peoria', 'Perry', 'Piatt', 'Pike', 'Pope', 'Pulaski', 'Putnam', 'Randolph', 'Richland', 'Rock Island', 'St. Clair', 'Saline', 'Sangamon', 'Schuyler', 'Scott', 'Shelby', 'Stark', 'Stephenson', 'Tazewell', 'Union', 'Vermilion', 'Wabash', 'Warren', 'Washington', 'Wayne', 'White', 'Whiteside', 'Will', 'Williamson', 'Winnebago', 'Woodford'],
'IN': ['Adams', 'Allen', 'Bartholomew', 'Benton', 'Blackford', 'Boone', 'Brown', 'Carroll', 'Cass', 'Clark', 'Clay', 'Clinton', 'Crawford', 'Daviess', 'Dearborn', 'Decatur', 'DeKalb', 'Delaware', 'Dubois', 'Elkhart', 'Fayette', 'Floyd', 'Fountain', 'Franklin', 'Fulton', 'Gibson', 'Grant', 'Greene', 'Hamilton', 'Hancock', 'Harrison', 'Hendricks', 'Henry', 'Howard', 'Huntington', 'Jackson', 'Jasper', 'Jay', 'Jefferson', 'Jennings', 'Johnson', 'Knox', 'Kosciusko', 'LaGrange', 'Lake', 'LaPorte', 'Lawrence', 'Madison', 'Marion', 'Marshall', 'Martin', 'Miami', 'Monroe', 'Montgomery', 'Morgan', 'Newton', 'Noble', 'Ohio', 'Orange', 'Owen', 'Parke', 'Perry', 'Pike', 'Porter', 'Posey', 'Pulaski', 'Putnam', 'Randolph', 'Ripley', 'Rush', 'St. Joseph', 'Scott', 'Shelby', 'Spencer', 'Starke', 'Steuben', 'Sullivan', 'Switzerland', 'Tippecanoe', 'Tipton', 'Union', 'Vanderburgh', 'Vermillion', 'Vigo', 'Wabash', 'Warren', 'Warrick', 'Washington', 'Wayne', 'Wells', 'White', 'Whitley'],
'IA': ['Adair', 'Adams', 'Allamakee', 'Appanoose', 'Audubon', 'Benton', 'Black Hawk', 'Boone', 'Bremer', 'Buchanan', 'Buena Vista', 'Butler', 'Calhoun', 'Carroll', 'Cass', 'Cedar', 'Cerro Gordo', 'Cherokee', 'Chickasaw', 'Clarke', 'Clay', 'Clayton', 'Clinton', 'Crawford', 'Dallas', 'Davis', 'Decatur', 'Delaware', 'Des Moines', 'Dickinson', 'Dubuque', 'Emmet', 'Fayette', 'Floyd', 'Franklin', 'Fremont', 'Greene', 'Grundy', 'Guthrie', 'Hamilton', 'Hancock', 'Hardin', 'Harrison', 'Henry', 'Howard', 'Humboldt', 'Ida', 'Iowa', 'Jackson', 'Jasper', 'Jefferson', 'Johnson', 'Jones', 'Keokuk', 'Kossuth', 'Lee', 'Linn', 'Louisa', 'Lucas', 'Lyon', 'Madison', 'Mahaska', 'Marion', 'Marshall', 'Mills', 'Mitchell', 'Monona', 'Monroe', 'Montgomery', 'Muscatine', "O'Brien", 'Osceola', 'Page', 'Palo Alto', 'Plymouth', 'Pocahontas', 'Polk', 'Pottawattamie', 'Poweshiek', 'Ringgold', 'Sac', 'Scott', 'Shelby', 'Sioux', 'Story', 'Tama', 'Taylor', 'Union', 'Van Buren', 'Wapello', 'Warren', 'Washington', 'Wayne', 'Webster', 'Winnebago', 'Winneshiek', 'Woodbury', 'Worth', 'Wright'],
'KS': ['Allen', 'Anderson', 'Atchison', 'Barber', 'Barton', 'Bourbon', 'Brown', 'Butler', 'Chase', 'Chautauqua', 'Cherokee', 'Cheyenne', 'Clark', 'Clay', 'Cloud', 'Coffey', 'Comanche', 'Cowley', 'Crawford', 'Decatur', 'Dickinson', 'Doniphan', 'Douglas', 'Edwards', 'Elk', 'Ellis', 'Ellsworth', 'Finney', 'Ford', 'Franklin', 'Geary', 'Gove', 'Graham', 'Grant', 'Gray', 'Greeley', 'Greenwood', 'Hamilton', 'Harper', 'Harvey', 'Haskell', 'Hodgeman', 'Jackson', 'Jefferson', 'Jewell', 'Johnson', 'Kearny', 'Kingman', 'Kiowa', 'Labette', 'Lane', 'Leavenworth', 'Lincoln', 'Linn', 'Logan', 'Lyon', 'McPherson', 'Marion', 'Marshall', 'Meade', 'Miami', 'Mitchell', 'Montgomery', 'Morris', 'Morton', 'Nemaha', 'Neosho', 'Ness', 'Norton', 'Osage', 'Osborne', 'Ottawa', 'Pawnee', 'Phillips', 'Pottawatomie', 'Pratt', 'Rawlins', 'Reno', 'Republic', 'Rice', 'Riley', 'Rooks', 'Rush', 'Russell', 'Saline', 'Scott', 'Sedgwick', 'Seward', 'Shawnee', 'Sheridan', 'Sherman', 'Smith', 'Stafford', 'Stanton', 'Stevens', 'Sumner', 'Thomas', 'Trego', 'Wabaunsee', 'Wallace', 'Washington', 'Wichita', 'Wilson', 'Woodson', 'Wyandotte'],
'KY': ['Adair', 'Allen', 'Anderson', 'Ballard', 'Barren', 'Bath', 'Bell', 'Boone', 'Bourbon', 'Boyd', 'Boyle', 'Bracken', 'Breathitt', 'Breckinridge', 'Bullitt', 'Butler', 'Caldwell', 'Calloway', 'Campbell', 'Carlisle', 'Carroll', 'Carter', 'Casey', 'Christian', 'Clark', 'Clay', 'Clinton', 'Crittenden', 'Cumberland', 'Daviess', 'Edmonson', 'Elliott', 'Estill', 'Fayette', 'Fleming', 'Floyd', 'Franklin', 'Fulton', 'Gallatin', 'Garrard', 'Grant', 'Graves', 'Grayson', 'Green', 'Greenup', 'Hancock', 'Hardin', 'Harlan', 'Harrison', 'Hart', 'Henderson', 'Henry', 'Hickman', 'Hopkins', 'Jackson', 'Jefferson', 'Jessamine', 'Johnson', 'Kenton', 'Knott', 'Knox', 'Larue', 'Laurel', 'Lawrence', 'Lee', 'Leslie', 'Letcher', 'Lewis', 'Lincoln', 'Livingston', 'Logan', 'Lyon', 'McCracken', 'McCreary', 'McLean', 'Madison', 'Magoffin', 'Marion', 'Marshall', 'Martin', 'Mason', 'Meade', 'Menifee', 'Mercer', 'Metcalfe', 'Monroe', 'Montgomery', 'Morgan', 'Muhlenberg', 'Nelson', 'Nicholas', 'Ohio', 'Oldham', 'Owen', 'Owsley', 'Pendleton', 'Perry', 'Pike', 'Powell', 'Pulaski', 'Robertson', 'Rockcastle', 'Rowan', 'Russell', 'Scott', 'Shelby', 'Simpson', 'Spencer', 'Taylor', 'Todd', 'Trigg', 'Trimble', 'Union', 'Warren', 'Washington', 'Wayne', 'Webster', 'Whitley', 'Wolfe', 'Woodford'],
'LA': ['Acadia', 'Allen', 'Ascension', 'Assumption', 'Avoyelles', 'Beauregard', 'Bienville', 'Bossier', 'Caddo', 'Calcasieu', 'Caldwell', 'Cameron', 'Catahoula', 'Claiborne', 'Concordia', 'De Soto', 'East Baton Rouge', 'East Carroll', 'East Feliciana', 'Evangeline', 'Franklin', 'Grant', 'Iberia', 'Iberville', 'Jackson', 'Jefferson', 'Jefferson Davis', 'Lafayette', 'Lafourche', 'La Salle', 'Lincoln', 'Livingston', 'Madison', 'Morehouse', 'Natchitoches', 'Orleans', 'Ouachita', 'Plaquemines', 'Pointe Coupee', 'Rapides', 'Red River', 'Richland', 'Sabine', 'St. Bernard', 'St. Charles', 'St. Helena', 'St. James', 'St. John the Baptist', 'St. Landry', 'St. Martin', 'St. Mary', 'St. Tammany', 'Tangipahoa', 'Tensas', 'Terrebonne', 'Union', 'Vermilion', 'Vernon', 'Washington', 'Webster', 'West Baton Rouge', 'West Carroll', 'West Feliciana', 'Winn'],
'ME': ['Androscoggin', 'Aroostook', 'Cumberland', 'Franklin', 'Hancock', 'Kennebec', 'Knox', 'Lincoln', 'Oxford', 'Penobscot', 'Piscataquis', 'Sagadahoc', 'Somerset', 'Waldo', 'Washington', 'York'],
'MD': ['Allegany', 'Anne Arundel', 'Baltimore', 'Calvert', 'Caroline', 'Carroll', 'Cecil', 'Charles', 'Dorchester', 'Frederick', 'Garrett', 'Harford', 'Howard', 'Kent', 'Montgomery', "Prince George's", "Queen Anne's", "St. Mary's", 'Somerset', 'Talbot', 'Washington', 'Wicomico', 'Worcester', 'Baltimore'],
'MA': ['Barnstable', 'Berkshire', 'Bristol', 'Dukes', 'Essex', 'Franklin', 'Hampden', 'Hampshire', 'Middlesex', 'Nantucket', 'Norfolk', 'Plymouth', 'Suffolk', 'Worcester'],
'MI': ['Alcona', 'Alger', 'Allegan', 'Alpena', 'Antrim', 'Arenac', 'Baraga', 'Barry', 'Bay', 'Benzie', 'Berrien', 'Branch', 'Calhoun', 'Cass', 'Charlevoix', 'Cheboygan', 'Chippewa', 'Clare', 'Clinton', 'Crawford', 'Delta', 'Dickinson', 'Eaton', 'Emmet', 'Genesee', 'Gladwin', 'Gogebic', 'Grand Traverse', 'Gratiot', 'Hillsdale', 'Houghton', 'Huron', 'Ingham', 'Ionia', 'Iosco', 'Iron', 'Isabella', 'Jackson', 'Kalamazoo', 'Kalkaska', 'Kent', 'Keweenaw', 'Lake', 'Lapeer', 'Leelanau', 'Lenawee', 'Livingston', 'Luce', 'Mackinac', 'Macomb', 'Manistee', 'Marquette', 'Mason', 'Mecosta', 'Menominee', 'Midland', 'Missaukee', 'Monroe', 'Montcalm', 'Montmorency', 'Muskegon', 'Newaygo', 'Oakland', 'Oceana', 'Ogemaw', 'Ontonagon', 'Osceola', 'Oscoda', 'Otsego', 'Ottawa', 'Presque Isle', 'Roscommon', 'Saginaw', 'St. Clair', 'St. Joseph', 'Sanilac', 'Schoolcraft', 'Shiawassee', 'Tuscola', 'Van Buren', 'Washtenaw', 'Wayne', 'Wexford'],
'MN': ['Aitkin', 'Anoka', 'Becker', 'Beltrami', 'Benton', 'Big Stone', 'Blue Earth', 'Brown', 'Carlton', 'Carver', 'Cass', 'Chippewa', 'Chisago', 'Clay', 'Clearwater', 'Cook', 'Cottonwood', 'Crow Wing', 'Dakota', 'Dodge', 'Douglas', 'Faribault', 'Fillmore', 'Freeborn', 'Goodhue', 'Grant', 'Hennepin', 'Houston', 'Hubbard', 'Isanti', 'Itasca', 'Jackson', 'Kanabec', 'Kandiyohi', 'Kittson', 'Koochiching', 'Lac qui Parle', 'Lake', 'Lake of the Woods', 'Le Sueur', 'Lincoln', 'Lyon', 'McLeod', 'Mahnomen', 'Marshall', 'Martin', 'Meeker', 'Mille Lacs', 'Morrison', 'Mower', 'Murray', 'Nicollet', 'Nobles', 'Norman', 'Olmsted', 'Otter Tail', 'Pennington', 'Pine', 'Pipestone', 'Polk', 'Pope', 'Ramsey', 'Red Lake', 'Redwood', 'Renville', 'Rice', 'Rock', 'Roseau', 'St. Louis', 'Scott', 'Sherburne', 'Sibley', 'Stearns', 'Steele', 'Stevens', 'Swift', 'Todd', 'Traverse', 'Wabasha', 'Wadena', 'Waseca', 'Washington', 'Watonwan', 'Wilkin', 'Winona', 'Wright', 'Yellow Medicine'],
'MS': ['Adams', 'Alcorn', 'Amite', 'Attala', 'Benton', 'Bolivar', 'Calhoun', 'Carroll', 'Chickasaw', 'Choctaw', 'Claiborne', 'Clarke', 'Clay', 'Coahoma', 'Copiah', 'Covington', 'DeSoto', 'Forrest', 'Franklin', 'George', 'Greene', 'Grenada', 'Hancock', 'Harrison', 'Hinds', 'Holmes', 'Humphreys', 'Issaquena', 'Itawamba', 'Jackson', 'Jasper', 'Jefferson', 'Jefferson Davis', 'Jones', 'Kemper', 'Lafayette', 'Lamar', 'Lauderdale', 'Lawrence', 'Leake', 'Lee', 'Leflore', 'Lincoln', 'Lowndes', 'Madison', 'Marion', 'Marshall', 'Monroe', 'Montgomery', 'Neshoba', 'Newton', 'Noxubee', 'Oktibbeha', 'Panola', 'Pearl River', 'Perry', 'Pike', 'Pontotoc', 'Prentiss', 'Quitman', 'Rankin', 'Scott', 'Sharkey', 'Simpson', 'Smith', 'Stone', 'Sunflower', 'Tallahatchie', 'Tate', 'Tippah', 'Tishomingo', 'Tunica', 'Union', 'Walthall', 'Warren', 'Washington', 'Wayne', 'Webster', 'Wilkinson', 'Winston', 'Yalobusha', 'Yazoo'],
'MO': ['Adair', 'Andrew', 'Atchison', 'Audrain', 'Barry', 'Barton', 'Bates', 'Benton', 'Bollinger', 'Boone', 'Buchanan', 'Butler', 'Caldwell', 'Callaway', 'Camden', 'Cape Girardeau', 'Carroll', 'Carter', 'Cass', 'Cedar', 'Chariton', 'Christian', 'Clark', 'Clay', 'Clinton', 'Cole', 'Cooper', 'Crawford', 'Dade', 'Dallas', 'Daviess', 'DeKalb', 'Dent', 'Douglas', 'Dunklin', 'Franklin', 'Gasconade', 'Gentry', 'Greene', 'Grundy', 'Harrison', 'Henry', 'Hickory', 'Holt', 'Howard', 'Howell', 'Iron', 'Jackson', 'Jasper', 'Jefferson', 'Johnson', 'Knox', 'Laclede', 'Lafayette', 'Lawrence', 'Lewis', 'Lincoln', 'Linn', 'Livingston', 'McDonald', 'Macon', 'Madison', 'Maries', 'Marion', 'Mercer', 'Miller', 'Mississippi', 'Moniteau', 'Monroe', 'Montgomery', 'Morgan', 'New Madrid', 'Newton', 'Nodaway', 'Oregon', 'Osage', 'Ozark', 'Pemiscot', 'Perry', 'Pettis', 'Phelps', 'Pike', 'Platte', 'Polk', 'Pulaski', 'Putnam', 'Ralls', 'Randolph', 'Ray', 'Reynolds', 'Ripley', 'St. Charles', 'St. Clair', 'Ste. Genevieve', 'St. Francois', 'St. Louis', 'Saline', 'Schuyler', 'Scotland', 'Scott', 'Shannon', 'Shelby', 'Stoddard', 'Stone', 'Sullivan', 'Taney', 'Texas', 'Vernon', 'Warren', 'Washington', 'Wayne', 'Webster', 'Worth', 'Wright', 'St. Louis'],
'MT': ['Beaverhead', 'Big Horn', 'Blaine', 'Broadwater', 'Carbon', 'Carter', 'Cascade', 'Chouteau', 'Custer', 'Daniels', 'Dawson', 'Deer Lodge', 'Fallon', 'Fergus', 'Flathead', 'Gallatin', 'Garfield', 'Glacier', 'Golden Valley', 'Granite', 'Hill', 'Jefferson', 'Judith Basin', 'Lake', 'Lewis and Clark', 'Liberty', 'Lincoln', 'McCone', 'Madison', 'Meagher', 'Mineral', 'Missoula', 'Musselshell', 'Park', 'Petroleum', 'Phillips', 'Pondera', 'Powder River', 'Powell', 'Prairie', 'Ravalli', 'Richland', 'Roosevelt', 'Rosebud', 'Sanders', 'Sheridan', 'Silver Bow', 'Stillwater', 'Sweet Grass', 'Teton', 'Toole', 'Treasure', 'Valley', 'Wheatland', 'Wibaux', 'Yellowstone'],
'NE': ['Adams', 'Antelope', 'Arthur', 'Banner', 'Blaine', 'Boone', 'Box Butte', 'Boyd', 'Brown', 'Buffalo', 'Burt', 'Butler', 'Cass', 'Cedar', 'Chase', 'Cherry', 'Cheyenne', 'Clay', 'Colfax', 'Cuming', 'Custer', 'Dakota', 'Dawes', 'Dawson', 'Deuel', 'Dixon', 'Dodge', 'Douglas', 'Dundy', 'Fillmore', 'Franklin', 'Frontier', 'Furnas', 'Gage', 'Garden', 'Garfield', 'Gosper', 'Grant', 'Greeley', 'Hall', 'Hamilton', 'Harlan', 'Hayes', 'Hitchcock', 'Holt', 'Hooker', 'Howard', 'Jefferson', 'Johnson', 'Kearney', 'Keith', 'Keya Paha', 'Kimball', 'Knox', 'Lancaster', 'Lincoln', 'Logan', 'Loup', 'McPherson', 'Madison', 'Merrick', 'Morrill', 'Nance', 'Nemaha', 'Nuckolls', 'Otoe', 'Pawnee', 'Perkins', 'Phelps', 'Pierce', 'Platte', 'Polk', 'Red Willow', 'Richardson', 'Rock', 'Saline', 'Sarpy', 'Saunders', 'Scotts Bluff', 'Seward', 'Sheridan', 'Sherman', 'Sioux', 'Stanton', 'Thayer', 'Thomas', 'Thurston', 'Valley', 'Washington', 'Wayne', 'Webster', 'Wheeler', 'York'],
'NV': ['Churchill', 'Clark', 'Douglas', 'Elko', 'Esmeralda', 'Eureka', 'Humboldt', 'Lander', 'Lincoln', 'Lyon', 'Mineral', 'Nye', 'Pershing', 'Storey', 'Washoe', 'White Pine', 'Carson City'],
'NH': ['Belknap', 'Carroll', 'Cheshire', 'Coos', 'Grafton', 'Hillsborough', 'Merrimack', 'Rockingham', 'Strafford', 'Sullivan'],
'NJ': ['Atlantic', 'Bergen', 'Burlington', 'Camden', 'Cape May', 'Cumberland', 'Essex', 'Gloucester', 'Hudson', 'Hunterdon', 'Mercer', 'Middlesex', 'Monmouth', 'Morris', 'Ocean', 'Passaic', 'Salem', 'Somerset', 'Sussex', 'Union', 'Warren'],
'NM': ['Bernalillo', 'Catron', 'Chaves', 'Cibola', 'Colfax', 'Curry', 'De Baca', 'Doña Ana', 'Eddy', 'Grant', 'Guadalupe', 'Harding', 'Hidalgo', 'Lea', 'Lincoln', 'Los Alamos', 'Luna', 'McKinley', 'Mora', 'Otero', 'Quay', 'Rio Arriba', 'Roosevelt', 'Sandoval', 'San Juan', 'San Miguel', 'Santa Fe', 'Sierra', 'Socorro', 'Taos', 'Torrance', 'Union', 'Valencia'],
'NY': ['Albany', 'Allegany', 'Bronx', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua', 'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware', 'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene', 'Hamilton', 'Herkimer', 'Jefferson', 'Kings', 'Lewis', 'Livingston', 'Madison', 'Monroe', 'Montgomery', 'Nassau', 'New York', 'Niagara', 'Oneida', 'Onondaga', 'Ontario', 'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam', 'Queens', 'Rensselaer', 'Richmond', 'Rockland', 'St. Lawrence', 'Saratoga', 'Schenectady', 'Schoharie', 'Schuyler', 'Seneca', 'Steuben', 'Suffolk', 'Sullivan', 'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne', 'Westchester', 'Wyoming', 'Yates'],
'NC': ['Alamance', 'Alexander', 'Alleghany', 'Anson', 'Ashe', 'Avery', 'Beaufort', 'Bertie', 'Bladen', 'Brunswick', 'Buncombe', 'Burke', 'Cabarrus', 'Caldwell', 'Camden', 'Carteret', 'Caswell', 'Catawba', 'Chatham', 'Cherokee', 'Chowan', 'Clay', 'Cleveland', 'Columbus', 'Craven', 'Cumberland', 'Currituck', 'Dare', 'Davidson', 'Davie', 'Duplin', 'Durham', 'Edgecombe', 'Forsyth', 'Franklin', 'Gaston', 'Gates', 'Graham', 'Granville', 'Greene', 'Guilford', 'Halifax', 'Harnett', 'Haywood', 'Henderson', 'Hertford', 'Hoke', 'Hyde', 'Iredell', 'Jackson', 'Johnston', 'Jones', 'Lee', 'Lenoir', 'Lincoln', 'McDowell', 'Macon', 'Madison', 'Martin', 'Mecklenburg', 'Mitchell', 'Montgomery', 'Moore', 'Nash', 'New Hanover', 'Northampton', 'Onslow', 'Orange', 'Pamlico', 'Pasquotank', 'Pender', 'Perquimans', 'Person', 'Pitt', 'Polk', 'Randolph', 'Richmond', 'Robeson', 'Rockingham', 'Rowan', 'Rutherford', 'Sampson', 'Scotland', 'Stanly', 'Stokes', 'Surry', 'Swain', 'Transylvania', 'Tyrrell', 'Union', 'Vance', 'Wake', 'Warren', 'Washington', 'Watauga', 'Wayne', 'Wilkes', 'Wilson', 'Yadkin', 'Yancey'],
'ND': ['Adams', 'Barnes', 'Benson', 'Billings', 'Bottineau', 'Bowman', 'Burke', 'Burleigh', 'Cass', 'Cavalier', 'Dickey', 'Divide', 'Dunn', 'Eddy', 'Emmons', 'Foster', 'Golden Valley', 'Grand Forks', 'Grant', 'Griggs', 'Hettinger', 'Kidder', 'LaMoure', 'Logan', 'McHenry', 'McIntosh', 'McKenzie', 'McLean', 'Mercer', 'Morton', 'Mountrail', 'Nelson', 'Oliver', 'Pembina', 'Pierce', 'Ramsey', 'Ransom', 'Renville', 'Richland', 'Rolette', 'Sargent', 'Sheridan', 'Sioux', 'Slope', 'Stark', 'Steele', 'Stutsman', 'Towner', 'Traill', 'Walsh', 'Ward', 'Wells', 'Williams'],
'OH': ['Adams', 'Allen', 'Ashland', 'Ashtabula', 'Athens', 'Auglaize', 'Belmont', 'Brown', 'Butler', 'Carroll', 'Champaign', 'Clark', 'Clermont', 'Clinton', 'Columbiana', 'Coshocton', 'Crawford', 'Cuyahoga', 'Darke', 'Defiance', 'Delaware', 'Erie', 'Fairfield', 'Fayette', 'Franklin', 'Fulton', 'Gallia', 'Geauga', 'Greene', 'Guernsey', 'Hamilton', 'Hancock', 'Hardin', 'Harrison', 'Henry', 'Highland', 'Hocking', 'Holmes', 'Huron', 'Jackson', 'Jefferson', 'Knox', 'Lake', 'Lawrence', 'Licking', 'Logan', 'Lorain', 'Lucas', 'Madison', 'Mahoning', 'Marion', 'Medina', 'Meigs', 'Mercer', 'Miami', 'Monroe', 'Montgomery', 'Morgan', 'Morrow', 'Muskingum', 'Noble', 'Ottawa', 'Paulding', 'Perry', 'Pickaway', 'Pike', 'Portage', 'Preble', 'Putnam', 'Richland', 'Ross', 'Sandusky', 'Scioto', 'Seneca', 'Shelby', 'Stark', 'Summit', 'Trumbull', 'Tuscarawas', 'Union', 'Van Wert', 'Vinton', 'Warren', 'Washington', 'Wayne', 'Williams', 'Wood', 'Wyandot'],
'OK': ['Adair', 'Alfalfa', 'Atoka', 'Beaver', 'Beckham', 'Blaine', 'Bryan', 'Caddo', 'Canadian', 'Carter', 'Cherokee', 'Choctaw', 'Cimarron', 'Cleveland', 'Coal', 'Comanche', 'Cotton', 'Craig', 'Creek', 'Custer', 'Delaware', 'Dewey', 'Ellis', 'Garfield', 'Garvin', 'Grady', 'Grant', 'Greer', 'Harmon', 'Harper', 'Haskell', 'Hughes', 'Jackson', 'Jefferson', 'Johnston', 'Kay', 'Kingfisher', 'Kiowa', 'Latimer', 'Le Flore', 'Lincoln', 'Logan', 'Love', 'McClain', 'McCurtain', 'McIntosh', 'Major', 'Marshall', 'Mayes', 'Murray', 'Muskogee', 'Noble', 'Nowata', 'Okfuskee', 'Oklahoma', 'Okmulgee', 'Osage', 'Ottawa', 'Pawnee', 'Payne', 'Pittsburg', 'Pontotoc', 'Pottawatomie', 'Pushmataha', 'Roger Mills', 'Rogers', 'Seminole', 'Sequoyah', 'Stephens', 'Texas', 'Tillman', 'Tulsa', 'Wagoner', 'Washington', 'Washita', 'Woods', 'Woodward'],
'OR': ['Baker', 'Benton', 'Clackamas', 'Clatsop', 'Columbia', 'Coos', 'Crook', 'Curry', 'Deschutes', 'Douglas', 'Gilliam', 'Grant', 'Harney', 'Hood River', 'Jackson', 'Jefferson', 'Josephine', 'Klamath', 'Lake', 'Lane', 'Lincoln', 'Linn', 'Malheur', 'Marion', 'Morrow', 'Multnomah', 'Polk', 'Sherman', 'Tillamook', 'Umatilla', 'Union', 'Wallowa', 'Wasco', 'Washington', 'Wheeler', 'Yamhill'],
'PA': ['Adams', 'Allegheny', 'Armstrong', 'Beaver', 'Bedford', 'Berks', 'Blair', 'Bradford', 'Bucks', 'Butler', 'Cambria', 'Cameron', 'Carbon', 'Centre', 'Chester', 'Clarion', 'Clearfield', 'Clinton', 'Columbia', 'Crawford', 'Cumberland', 'Dauphin', 'Delaware', 'Elk', 'Erie', 'Fayette', 'Forest', 'Franklin', 'Fulton', 'Greene', 'Huntingdon', 'Indiana', 'Jefferson', 'Juniata', 'Lackawanna', 'Lancaster', 'Lawrence', 'Lebanon', 'Lehigh', 'Luzerne', 'Lycoming', 'McKean', 'Mercer', 'Mifflin', 'Monroe', 'Montgomery', 'Montour', 'Northampton', 'Northumberland', 'Perry', 'Philadelphia', 'Pike', 'Potter', 'Schuylkill', 'Snyder', 'Somerset', 'Sullivan', 'Susquehanna', 'Tioga', 'Union', 'Venango', 'Warren', 'Washington', 'Wayne', 'Westmoreland', 'Wyoming', 'York'],
'RI': ['Bristol', 'Kent', 'Newport', 'Providence', 'Washington'],
'SC': ['Abbeville', 'Aiken', 'Allendale', 'Anderson', 'Bamberg', 'Barnwell', 'Beaufort', 'Berkeley', 'Calhoun', 'Charleston', 'Cherokee', 'Chester', 'Chesterfield', 'Clarendon', 'Colleton', 'Darlington', 'Dillon', 'Dorchester', 'Edgefield', 'Fairfield', 'Florence', 'Georgetown', 'Greenville', 'Greenwood', 'Hampton', 'Horry', 'Jasper', 'Kershaw', 'Lancaster', 'Laurens', 'Lee', 'Lexington', 'McCormick', 'Marion', 'Marlboro', 'Newberry', 'Oconee', 'Orangeburg', 'Pickens', 'Richland', 'Saluda', 'Spartanburg', 'Sumter', 'Union', 'Williamsburg', 'York'],
'SD': ['Aurora', 'Beadle', 'Bennett', 'Bon Homme', 'Brookings', 'Brown', 'Brule', 'Buffalo', 'Butte', 'Campbell', 'Charles Mix', 'Clark', 'Clay', 'Codington', 'Corson', 'Custer', 'Davison', 'Day', 'Deuel', 'Dewey', 'Douglas', 'Edmunds', 'Fall River', 'Faulk', 'Grant', 'Gregory', 'Haakon', 'Hamlin', 'Hand', 'Hanson', 'Harding', 'Hughes', 'Hutchinson', 'Hyde', 'Jackson', 'Jerauld', 'Jones', 'Kingsbury', 'Lake', 'Lawrence', 'Lincoln', 'Lyman', 'McCook', 'McPherson', 'Marshall', 'Meade', 'Mellette', 'Miner', 'Minnehaha', 'Moody', 'Pennington', 'Perkins', 'Potter', 'Roberts', 'Sanborn', 'Shannon', 'Spink', 'Stanley', 'Sully', 'Todd', 'Tripp', 'Turner', 'Union', 'Walworth', 'Yankton', 'Ziebach'],
'TN': ['Anderson', 'Bedford', 'Benton', 'Bledsoe', 'Blount', 'Bradley', 'Campbell', 'Cannon', 'Carroll', 'Carter', 'Cheatham', 'Chester', 'Claiborne', 'Clay', 'Cocke', 'Coffee', 'Crockett', 'Cumberland', 'Davidson', 'Decatur', 'DeKalb', 'Dickson', 'Dyer', 'Fayette', 'Fentress', 'Franklin', 'Gibson', 'Giles', 'Grainger', 'Greene', 'Grundy', 'Hamblen', 'Hamilton', 'Hancock', 'Hardeman', 'Hardin', 'Hawkins', 'Haywood', 'Henderson', 'Henry', 'Hickman', 'Houston', 'Humphreys', 'Jackson', 'Jefferson', 'Johnson', 'Knox', 'Lake', 'Lauderdale', 'Lawrence', 'Lewis', 'Lincoln', 'Loudon', 'McMinn', 'McNairy', 'Macon', 'Madison', 'Marion', 'Marshall', 'Maury', 'Meigs', 'Monroe', 'Montgomery', 'Moore', 'Morgan', 'Obion', 'Overton', 'Perry', 'Pickett', 'Polk', 'Putnam', 'Rhea', 'Roane', 'Robertson', 'Rutherford', 'Scott', 'Sequatchie', 'Sevier', 'Shelby', 'Smith', 'Stewart', 'Sullivan', 'Sumner', 'Tipton', 'Trousdale', 'Unicoi', 'Union', 'Van Buren', 'Warren', 'Washington', 'Wayne', 'Weakley', 'White', 'Williamson', 'Wilson'],
'TX': ['Anderson', 'Andrews', 'Angelina', 'Aransas', 'Archer', 'Armstrong', 'Atascosa', 'Austin', 'Bailey', 'Bandera', 'Bastrop', 'Baylor', 'Bee', 'Bell', 'Bexar', 'Blanco', 'Borden', 'Bosque', 'Bowie', 'Brazoria', 'Brazos', 'Brewster', 'Briscoe', 'Brooks', 'Brown', 'Burleson', 'Burnet', 'Caldwell', 'Calhoun', 'Callahan', 'Cameron', 'Camp', 'Carson', 'Cass', 'Castro', 'Chambers', 'Cherokee', 'Childress', 'Clay', 'Cochran', 'Coke', 'Coleman', 'Collin', 'Collingsworth', 'Colorado', 'Comal', 'Comanche', 'Concho', 'Cooke', 'Coryell', 'Cottle', 'Crane', 'Crockett', 'Crosby', 'Culberson', 'Dallam', 'Dallas', 'Dawson', 'Deaf Smith', 'Delta', 'Denton', 'DeWitt', 'Dickens', 'Dimmit', 'Donley', 'Duval', 'Eastland', 'Ector', 'Edwards', 'Ellis', 'El Paso', 'Erath', 'Falls', 'Fannin', 'Fayette', 'Fisher', 'Floyd', 'Foard', 'Fort Bend', 'Franklin', 'Freestone', 'Frio', 'Gaines', 'Galveston', 'Garza', 'Gillespie', 'Glasscock', 'Goliad', 'Gonzales', 'Gray', 'Grayson', 'Gregg', 'Grimes', 'Guadalupe', 'Hale', 'Hall', 'Hamilton', 'Hansford', 'Hardeman', 'Hardin', 'Harris', 'Harrison', 'Hartley', 'Haskell', 'Hays', 'Hemphill', 'Henderson', 'Hidalgo', 'Hill', 'Hockley', 'Hood', 'Hopkins', 'Houston', 'Howard', 'Hudspeth', 'Hunt', 'Hutchinson', 'Irion', 'Jack', 'Jackson', 'Jasper', 'Jeff Davis', 'Jefferson', 'Jim Hogg', 'Jim Wells', 'Johnson', 'Jones', 'Karnes', 'Kaufman', 'Kendall', 'Kenedy', 'Kent', 'Kerr', 'Kimble', 'King', 'Kinney', 'Kleberg', 'Knox', 'Lamar', 'Lamb', 'Lampasas', 'La Salle', 'Lavaca', 'Lee', 'Leon', 'Liberty', 'Limestone', 'Lipscomb', 'Live Oak', 'Llano', 'Loving', 'Lubbock', 'Lynn', 'McCulloch', 'McLennan', 'McMullen', 'Madison', 'Marion', 'Martin', 'Mason', 'Matagorda', 'Maverick', 'Medina', 'Menard', 'Midland', 'Milam', 'Mills', 'Mitchell', 'Montague', 'Montgomery', 'Moore', 'Morris', 'Motley', 'Nacogdoches', 'Navarro', 'Newton', 'Nolan', 'Nueces', 'Ochiltree', 'Oldham', 'Orange', 'Palo Pinto', 'Panola', 'Parker', 'Parmer', 'Pecos', 'Polk', 'Potter', 'Presidio', 'Rains', 'Randall', 'Reagan', 'Real', 'Red River', 'Reeves', 'Refugio', 'Roberts', 'Robertson', 'Rockwall', 'Runnels', 'Rusk', 'Sabine', 'San Augustine', 'San Jacinto', 'San Patricio', 'San Saba', 'Schleicher', 'Scurry', 'Shackelford', 'Shelby', 'Sherman', 'Smith', 'Somervell', 'Starr', 'Stephens', 'Sterling', 'Stonewall', 'Sutton', 'Swisher', 'Tarrant', 'Taylor', 'Terrell', 'Terry', 'Throckmorton', 'Titus', 'Tom Green', 'Travis', 'Trinity', 'Tyler', 'Upshur', 'Upton', 'Uvalde', 'Val Verde', 'Van Zandt', 'Victoria', 'Walker', 'Waller', 'Ward', 'Washington', 'Webb', 'Wharton', 'Wheeler', 'Wichita', 'Wilbarger', 'Willacy', 'Williamson', 'Wilson', 'Winkler', 'Wise', 'Wood', 'Yoakum', 'Young', 'Zapata', 'Zavala'],
'UT': ['Beaver', 'Box Elder', 'Cache', 'Carbon', 'Daggett', 'Davis', 'Duchesne', 'Emery', 'Garfield', 'Grand', 'Iron', 'Juab', 'Kane', 'Millard', 'Morgan', 'Piute', 'Rich', 'Salt Lake', 'San Juan', 'Sanpete', 'Sevier', 'Summit', 'Tooele', 'Uintah', 'Utah', 'Wasatch', 'Washington', 'Wayne', 'Weber'],
'VT': ['Addison', 'Bennington', 'Caledonia', 'Chittenden', 'Essex', 'Franklin', 'Grand Isle', 'Lamoille', 'Orange', 'Orleans', 'Rutland', 'Washington', 'Windham', 'Windsor'],
'VA': ['Accomack', 'Albemarle', 'Alleghany', 'Amelia', 'Amherst', 'Appomattox', 'Arlington', 'Augusta', 'Bath', 'Bedford', 'Bland', 'Botetourt', 'Brunswick', 'Buchanan', 'Buckingham', 'Campbell', 'Caroline', 'Carroll', 'Charles City', 'Charlotte', 'Chesterfield', 'Clarke', 'Craig', 'Culpeper', 'Cumberland', 'Dickenson', 'Dinwiddie', 'Essex', 'Fairfax', 'Fauquier', 'Floyd', 'Fluvanna', 'Franklin', 'Frederick', 'Giles', 'Gloucester', 'Goochland', 'Grayson', 'Greene', 'Greensville', 'Halifax', 'Hanover', 'Henrico', 'Henry', 'Highland', 'Isle of Wight', 'James City', 'King and Queen', 'King George', 'King William', 'Lancaster', 'Lee', 'Loudoun', 'Louisa', 'Lunenburg', 'Madison', 'Mathews', 'Mecklenburg', 'Middlesex', 'Montgomery', 'Nelson', 'New Kent', 'Northampton', 'Northumberland', 'Nottoway', 'Orange', 'Page', 'Patrick', 'Pittsylvania', 'Powhatan', 'Prince Edward', 'Prince George', 'Prince William', 'Pulaski', 'Rappahannock', 'Richmond', 'Roanoke', 'Rockbridge', 'Rockingham', 'Russell', 'Scott', 'Shenandoah', 'Smyth', 'Southampton', 'Spotsylvania', 'Stafford', 'Surry', 'Sussex', 'Tazewell', 'Warren', 'Washington', 'Westmoreland', 'Wise', 'Wythe', 'York', 'Alexandria', 'Bristol', 'Buena Vista', 'Charlottesville', 'Chesapeake', 'Colonial Heights', 'Covington', 'Danville', 'Emporia', 'Fairfax', 'Falls Church', 'Franklin', 'Fredericksburg', 'Galax', 'Hampton', 'Harrisonburg', 'Hopewell', 'Lexington', 'Lynchburg', 'Manassas', 'Manassas Park', 'Martinsville', 'Newport News', 'Norfolk', 'Norton', 'Petersburg', 'Poquoson', 'Portsmouth', 'Radford', 'Richmond', 'Roanoke', 'Salem', 'Staunton', 'Suffolk', 'Virginia Beach', 'Waynesboro', 'Williamsburg', 'Winchester'],
'WA': ['Adams', 'Asotin', 'Benton', 'Chelan', 'Clallam', 'Clark', 'Columbia', 'Cowlitz', 'Douglas', 'Ferry', 'Franklin', 'Garfield', 'Grant', 'Grays Harbor', 'Island', 'Jefferson', 'King', 'Kitsap', 'Kittitas', 'Klickitat', 'Lewis', 'Lincoln', 'Mason', 'Okanogan', 'Pacific', 'Pend Oreille', 'Pierce', 'San Juan', 'Skagit', 'Skamania', 'Snohomish', 'Spokane', 'Stevens', 'Thurston', 'Wahkiakum', 'Walla Walla', 'Whatcom', 'Whitman', 'Yakima'],
'WV': ['Barbour', 'Berkeley', 'Boone', 'Braxton', 'Brooke', 'Cabell', 'Calhoun', 'Clay', 'Doddridge', 'Fayette', 'Gilmer', 'Grant', 'Greenbrier', 'Hampshire', 'Hancock', 'Hardy', 'Harrison', 'Jackson', 'Jefferson', 'Kanawha', 'Lewis', 'Lincoln', 'Logan', 'McDowell', 'Marion', 'Marshall', 'Mason', 'Mercer', 'Mineral', 'Mingo', 'Monongalia', 'Monroe', 'Morgan', 'Nicholas', 'Ohio', 'Pendleton', 'Pleasants', 'Pocahontas', 'Preston', 'Putnam', 'Raleigh', 'Randolph', 'Ritchie', 'Roane', 'Summers', 'Taylor', 'Tucker', 'Tyler', 'Upshur', 'Wayne', 'Webster', 'Wetzel', 'Wirt', 'Wood', 'Wyoming'],
'WI': ['Adams', 'Ashland', 'Barron', 'Bayfield', 'Brown', 'Buffalo', 'Burnett', 'Calumet', 'Chippewa', 'Clark', 'Columbia', 'Crawford', 'Dane', 'Dodge', 'Door', 'Douglas', 'Dunn', 'Eau Claire', 'Florence', 'Fond du Lac', 'Forest', 'Grant', 'Green', 'Green Lake', 'Iowa', 'Iron', 'Jackson', 'Jefferson', 'Juneau', 'Kenosha', 'Kewaunee', 'La Crosse', 'Lafayette', 'Langlade', 'Lincoln', 'Manitowoc', 'Marathon', 'Marinette', 'Marquette', 'Menominee', 'Milwaukee', 'Monroe', 'Oconto', 'Oneida', 'Outagamie', 'Ozaukee', 'Pepin', 'Pierce', 'Polk', 'Portage', 'Price', 'Racine', 'Richland', 'Rock', 'Rusk', 'St. Croix', 'Sauk', 'Sawyer', 'Shawano', 'Sheboygan', 'Taylor', 'Trempealeau', 'Vernon', 'Vilas', 'Walworth', 'Washburn', 'Washington', 'Waukesha', 'Waupaca', 'Waushara', 'Winnebago', 'Wood'],
'WY': ['Albany', 'Big Horn', 'Campbell', 'Carbon', 'Converse', 'Crook', 'Fremont', 'Goshen', 'Hot Springs', 'Johnson', 'Laramie', 'Lincoln', 'Natrona', 'Niobrara', 'Park', 'Platte', 'Sheridan', 'Sublette', 'Sweetwater', 'Teton', 'Uinta', 'Washakie', 'Weston'],
}

column1 = dbc.Col(
    [

        dcc.Markdown('''## Predictions''', className='mb-2' ),

        dcc.Markdown('Start by selecting the State and County from the dropdowns to the right (you can search by typing)'),

        dcc.Markdown('Once you have State and County selected, change the dials below to set parameters for the population and see the prediction update'),

        dcc.Markdown('#### Percent of Obese Adults'),

        daq.Knob(
            id='obese-knob',
            max=50,
            value=25,
            min=0,
            color={'gradient':True,
             'ranges':{'green': [0, 28], 
             'yellow': [28, 33], 
             'red': [33, 50]}}
        ),  

        dcc.Markdown('#### Percent of Population 65 and Older'),

        daq.Knob(
            id='65older-knob',
            max=50,
            value=25,
            min=0,
            color={'gradient':True,
             'ranges':{'green': [0, 13], 
             'yellow': [13, 18], 
             'red': [18, 50]}}
        )
    
    ],
    md=4,
)

column2 = dbc.Col(
    [
        
        dcc.Markdown('#### State'),
        dcc.Dropdown(
            id='states_dropdown',
            options=[{'label': k, 'value': k} for k in all_options.keys()],
            value='AL',
            className='mb-2'
        ),

        dcc.Markdown('#### County'),

        dcc.Dropdown(id='county-dropdown', className='mb-5'),

        dcc.Markdown('#### Percent of Children and Adults Recieveing Care Food Programs'),    

        daq.Knob(
            id='foodassist-knob',
            max=3,
            value=1.5,
            min=0,
            color={'gradient':True,
             'ranges':{'green': [0, 1], 
             'yellow': [1, 2], 
             'red': [2, 3]}}
        ),

        dcc.Markdown('#### Percent of Households with Very-Low Food Security'),

        daq.Knob(
            id='foodsec-knob',
            max=10,
            value=5,
            min=0,
            color={'gradient':True,
             'ranges':{'green': [0, 5], 
             'yellow': [5, 7], 
             'red': [7, 10]}}
        )

    ],
    md=4
)

column3 = dbc.Col(
    [

        html.H2('Predicted Percent of Adults with Diabetes'),
        html.Div(id='prediction', className='lead'),

        dcc.Markdown('This value is the predicted percentage of adults in the specifed County with any form of diabetes.'),
        dcc.Markdown('For more information about how the model works, please click below.'),

        dcc.Link(dbc.Button('Learn more!', color='primary'), href='/insights')

    ]
)



layout = dbc.Row([column1, column2, column3])

@app.callback(
    Output('county-dropdown', 'options'),
    [Input('states_dropdown', 'value')])
def set_county_options(selected_state):
    return [{'label': i, 'value': i} for i in all_options[selected_state]]


@app.callback(
    Output('county-dropdown', 'value'),
    [Input('county-dropdown', 'options')])
def set_county_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output('prediction', 'children'),
    [Input('states_dropdown', 'value'), Input('county-dropdown', 'value'),
    Input('obese-knob', 'value'), Input('65older-knob', 'value'),
    Input('foodassist-knob', 'value'), Input('foodsec-knob', 'value')]
)
def predict(state, county, obese, older, assist, secure):
    df = pd.DataFrame(
        columns=['State', 'County', 
        'PCT_OBESE_ADULTS13', 'PCT_65OLDER10', 
        'VLFOODSEC_10_12', 'PCT_CACFP09'],
        data=[[state, county, obese, older, assist, secure]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.1f}%'