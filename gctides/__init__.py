from future import standard_library
import ulmo.usgs.nwis as nwis
import pandas as pd
import matplotlib.pyplot as plt


def gcgauges():
    gauges = pd.DataFrame.from_records(
        [(0.0,      '09380000', 'Colorado River at Lees Ferry'),
         (87.4,     '09402500', 'Colorado River near Grand Canyon'),
         (225.0,    '09404200', 'Colorado River above Diamond Creek')],
        columns=["RM", "ID", "Name"])
    return gauges


def gcmiles(what='all'):
    miles = None
    frames = []

    if type(what) is not list:
        what = [what]

    if what not in ['all', 'camps', 'rapids', 'hikes', 'misc']:
        raise ValueError("Unexpected request type: " + what)

    # Construct feature dataframe(s). Each dataframe MUST contain the fields
    #   RM      river mile (float)
    #   Name    feature name (string)
    #   Type    feature type (string)
    # Dataframe(s) describing on-shore features should include a "Side" column
    # indicating whether the feature is river right or left
    if what in ["all", "camps"]:
        camps = [
            # RM    Name                    Type    Side        Size
            (0.0,   "Lee's Ferry",          "Camp", "Right",    "Large"),
            (5.0,   "5 Mile",               "Camp", "Right",    "Small"),
            (5.9,   "6 Mile",               "Camp", "Right",    "Small"),
            (8.1,   "Jackass Canyon",       "Camp", "Left",     "Large"),
            (8.1,   "Badger Creek",         "Camp", "Right",    "Medium"),
            (8.8,   "Below Jackass",        "Camp", "Left",     "Small"),
            (9.0,   "Sandbar",              "Camp", "Left",     "Small"),
            (11.3,  "Soap Creek",           "Camp", "Right",    "Medium"),
            (12.1,  "Brown's Inscription",  "Camp", "Left",     "Small"),
            (12.4,  "12.4 Mile",            "Camp", "Left",     "Small"),
            (13.1,  "13 Mile Ledges",       "Camp", "Right",    "Medium"),
            (14.4,  "Sheer Wall",           "Camp", "Left",     "Small"),
            (16.4,  "Hot Na Na",            "Camp", "Left",     "Medium"),
            (17.3,  "House Rock",           "Camp", "Right",    "Large"),
            (18.4,  "18 Mi. Wash",          "Camp", "Left",     "Medium"),
            (18.5,  "18 Mi. Ledges",        "Camp", "Left",     "Small"),
            (19.2,  "19.2 Mi.",             "Camp", "Right",    "Small"),
            (19.4,  "19.4 Mile",            "Camp", "Left",     "Large"),
            (20.2,  "Twenty Mile",          "Camp", "Left",     "Large"),
            (20.7,  "Upper North Canyon",   "Camp", "Right",    "Large"),
            (20.8,  "Lower North Canyon",   "Camp", "Right",    "Large"),
            (22.1,  "22 Mile",              "Camp", "Right",    "Small"),
            (22.7,  "Indian Dick",          "Camp", "Left",     "Large"),
            (23.5,  "Lone Cedar",           "Camp", "Left",     "Medium"),
            (24.5,  "24.5 Mile",            "Camp", "Left",     "Medium"),
            (26.4,  "Above tiger Wash",     "Camp", "Left",     "Small"),
            (29.5,  "Shinumo Wash",         "Camp", "Left",     "Large"),
            (29.8,  "Island",               "Camp", "Right",    "Small"),
            (30.6,  "Fence Fault",          "Camp", "Right",    "Large"),
            (30.8,  "Sand Pile",            "Camp", "Right",    "Large"),
            (31.6,  "Upper South Canyon",   "Camp", "Right",    "Small"),
            (31.7,  "South Canyon",         "Camp", "Right",    "Large"),
            (33.8,  "Below Redwall",        "Camp", "Left",     "Small"),
            (34.0,  "Little Redwall",       "Camp", "Left",     "Medium"),
            (35.1,  "Nautiloid",            "Camp", "Left",     "Large"),
            (37.9,  "Tatahatso",            "Camp", "Left",     "Large"),
            (38.3,  "Above Martha's",       "Camp", "Left",     "Small"),
            (38.7,  "Martha's",             "Camp", "Left",     "Medium"),
            (39.3,  "Redbud Alcove",        "Camp", "Right",    "Large"),
            (41.2,  "Buck Farm",            "Camp", "Right",    "Large"),
            (43.4,  "Anasazi Bridge",       "Camp", "Left",     "Small"),
            (43.6,  "Lower Anasazi",        "Camp", "Left",     "Small"),
            (44.0,  "Pres. Harding",        "Camp", "Left",     "Medium"),
            (44.5,  "Eminence",             "Camp", "Left",     "Large"),
            (45.0,  "Willie Taylor",        "Camp", "Left",     "Small"),
            (47.2,  "Duck-n-Quack",         "Camp", "Left",     "Small"),
            (47.2,  "Upper Saddle",         "Camp"  "Right",    "Large"),
            (47.7,  "Lower Saddle",         "Camp", "Right",    "Large"),
            (50.1,  "Dinosaur",             "Camp", "Right",    "Large"),
            (52.1,  "Little Nankoweap",     "Camp", "Right",    "Medium"),
            (53.1,  "Upper Nankoweap",      "Camp", "Right",    "Large"),
            (53.4,  "Main Nankoweap",       "Camp", "Right",    "Large"),
            (53.5,  "Lower Nankoweap",      "Camp", "Right",    "Medium"),
            (56.6,  "Kwagunt",              "Camp", "Right",    "Large"),
            (57.1,  "Below Kwagunt",        "Camp", "Right",    "Medium"),
            (58.0,  "Malagosa",             "Camp", "Right",    "Small"),
            (58.1,  "Opposite Malagosa",    "Camp", "Left",     "Medium"),
            (58.6,  "Awatubi",              "Camp", "Right",    "Medium"),
            (59.1,  "Below Awatubi",        "Camp", "Left",     "Small"),
            (60.2,  "60 Mile",              "Camp", "Right",    "Small"),
            (60.7,  "60 Mile Ledges",       "Camp", "Right",    "Small"),
            (61.1,  "61 Mile",              "Camp", "Right",    "Small"),
            (61.7,  "Above LCR",            "Camp", "Right",    "Medium"),
            (62.2,  "Below LCR"             "Camp", "Right",    "Small"),
            (63.0,  "Crash Canyon",         "Camp", "Right",    "Small"),
            (64.6,  "Carbon Creek",         "Camp", "Right",    "Large"),
            (65.9,  "Chuar/Lava Canyon",    "Camp", "Right",    "Medium"),
            (66.1,  "Palisades",            "Camp", "Left",     "Medium"),
            (66.8,  "Espejo",               "Camp", "Left",     "Small"),
            (67.7,  "Comanche",             "Camp", "Left",     "Small"),
            (68.3,  "Upper Tanner",         "Camp", "Right",    "Large"),
            (68.7,  "Tanner",               "Camp", "Right",    "Large"),
            (69.3,  "Below Tanner Rapid",   "Camp", "Left",     "Medium"),
            (70.1,  "Basalt",               "Camp", "Right",    "Medium"),
            (71.2,  "Cardenas",             "Camp", "Left",     "Medium"),
            (72.4,  "Upper Unkar",          "Camp", "Right",    "Medium"),
            (72.7,  "Unkar Left",           "Camp", "Left",     "Large"),
            (74.2,  "Anasazi Granary",      "Camp", "Left",     "Small"),
            (74.6,  "Upper Rattlesnake",    "Camp", "Right",    "Large"),
            (75.4,  "Escalante",            "Camp", "Left",     "Small"),
            (75.7,  "Upper Nevills",        "Camp", "Left",     "Small"),
            (76.1,  "Nevills",              "Camp", "Left",     "Large"),
            (76.3,  "Below Nevills",        "Camp", "Right",    "Medium"),
            (76.5,  "Papago",               "Camp", "Left",     "Medium"),
            (77.1,  "Hance",                "Camp", "Left",     "Medium"),
            (79.4,  "Below Sockdolager",    "Camp", "Left",     "Small"),
            (81.7,  "Grapevine",            "Camp", "Left",     "Large"),
            (84.6,  "Clear Creek",          "Camp", "Right",    "Small"),
            (84.8,  "Below Clear Creek",    "Camp", "Right",    "Small"),
            (85.0,  "Zoroaster",            "Camp", "Left",     "Medium"),
            (87.6,  "Upper Cremation",      "Camp", "Left",     "Medium"),
            (87.8,  "Lower Cremation",      "Camp", "Left",     "Medium"),
            (89.9,  "Pipe Creek",           "Camp", "Right",    "Small"),
            (91.7,  "91 Mile Creek",        "Camp", "Left",     "Small"),
            (92.1,  "Trinity Creek",        "Camp", "Right",    "Small"),
            (92.8,  "Above Salt Creek",     "Camp", "Left",     "Medium"),
            (93.2,  "Salt Creek",           "Camp", "Left",     "Small"),
            (93.8,  "Granite",              "Camp", "Left",     "Large"),
            (94.8,  "94 Mile Canyon",       "Camp", "Right",    "Small"),
            (95.2,  "Hermit",               "Camp", "Left",     "Medium"),
            (96.5,  "Schist",               "Camp", "Left",     "Medium"),
            (97.2,  "Boucher",              "Camp", "Left",     "Medium"),
            (98.7,  "Crystal",              "Camp", "Right",    "Medium"),
            (98.9,  "Ego Beach",            "Camp", "Right",    "Small"),
            (99.7,  "Willies Necktie",      "Camp", "Left",     "Small"),
            (100.1, "Lower Tuna",           "Camp", "Left",     "Large"),
            (103.4, "New Shady Grove",      "Camp", "Right",    "Medium"),
            (103.7, "103 Mile",             "Camp", "Right",    "Medium"),
            (104.4, "Emerald",              "Camp", "Right",    "Medium"),
            (108.7, "Hotauta",              "Camp", "Right",    "Medium"),
            (108.3, "Ross Wheeler",         "Camp", "Left",     "Small"),
            (108.5, "Parkins Inscription",  "Camp", "Right",    "Small"),
            (108.9, "Bass Crossing",        "Camp", "Right",    "Right"),
            (109.0, "Bass",                 "Camp", "Right",    "Large"),
            (110.0, "110 Mile",             "Camp", "Right",    "Large"),
            (112.8, "Waltenberg",           "Camp", "Right",    "Small"),
            (114.9, "Upper Garnet",         "Camp", "Right",    "Medium"),
            (115.1, "LowerGarnet",          "Camp", "Right",    "Medium"),
            (117.6, "Buckhorn Canyon",      "Camp", "Left",     "Small"),
            (118.3, "Below Elves Right",    "Camp", "Right",    "Small"),
            (119.1, "119 Mile",             "Camp", "Right",    "Small"),
            (119.4, "Big Dune",             "Camp", "Right",    "Medium"),
            (119.9, "119.8 Mile",           "Camp", "Right",    "Small"),
            (120.3, "120 Mile",             "Camp", "Left",     "Large"),
            (120.6, "Blacktail",            "Camp", "Right",    "Medium"),
            (120.6, "Opposite Blacktail",   "Camp", "Left",     "Small"),
            (120.7, "Lower Blacktail",      "Camp", "Right",    "Medium"),
            (120.8, "Below Blacktail",      "Camp", "Left",     "Large"),
            (121.4, "121.4 Mile",           "Camp", "Left",     "Small"),
            (122.3, "122.3 Mile",           "Camp", "Left",     "Small"),
            (122.8, "122 Mile Canyon",      "Camp", "Left",     "Large"),
            (123.2, "Upper Forster",        "Camp", "Left",     "Medium"),
            (123.6, "Below Forster",        "Camp", "Right",    "Medium"),
            (124.2, "Enfilade",             "Camp", "Left",     "Medium"),
            (125.5, "Fossil",               "Camp", "Left",     "Large"),
            (126.1, "Below Fossil",         "Camp", "Left",     "Medium"),
            (127.0, "Randys Rock",          "Camp", "Right",    "Large"),
            (131.7, "Below Bedrock",        "Camp", "Right",    "Large"),
            (132.2, "Galloway",             "Camp", "Right",    "Medium"),
            (132.5, "Stone Creek",          "Camp", "Right",    "Large"),
            (133.7, "Talking Heads",        "Camp", "Left",     "Medium"),
            (134.2, "Racetrack",            "Camp", "Right",    "Medium"),
            (134.4, "Lower Tapeats",        "Camp", "Right",    "Medium"),
            (134.8, "Above Owl Eyes",       "Camp", "Left",     "Large"),
            (135.2, "Owl Eyes",             "Camp", "Left",     "Large"),
            (136.6, "Junebug",              "Camp", "Left",     "Small"),
            (136.8, "Across Deer Creek",    "Camp", "Left",     "Medium"),
            (137.1, "OC's",                 "Camp", "Left",     "Large"),
            (137.6, "Pancho's Kitchen",     "Camp", "Left",     "Large"),
            (137.7, "Football Field",       "Camp", "Left",     "Large"),
            (137.8, "Backeddy",             "Camp", "Left",     "Large"),
            (138.6, "Doris",                "Camp", "Left",     "Medium"),
            (139.1, "139 Mile",             "Camp", "Left",     "Small"),
            (139.6, "Fishtail",             "Camp", "Right",    "Small"),
            (140.4, "Keyhole",              "Camp", "Left",     "Medium"),
            (143.9, "Above Kanab",          "Camp", "Left",     "Small"),
            (144.8, "Below Kanab",          "Camp", "Right",    "Medium"),
            (145.9, "Above Olo",            "Camp", "Left",     "Large"),
            (146.1, "Olo",                  "Camp", "Left",     "Small"),
            (148.4, "Opposite Matkat",      "Camp", "Right",    "Small"),
            (148.9, "Matkat Hotel",         "Camp", "Left",     "Medium"),
            (150.3, "Patch",                "Camp", "Right",    "Medium"),
            (150.7, "Upsey Hotel",          "Camp", "Left",     "Small"),
            (151.9, "Upper Ledges",         "Camp", "Right",    "Medium"),
            (152.1, "Ledges",               "Camp", "Right",    "Medium"),
            (156.3, "Last Chance",          "Camp", "Right",    "Medium"),
            (156.9, "Very Last Chance",     "Camp", "Right",    "Small"),
            (158.3, "First Chance",         "Camp", "Right",    "Small"),
            (158.7, "158.7 Mile",           "Camp", "Right",    "Medium"),
            (159.2, "Second Chance",        "Camp", "Right",    "Small"),
            (160.5, "160.5 Mile",           "Camp", "Left",     "Small"),
            (161.3, "161.3 Mile",           "Camp", "Right",    "Medium"),
            (165.1, "Above Tuckup",         "Camp", "Right",    "Small"),
            (165.2, "Tuckup",               "Camp", "Right",    "Large"),
            (165.4, "Below Tuckup",         "Camp", "Left",     "Small"),
            (165.7, "167.5 Mile",           "Camp", "Right",    "Small"),
            (167.0, "Upper National",       "Camp", "Left",     "Large"),
            (167.1, "Lower National",       "Camp", "Left",     "Large"),
            (167.5, "Below National",       "Camp", "Left",     "Small"),
            (168.8, "Fern Glen",            "Camp", "Right",    "Large"),
            (171.6, "Stairway Canyon",      "Camp", "Right",    "Medium"),
            (172.1, "Mohawk",               "Camp", "Left",     "Large"),
            (172.6, "172.6 Mile",           "Camp", "Left",     "Small"),
            (174.7, "Upper Cove",           "Camp", "Right",    "Medium"),
            (174.8, "Lower Cover",          "Camp", "Right",    "Large"),
            (176.3, "Below Red Slide",      "Camp", "Left",     "Large"),
            (177.6, "Honga Spring",         "Camp", "Left",     "Medium"),
            (178.1, "Above Anvil",          "Camp", "Left",     "Large"),
            (179.5, "Above Lava",           "Camp", "Left",     "Medium"),
            (180.1, "Below Lower Lava",     "Camp", "Right",    "Large"),
            (182.8, "Upper Chevron",        "Camp", "Right",    "Large"),
            (182.9, "Lower Chevron",        "Camp", "Right",    "Medium"),
            (183.3, "183.3 Mile",           "Camp", "Left",     "Medium"),
            (184.9, "184.9 Mile",           "Camp", "Left",     "Small"),
            (185.9, "Upper 185 Mile",       "Camp", "Right",    "Large"),
            (186.0, "Lower 185 Mile",       "Camp", "Right",    "Large"),
            (186.4, "186.4 Mile",           "Camp", "Left",     "Large"),
            (187.5, "Whitmore Helipad",     "Camp", "Left",     "Medium"),
            (188.4, "Whitmore Wash",        "Camp", "Right",    "Large"),
            (188.7, "Lower Whitmore",       "Camp", "Right",    "Large"),
            (190.4, "Granite Island",       "Camp", "Right",    "Small"),
            (190.7, "190.7 Mile",           "Camp", "Left",     "Small"),
            (191.5, "Upper Fat City",       "Camp", "Right",    "Medium"),
            (192.3, "Fat City",             "Camp", "Left",     "Large"),
            (193.3, "193.3 Mile",           "Camp", "Right",    "Small"),
            (194.6, "Hualapai Acres",       "Camp", "Left",     "Large"),
            (196.9, "Froggy Fault",         "Camp", "Left",     "Medium"),
            (197.0, "Below Froggy",         "Camp", "Left",     "Small"),
            (198.9, "Parashant",            "Camp", "Right",    "Medium"),
            (199.3, "Below Parashant",      "Camp", "Right",    "Medium"),
            (202.3, "202 Mile",             "Camp", "Right",    "Medium"),
            (202.9, "203 Mile",             "Camp", "Right",    "Medium"),
            (204.9, "Below Spring Canyon",  "Camp", "Right",    "Small"),
            (205.7, "205 Mile",             "Camp", "Left",     "Small"),
            (207.0, "Indian Canyon",        "Camp", "Right",    "Medium"),
            (207.9, "207.9 Mile",           "Camp", "Left",     "Small"),
            (209.1, "Granite Park",         "Camp", "Left",     "Large"),
            (209.8, "209.8 Mile",           "Camp", "Right",    "Large"),
            (210.2, "210.2 Mile",           "Camp", "Right",    "Large"),
            (211.9, "Upper Fall Canyon",    "Camp", "Right",    "Medium"),
            (212.0, "Lower Fall Canyon",    "Camp", "Right",    "Small"),
            (213.1, "213.1 Mile",           "Camp", "Right",    "Small"),
            (213.3, "Pumpkin Spring",       "Camp", "Left",     "Large"),
            (214.5, "214 Mile",             "Camp", "Right",    "Medium"),
            (216.1, "Opposite 3 Springs",   "Camp", "Right",    "Large"),
            (218.0, "217 Mile Rapid",       "Camp", "Left",     "Medium"),
            (220.0, "Upper 220 Mile",       "Camp", "Right",    "Large"),
            (220.1, "Middle 220 Mile",      "Camp", "Right",    "Medium"),
            (220.2, "Lower 220 Mile",       "Camp", "Right",    "Medium"),
            (221.6, "221 Mile",             "Camp", "Right",    "Large"),
            (222.2, "222 Mile",             "Camp", "Left",     "Large"),
            (223.7, "224 Mile",             "Camp", "Left",     "Medium"),
            (224.9, "224.9 Mile",           "Camp", "Left",     "Medium"),
            (225.7, "Last Chance Diamond",  "Camp", "Right",    "Small"),
            (226.3, "Truck Seat",           "Camp", "Right",    "Medium"),
            (227.3, "227.3 Mile",           "Camp", "Right",    "Medium"),
            (229.3, "Travertine Canyon",    "Camp", "Left",     "Medium"),
            (230.6, "Travertine Falls",     "Camp", "Left",     "Medium"),
            (231.0, "231 Mile",             "Camp", "Right",    "Medium"),
            (234.4, "234.4 Mile",           "Camp", "Right",    "Medium"),
            (235.3, "235.1 Mile",           "Camp", "Left",     "Medium"),
            (236.1, "Gneiss Canyon",        "Camp", "Right",    "Medium"),
            (236.7, "236.7 Mile",           "Camp", "Left",     "Medium"),
            (238.7, "Bridge City",          "Camp", "Left",     "Medium"),
            (239.8, "Separation Canyon",    "Camp", "Right",    "Medium"),
            (242.7, "242.7 Mile",           "Camp", "Right",    "Medium"),
            (243.0, "243 Mile",             "Camp", "Right",    "Medium"),
            (246.2, "Spenser Canyon",       "Camp", "Left",     "Medium"),
            (248.7, "Surprise Canyon",      "Camp", "Right",    "Medium"),
            (250.0, "Tomahawk",             "Camp", "Right",    "Medium"),
            (260.7, "Lower Quartermaster",  "Camp", "Left",     "Medium"),
            (264.6, "Dry Canyon",           "Camp", "Right",    "Medium"),
            (273.6, "273.6 Mile",           "Camp", "Left",     "Medium"),
            (279.4, "279.4 Mile",           "Camp", "Left",     "Medium"),
            (280.0, "280 Mile/Last Chance", "Camp", "Right",    "Medium")
        ]
        cdf = pd.DataFrame(camps, columns=['RM', 'Name', 'Type', 'Side', 'Size'])
        #cdf.set_index(['RM','Type'], drop=False, inplace=True)
        frames.append(cdf)

    if what in ['all','rapids']:
        rapids = [
            #   RM      Name                Feature     Rating(s)
            (0.2,   "Paria Riffle",         "Rapid",    1,  1,  1,  1),
            (2.8,   "Cathedral Wash",       "Rapid",    2,  2,  2,  2),
            (7.8,   "Badger Creek",         "Rapid",    5,  5,  6,  6),
            (7.8,   "Badger Creek",         "Rapid",    8,  7,  6,  5),
            (11.2,  "Soap Creek",           "Rapid",    6,  5,  5,  5),
            (12.8,  "Thirteen Mile",        "Rapid",    1,  1,  1,  1),
            (14.5,  "Sheer Wall",           "Rapid",    5,  4,  3,  2),
            (17.1,  "House Rock",           "Rapid",    9,  8,  7,  7),
            (17.4,  "Redneck",              "Rapid",    3,  3,  3,  3),
            (20.5,  "North Canyon",         "Rapid",    4,  4,  5,  5),
            (21.2,  "21 Mile",              "Rapid",    5,  5,  5,  5),
            (23.0,  "23 Mile",              "Rapid",    6,  5,  5,  4),
            (23.5,  "23.5 Mile",            "Rapid",    4,  4,  4,  4),
            (24.1,  "Georgie (24 Mi.)",     "Rapid",    8,  7,  6,  6),
            (24.5,  "24.5 Mile",            "Rapid",    6,  6,  5,  5),
            (24.9,  "25 Mile",              "Rapid",    7,  6,  5,  5),
            (25.5,  "Cave Springs",         "Rapid",    6,  5,  5,  6),
            (25.8,  "26 Mile",              "Rapid",    3,  3,  3,  3),
            (26.7,  "Tiger Wash",           "Rapid",    5,  4,  4,  4),
            (26.9,  "MNA",                  "Rapid",    4,  3,  1,  0),
            (29.2,  "29 Mile",              "Rapid",    3,  3,  3,  3),
            (36.0,  "36 Mile",              "Rapid",    4,  3,  3,  3),
            (43.7,  "Pres. Harding",        "Rapid",    4,  4,  4,  4),
            (52.2,  "Nankoweap",            "Rapid",    3,  3,  4,  4),
            (55.9,  "Kwagunt",              "Rapid",    6,  6,  6,  6),
            (59.7,  "60 Mile",              "Rapid",    4,  4,  4,  4),
            (65.5,  "Chuar",                "Rapid",    4,  3,  4,  5),
            (68.4,  "Tanner",               "Rapid",    4,  4,  4,  4),
            (72.4,  "Unkar",                "Rapid",    7,  7,  6,  6),
            (75.3,  "Nevills",              "Rapid",    6,  6,  6,  6),
            (76.7,  "Hance",                "Rapid",    9,  8,  7,  7),
            (78.5,  "Sockdolager",          "Rapid",    8,  8,  9,  9),
            (81.4,  "Grapevine",            "Rapid",    8,  8,  8,  8),
            (83.5,  "83 Mile",              "Rapid",    6,  5,  4,  3),
            (84.7,  "Zoroaster",            "Rapid",    8,  7,  6,  5),
            (85.2,  "85 Mile",              "Rapid",    5,  4,  4,  3),
            (87.9,  "Bright Angel",         "Rapid",    4,  4,  4,  4),
            (90.3,  "Horn Creek",           "Rapid",    9, 10,  8,  8),
            (93.4,  "Granite",              "Rapid",    8,  8,  9,  9),
            (94.8,  "Hermit",               "Rapid",    9,  8,  9,  9),
            (96.5,  "Boucher",              "Rapid",    5,  4,  4,  3),
            (98.1,  "Crystal",              "Rapid",   10,  8,  9, 10),
            (99.1,  "Tuna Creek",           "Rapid",    5,  5,  6,  6),
            (99.5,  "Lower Tuna",           "Rapid",    4,  4,  4,  4),
            (100.0, "Nixon Rock",           "Rapid",    5,  5,  5,  5),
            (100.5, "Agate",                "Rapid",    2,  3,  3,  4),
            (101.1, "Sapphire",             "Rapid",    7,  7,  7,  7),
            (101.9, "Turquoise",            "Rapid",    6,  5,  4,  3),
            (103.8, "Emerald (104 Mi.)",    "Rapid",    7,  6,  6,  5),
            (104.6, "Ruby",                 "Rapid",    7,  6,  6,  7),
            (105.9, "Serpentine",           "Rapid",    8,  7,  7,  6),
            (107.8, "Bass",                 "Rapid",    6,  5,  4,  3),
            (108.6, "Shinumo",              "Rapid",    4,  4,  5,  5),
            (109.8, "110 Mile",             "Rapid",    4,  3,  1,  0),
            (110.7, "Hakatai",              "Rapid",    4,  4,  4,  4),
            (112.2, "Waltenberg",           "Rapid",    9,  8,  7,  6),
            (112.5, "112 & 1/2 Mile",       "Rapid",    6,  4,  2,  1),
            (113.0, "Rancid Tuna",          "Rapid",    6,  6,  6,  6),
            (118.8, "119 Mile",             "Rapid",    4,  3,  2,  1),
            (120.6, "Blacktail",            "Rapid",    3,  3,  3,  3),
            (122.2, "122 Mile",             "Rapid",    4,  4,  5,  6),
            (123.3, "Forster",              "Rapid",    6,  6,  6,  6),
            (125.5, "Fossil",               "Rapid",    6,  7,  6,  6),
            (127.5, "127 Mile",             "Rapid",    4,  4,  3,  2),
            (129.2, "128 Mile",             "Rapid",    5,  5,  5,  5),
            (129.7, "Specter",              "Rapid",    8,  7,  6,  5),
            (131.1, "Bedrock",              "Rapid",    8,  8,  8,  8),
            (132.3, "Deubendorff",          "Rapid",    9,  8,  8,  7),
            (134.4, "Tapeats",              "Rapid",    8,  7,  6,  5),
            (135.4, "Helicopter Eddy",      "Rapid",    3,  3,  3,  3),
            (138.4, "Doris",                "Rapid",    5,  6,  6,  7),
            (139.2, "138.5 Mile",           "Rapid",    4,  4,  4,  4),
            (139.7, "Fishtale",             "Rapid",    7,  6,  6,  5),
            (141.7, "141 Mile",             "Rapid",    2,  2,  2,  2),
            (144.0, "Kanab",                "Rapid",    4,  3,  3,  3),
            (148.4, "Matkatimiba",          "Rapid",    2,  2,  2,  2),
            (150.2, "Upset",                "Rapid",    9,  8,  8,  6),
            (154.0, "Sinyala",              "Rapid",    2,  2,  2,  2),
            (165.0, "164 Mile",             "Rapid",    3,  3,  3,  3),
            (167.0, "National",             "Rapid",    2,  2,  2,  2),
            (168.5, "Fern Glen",            "Rapid",    3,  3,  3,  3),
            (171.9, "Gateway",              "Rapid",    3,  3,  3,  3),
            (179.7, "Lava Falls",           "Rapid",   10, 10, 10, 10),
            (180.1, "Lower Lava",           "Rapid",    5,  5,  5,  5),
            (186.0, "185 Mile",             "Rapid",    2,  2,  2,  2),
            (188.3, "Whitmore",             "Rapid",    3,  3,  3,  3),
            (205.6, "205 Mile (Kolb)",      "Rapid",    8,  7,  7,  6),
            (209.2, "209 Mile",             "Rapid",    7,  7,  7,  7),
            (212.5, "Little Bastard",       "Rapid",    7,  5,  3,  1),
            (216.0, "Three Springs",        "Rapid",    2,  2,  2,  2),
            (217.8, "217 Mile",             "Rapid",    4,  4,  5,  4),
            (220.7, "Granite Springs",      "Rapid",    2,  2,  2,  2),
            (223.7, "224 Mile",             "Rapid",    2,  3,  3,  4),
            (225.9, "Diamond Creek",        "Rapid",    4,  4,  4,  4),
            (229.3, "Travertine",           "Rapid",    2,  2,  2,  2),
            (231.2, "231 Mile",             "Rapid",    7,  6,  5,  4),
            (232.5, "Killer Fang Falls",    "Rapid",    7,  6,  5,  4),
            (233.9, "234 Mile",             "Rapid",    6,  5,  4,  4),
            (235.3, "Bridge Canyon",        "Rapid",    6,  5,  4,  3),
            (236.0, "Gneiss Canyon",        "Rapid",    6,  5,  4,  3),
            (280.8, "Pearce Ferry",         "Rapid",   10, 10, 10, 10)
        ]
        rdf = pd.DataFrame.from_records(rapids,
                                        columns=['RM', 'Name', 'Type',
                                                 'VeryLow', 'Low', 'Medium', 'High'])
        #rdf.set_index('RM', drop=True, inplace=True)
        frames.append(rdf)

    # hikes
    if what in ['all','hikes']:
        hikes = [
            (0.0,   "Lee's Ferry",              "Hike", "Right"),
            (12.1,  "Browns Inscription",       "Hike", "Left"),
            (53.3,  "Nankoweap",                "Hike", "Right"),
            (61.9,  "Little Colorado",          "Hike", "Left"),
        ]
        hdf = pd.DataFrame(hikes, columns=['RM', 'Name', 'Type', 'Side'])
        #hdf.set_index('RM', drop=True, inplace=True)
        frames.append(hdf)

    # everything else...
    if what in ['all', 'misc']:
        misc = [
            (0.0,   "Lee's Ferry",          "Access",   "Right"),
            (31.9,  "Vaseys Paradise",      "Water",    "Right"),
            (53.2,  "Nankoweap Creek",      "Water",    "Right"),
            (66.1,  "Palisade Creek",       "Water",    "Right"),
            (88.2,  "Phantom Ranch",        "Access",   "Right"),
            (93.9,  "Monument Creek",       "Water",    "Left"),
            (95.2,  "Hermit Creek",         "Water",    "Left"),
            (98.9,  "Ego Beach",            "Water",    "Right"),
            (109.2, "Shinumo Creek",        "Water",    "Right"),
            (116.5, "Elves Chasm",          "Water",    "Left"),
            (120.6, "Blacktail Creek",      "Water",    "Right"),
            (134.3, "Tapeats Creek",        "Water",    "Right"),
            (136.9, "Deer Creek",           "Water",    "Right"),
            (144.0, "Kanab Creek",          "Water",    "Right"),
            (148.5, "Matkatimiba Canyon",   "Water",    "Left"),
            (225.7, "Diamond Creek",        "Access",   "Left")
        ]
        mdf = pd.DataFrame(misc, columns=['RM', 'Name', 'Type', 'Side'])
        #mdf.set_index('RM', drop=True, inplace=True)
        frames.append(mdf)

    for df in frames:
        if df is None:
            continue
        if miles is None:
            miles = df
        else:
            miles = pd.concat([miles, df], axis=0)

    return miles

def get_flows(start_date=None):
    if start_date is None:
        period = 'P1D'
    else:
        period = 'P1D'

    stations = gcgauges()
    parameter = '00060'
    flows = None
    for s in stations['ID']:
        d = nwis.get_site_data(s, service='iv', parameter_code=parameter, period=period)
        fd = pd.DataFrame(d['00060:00011']['values'])
        # fd[['value']] = fd[['value']].astype(int)
        fd = fd.rename(columns={'value': s})
        fd.drop('qualifiers', axis=1, inplace=True)
        fd.set_index('datetime', drop=True, inplace=True)
        if flows is None:
            # flows['datetime'] = pd.to_datetime(fd['datetime'])
            flows = fd
            print(flows)
        else:
            flows = pd.concat([flows, fd], axis=1)
            print(flows)
    plt.figure()
    flows.plot(x='index')

    return flows


if __name__ == '__main__':
    print("in gctides")
    # flows = get_flows("2016-06-01")
    print(gcmiles(what=['camps','rapids']))
