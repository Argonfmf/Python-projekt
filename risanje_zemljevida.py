import plotly.graph_objects as go
import requests
import re

ime_zivali = input('Vnesite ime živali: ')
ime = ime_zivali
if ' ' in ime_zivali:
    ime_zivali = ime_zivali.replace(' ', '-')
ime_zivali = ime_zivali.lower()
url1 = 'https://a-z-animals.com/animals/'+ ime_zivali +'/'
html1 = requests.get(url1).text
c1 = re.findall(r'<a href="/animals/location/[^<]+', html1)
if len(c1) == 0:
    print('Takšno ime živali ne obstaja ali pa te živali nimamo v naši bazi podatkov. V primeru, da stran prepoveduje vpogled, prosimo poskusite kasneje.')
else:
    lokacija = []
    for j in range(len(c1)):
        lokacija.append(c1[j].split('">')[1])

    vsi_kontinenti = {'Africa': ['Angola', 'Burkina Faso', 'Burundi', 'Benin', 'Botswana', 'Democratic Republic of Congo', 'Central African Republic', 'Republic of Congo',
                                 "Côte d'Ivoire", 'Cameroon', 'Djibouti', 'Algeria', 'Egypt', 'Eritrea', 'Ethiopia', 'Gabon', 'Ghana', 'Gambia', 'Guinea', 'Equatorial Guinea',
                                 'Guinea-Bissau', 'Kenya', 'Liberia', 'Lesotho', 'Libya', 'Morocco', 'Madagascar', 'Mali', 'Mauritania', 'Malawi', 'Mozambique', 'Namibia', 'Niger',
                                 'Nigeria', 'Rwanda', 'Sudan', 'Sierra Leone', 'Senegal', 'Somalia', 'South Sudan', 'Swaziland', 'Chad', 'Togo', 'Tunisia', 'Tanzania', 'Uganda', 'South Africa', 'Zambia', 'Zimbabwe', 'Western Sahara'],
                      'Asia': ['United Arab Emirates', 'Afghanistan', 'Bangladesh', 'Brunei Darussalam', 'Bhutan', 'China', 'Indonesia', 'Indonesia (Southern Borneo)', 'Indonesia (Islands)', 'Indonesia (Java)', 'Indonesia (Sulawesi)',
                               'Israel', 'India', 'Iraq', 'Iran', 'Jordan', 'Japan', 'Kyrgyzstan', 'Cambodia', 'North Korea', 'South Korea', 'Kuwait', "Lao People's Democratic Republic", 'Lebanon', 'Sri Lanka', 'Myanmar', 'Mongolia',
                               'Malaysia', 'Malaysia (Northern Borneo)', 'Nepal', 'Oman', 'Philippines', 'Pakistan', 'Palestinian Territories', 'Qatar', 'Saudi Arabia', 'Syria', 'Thailand', 'Tajikistan', 'Timor-Leste', 'Turkmenistan',
                               'Taiwan', 'Uzbekistan', 'Vietnam', 'Yemen'],
                      'Central-America': ['Bahamas', 'Belize', 'Costa Rica', 'Cuba', 'Dominican Republic', 'Guatemala', 'Honduras', 'Haiti', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Puerto Rico', 'El Salvador', 'Trinidad and Tobago'],
                      'Eurasia': ['Kazakhstan', 'Russia'],
                      'Europe': ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Bosnia and Herzegovina', 'Belgium', 'Bulgaria', 'Belarus', 'Switzerland', 'Cyprus', 'Czech Republic', 'Germany', 'Denmark', 'Estonia', 'Spain', 'Finland',
                                 'France', 'United Kingdom', 'Georgia', 'Greece', 'Croatia', 'Hungary', 'Ireland', 'Iceland', 'Italy', 'Lithuania', 'Luxembourg', 'Latvia', 'Moldova', 'Montenegro', 'Macedonia', 'Netherlands', 'Norway',
                                 'Poland', 'Portugal', 'Romania', 'Serbia', 'Russia (Kaliningrad Oblast)', 'Sweden', 'Slovenia', 'Svalbard and Jan Mayen', 'Slovakia', 'Turkey', 'Ukraine', 'Kosovo'],
                      'North-America': ['Canada', 'Greenland', 'United States', 'United States (Alaska)', 'United States (Hawaii)'],
                      'Ocean': ['Southern Ocean', 'Arctic', 'Great Lakes', 'Indian', 'Mediterranean-Caspian', 'North Atlantic', 'Northeast Pacific', 'Northwest Pacific', 'South Atlantic', 'Southeast Pacific', 'Southwest Pacific'],
                      'Oceania': ['Australia', 'Australia (Tasmania)', 'Fiji', 'Indonesia (Papua)', 'New Caledonia', 'New Zealand', 'Papua New Guinea', 'Solomon Islands', 'French Southern and Antarctic Lands', 'Vanuatu'],
                      'South-America': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Falkland Islands', 'French Guiana', 'Guyana', 'Peru', 'Paraguay', 'Suriname', 'Uruguay', 'Venezuela']}

    vse_kratice_drzav = {'Afghanistan': 'AFG', 'Aland Islands': 'ALA', 'Albania': 'ALB', 'Algeria': 'DZA', 'American Samoa': 'ASM', 'Andorra': 'AND', 'Angola': 'AGO', 'Anguilla': 'AIA', 'Antarctica': 'ATA', 'Antigua and Barbuda': 'ATG', 'Argentina': 'ARG', 'Armenia': 'ARM', 'Aruba': 'ABW', 'Australia': 'AUS', 'Austria': 'AUT', 'Azerbaijan': 'AZE', 'Bahamas': 'BHS', 'Bahrain': 'BHR', 'Bangladesh': 'BGD', 'Barbados': 'BRB', 'Belarus': 'BLR', 'Belgium': 'BEL', 'Belize': 'BLZ', 'Benin': 'BEN', 'Bermuda': 'BMU', 'Bhutan': 'BTN', 'Bolivia': 'BOL', 'Bosnia and Herzegovina': 'BIH', 'Botswana': 'BWA', 'Bouvet Island': 'BVT', 'Brazil': 'BRA', 'British Virgin Islands': 'VGB', 'British Indian Ocean Territory': 'IOT', 'Brunei Darussalam': 'BRN', 'Bulgaria': 'BGR', 'Burkina Faso': 'BFA', 'Burundi': 'BDI', 'Cambodia': 'KHM', 'Cameroon': 'CMR', 'Canada': 'CAN', 'Cape Verde': 'CPV', 'Cayman Islands ': 'CYM', 'Central African Republic': 'CAF', 'Chad': 'TCD', 'Chile': 'CHL', 'China': 'CHN', 'Hong Kong, SAR China': 'HKG', 'Macao, SAR China': 'MAC', 'Christmas Island': 'CXR', 'Cocos (Keeling) Islands': 'CCK', 'Colombia': 'COL', 'Comoros': 'COM', 'Cook Islands ': 'COK', 'Costa Rica': 'CRI', "Côte d'Ivoire": 'CIV', 'Croatia': 'HRV', 'Cuba': 'CUB', 'Cyprus': 'CYP', 'Czech Republic': 'CZE', 'Democratic Republic of Congo': 'COD', 'Denmark': 'DNK', 'Djibouti': 'DJI', 'Dominica': 'DMA', 'Dominican Republic': 'DOM', 'Ecuador': 'ECU', 'Egypt': 'EGY', 'El Salvador': 'SLV', 'Equatorial Guinea': 'GNQ', 'Eritrea': 'ERI', 'Estonia': 'EST', 'Ethiopia': 'ETH', 'Falkland Islands (Malvinas) ': 'FLK', 'Faroe Islands': 'FRO', 'Fiji': 'FJI', 'Finland': 'FIN', 'France': 'FRA', 'French Guiana': 'GUF', 'French Polynesia': 'PYF', 'French Southern and Antarctic Lands': 'ATF', 'Gabon': 'GAB', 'Gambia': 'GMB', 'Georgia': 'GEO', 'Germany': 'DEU', 'Ghana': 'GHA', 'Gibraltar ': 'GIB', 'Greece': 'GRC', 'Greenland': 'GRL', 'Grenada': 'GRD', 'Guadeloupe': 'GLP', 'Guam': 'GUM', 'Guatemala': 'GTM', 'Guernsey': 'GGY', 'Guinea': 'GIN', 'Guinea-Bissau': 'GNB', 'Guyana': 'GUY', 'Haiti': 'HTI', 'Heard and Mcdonald Islands': 'HMD', 'Holy See (Vatican City State)': 'VAT', 'Honduras': 'HND', 'Hungary': 'HUN', 'Iceland': 'ISL', 'India': 'IND', 'Indonesia': 'IDN', 'Iran, Islamic Republic of': 'IRN', 'Iraq': 'IRQ', 'Ireland': 'IRL', 'Isle of Man ': 'IMN', 'Israel': 'ISR', 'Italy': 'ITA', 'Jamaica': 'JAM', 'Japan': 'JPN', 'Jersey': 'JEY', 'Jordan': 'JOR', 'Kazakhstan': 'KAZ', 'Kenya': 'KEN', 'Kiribati': 'KIR', 'Kosovo': 'KSV', 'Kuwait': 'KWT', 'Kyrgyzstan': 'KGZ', "Lao People's Democratic Republic": 'LAO', 'Latvia': 'LVA', 'Lebanon': 'LBN', 'Lesotho': 'LSO', 'Liberia': 'LBR', 'Libya': 'LBY', 'Liechtenstein': 'LIE', 'Lithuania': 'LTU', 'Luxembourg': 'LUX', 'Macedonia, Republic of': 'MKD', 'Madagascar': 'MDG', 'Malawi': 'MWI', 'Malaysia': 'MYS', 'Maldives': 'MDV', 'Mali': 'MLI', 'Malta': 'MLT', 'Marshall Islands': 'MHL', 'Martinique': 'MTQ', 'Mauritania': 'MRT', 'Mauritius': 'MUS', 'Mayotte': 'MYT', 'Mexico': 'MEX', 'Micronesia, Federated States of': 'FSM', 'Moldova': 'MDA', 'Monaco': 'MCO', 'Mongolia': 'MNG', 'Montenegro': 'MNE', 'Montserrat': 'MSR', 'Morocco': 'MAR', 'Mozambique': 'MOZ', 'Myanmar': 'MMR', 'Namibia': 'NAM', 'Nauru': 'NRU', 'Nepal': 'NPL', 'Netherlands': 'NLD', 'Netherlands Antilles': 'ANT', 'New Caledonia': 'NCL', 'New Zealand': 'NZL', 'Nicaragua': 'NIC', 'Niger': 'NER', 'Nigeria': 'NGA', 'Niue ': 'NIU', 'Norfolk Island': 'NFK', 'Northern Mariana Islands': 'MNP', 'North Korea': 'PRK', 'Norway': 'NOR', 'Oman': 'OMN', 'Pakistan': 'PAK', 'Palau': 'PLW', 'Palestinian Territories': 'PSE', 'Panama': 'PAN', 'Papua New Guinea': 'PNG', 'Paraguay': 'PRY', 'Peru': 'PER', 'Philippines': 'PHL', 'Pitcairn': 'PCN', 'Poland': 'POL', 'Portugal': 'PRT', 'Puerto Rico': 'PRI', 'Qatar': 'QAT', 'Republic of Congo': 'COG', 'Réunion': 'REU', 'Romania': 'ROU', 'Russian Federation': 'RUS', 'Rwanda': 'RWA', 'Saint-Barthélemy': 'BLM', 'Saint Helena': 'SHN', 'Saint Kitts and Nevis': 'KNA', 'Saint Lucia': 'LCA', 'Saint-Martin (French part)': 'MAF', 'Saint Pierre and Miquelon ': 'SPM', 'Saint Vincent and Grenadines': 'VCT', 'Samoa': 'WSM', 'San Marino': 'SMR', 'Sao Tome and Principe': 'STP', 'Saudi Arabia': 'SAU', 'Senegal': 'SEN', 'Serbia': 'SRB', 'Seychelles': 'SYC', 'Sierra Leone': 'SLE', 'Singapore': 'SGP', 'Slovakia': 'SVK', 'Slovenia': 'SVN', 'Solomon Islands': 'SLB', 'Somalia': 'SOM', 'South Africa': 'ZAF', 'South Georgia and the South Sandwich Islands': 'SGS', 'South Korea': 'KOR', 'South Sudan': 'SSD', 'Spain': 'ESP', 'Sri Lanka': 'LKA', 'Sudan': 'SDN', 'Suriname': 'SUR', 'Svalbard and Jan Mayen Islands ': 'SJM', 'Swaziland': 'SWZ', 'Sweden': 'SWE', 'Switzerland': 'CHE', 'Syrian Arab Republic (Syria)': 'SYR', 'Taiwan, Republic of China': 'TWN', 'Tajikistan': 'TJK', 'Tanzania, United Republic of': 'TZA', 'Thailand': 'THA', 'Timor-Leste': 'TLS', 'Togo': 'TGO', 'Tokelau ': 'TKL', 'Tonga': 'TON', 'Trinidad and Tobago': 'TTO', 'Tunisia': 'TUN', 'Turkey': 'TUR', 'Turkmenistan': 'TKM', 'Turks and Caicos Islands ': 'TCA', 'Tuvalu': 'TUV', 'Uganda': 'UGA', 'Ukraine': 'UKR', 'United Arab Emirates': 'ARE', 'United Kingdom': 'GBR', 'United States of America': 'USA', 'US Minor Outlying Islands': 'UMI', 'Uruguay': 'URY', 'Uzbekistan': 'UZB', 'Vanuatu': 'VUT', 'Venezuela (Bolivarian Republic)': 'VEN', 'Vietnam': 'VNM', 'Virgin Islands, US': 'VIR', 'Wallis and Futuna Islands ': 'WLF', 'Western Sahara': 'ESH', 'Yemen': 'YEM', 'Zambia': 'ZMB', 'Zimbabwe': 'ZWE'}

    kratice_drzav = vse_kratice_drzav

    # nova_tab prejme kratice držav/območij na katerih živi iskana žival
    nova_tab = []
    for i in range(len(lokacija)):
        for kljuc, vrednost in vsi_kontinenti.items():
            if lokacija[i] == kljuc:
                for k in range(len(vrednost)):
                    for kljuc1, vrednost1 in kratice_drzav.items():
                        if vrednost[k] in kljuc1:
                            nova_tab.append(vrednost1)

    z = []
    for j in range(len(nova_tab)):
        z.append('1')
        
    fig = go.Figure(data=go.Choropleth(
        locations = nova_tab,
        z = z,
        colorscale = 'algae',
        marker_line_color='darkgray',
        marker_line_width=0.5
    ))

    fig.update_traces(showscale=False)

    if 'Ocean' in lokacija:
        fig.update_geos(showocean = True)

    fig.update_layout(
        title_text= ime +' živi tukaj'
    )

    fig.show()
