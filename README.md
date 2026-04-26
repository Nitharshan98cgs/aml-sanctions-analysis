# OFAC SDN List — AML Sanctions Analysis & Dashboard

## What This Project Does
Python and Power BI analysis of the OFAC Specially Designated Nationals 
(SDN) list — the live sanctions database used by financial institutions 
globally for transaction screening and sanctions compliance.

## Key Findings
- 18,864 sanctioned entries analysed
- Russia EO14024 is the largest sanctions program — bigger than Iran, 
  North Korea, and Global Terrorism combined
- 7,430 sanctioned individuals | 1,480 vessels | 344 aircraft
- 50.96% of entries are aliases — explaining why name-matching 
  generates false positives in daily screening
- Built to understand the data structure behind daily sanctions 
  screening work

## What's Included
- `ofac_analyser.py` — Python script analysing the full SDN dataset
- `entity_types.png` — Entity type breakdown chart
- `sanctions_programs.png` — Top sanctions programs chart
- `OFAC_Dashboard.pbix` — Interactive Power BI dashboard file

## Tools Used
- Python 3
- pandas
- matplotlib
- Microsoft Power BI

## Author
Nitharshan Sridharan
Financial Crime Analyst — Dublin
linkedin.com/in/nitharshan-sridharan-014156229
