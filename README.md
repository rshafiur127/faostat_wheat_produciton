# faostat_wheat_produciton
Collect data from faostat and through data preparation make it up to dashboard

FAO is Food and Agriculture Organization of UN. Faostat preserve the data collected by FAO. 

They also developed a Python package called 'faostat'. 

https://pypi.org/project/faostat/

Which helps to read data from Faostat API. 

# Pipeline
For data pipeline we used only Mage

And as infustructure we used docker image locally. In Google Cloud we used BigQuery, GCS, Looker Studio. 

All the codes are in the mage and infrastructure repo.

# Dashboard location

https://lookerstudio.google.com/reporting/a2fea42b-0668-4077-a80a-53677e7c24be

<img width="603" alt="image" src="https://github.com/rshafiur127/faostat_wheat_produciton/assets/21085351/ea559afc-9d21-4fa4-9c75-393774e1765f">

We can use filter to select specific country and/or time line

<img width="603" alt="image" src="https://github.com/rshafiur127/faostat_wheat_produciton/assets/21085351/a6d17cf8-f9af-49c8-8dc5-cfcb52f036b7">

<img width="600" alt="image" src="https://github.com/rshafiur127/faostat_wheat_produciton/assets/21085351/f4e4d899-2eee-409e-a428-d6358ed3c814">

