# BAE305 Lab 10: Python and AI
**Author: Seth Daniel**

**Date: April 23rd, 2025**

## Introduction
   This lab aimed to develop software tools using Python and a large language model (LLM) to analyze water quality data. By leveraging libraries like pandas and Streamlit, we created user-friendly functions to filter, clean, and visualize data from real-world environmental datasets provided by the USGS. This hands-on exercise demonstrated how AI-assisted programming can streamline data processing and enhance accessibility to complex information through intuitive web apps.

Throughout the lab, we worked with two datasets: one containing metadata on water quality monitoring stations and another with detailed water quality test results. Using Python and AI-generated code, we built functions to extract site information, plot time-series contaminant trends, and develop an interactive Streamlit app. This lab reinforced data science and environmental engineering concepts and introduced tools and techniques used in real-world data analysis and app development.

## Materials
1. A computer running Arduino IDE
2. Chrome

## Assembly Methods
**Part 1:**

  The lab began with the setup of the development environment and data files. The station.csv file, downloaded from Canvas, was uploaded to the selected cloud-based IDE (Google Colab, Anaconda, or similar). A Python script was created with the help of an LLM AI to read the CSV using the pandas library and extract relevant station information. 
  The data was examined to identify useful headers like site name, latitude, and longitude. A filtering function was assembled to eliminate duplicate entries and organize the station data. Next, a function was generated to create a simple map visualization using libraries such as matplotlib or folium, plotting each unique station as a point based on its geographic coordinates. ChatGPT model GPT-4-turbo was used to generate the code for this part of the lab, and the prompts used for generation are given in the Test Results section. The 
code used for this portion of the lab is provided below.

<div align="center">
<img src="https://github.com/user-attachments/assets/f5d134a1-717f-4653-8f16-a870d522c0fc" alt="1" width="600">
<br/>
<figcaption style="font-size: 16px; text-align: center;"> Figure 1: ChatGPT Python pandas database code for Part 1 of the lab. </figcaption>
</div> 

<br/>


**Part 2:**

   For the second phase, the narrowresult.csv file was uploaded and analyzed. An LLM-assisted Python script was written to load the file and filter it by a specific water quality characteristic, such as dissolved oxygen or nitrate levels. The script grouped the data by monitoring station and time, then plotted each station's measurements over time using distinct line colors. 
   After the initial plot was successfully created, the script was modified to support filtering and plotting two characteristics at once. This required adjustments to the data selection logic and plotting code to ensure that both contaminants could be visualized together, clearly labeled and color-coded.
<br/>

<div align="center">
<img src="https://github.com/user-attachments/assets/0a842836-0a8f-4369-a520-160d9e89d9b5" alt="2" width="600">
<br/>
<figcaption style="font-size: 16px; text-align: center;"> Figure 2: ChatGPT generated code for narrowresults data from part 2. </figcaption>
</div> 

<br/>

**Part 3:**

  In the final section, a GitHub repository was created to host the Streamlit app. A new file named streamlit_app.py was initialized in the main branch. Within the Streamlit portal, the app was deployed by linking to the GitHub repo. Using the LLM, Python code was generated to build an interactive app allowing users to upload both CSV files, select a contaminant, and specify value and date ranges. 
  The app dynamically updated a map showing station locations with matching data and a time-series plot summarizing the contaminant’s trends. After the app was functional, a requirements.txt file was created listing libraries like pandas, streamlit, and matplotlib, ensuring the app could install all dependencies during deployment.

<div align="center">
<img src="https://github.com/user-attachments/assets/26a13012-f640-4757-b779-9b3e9401fd34" alt="Code 1" width="600">
<br/>
<figcaption style="font-size: 16px; text-align: center;"> Figure 3: ChatGPT generated streamlit app code for part 3 of the lab. </figcaption>
</div> 

<br/>

<div align="center">
<img src="https://github.com/user-attachments/assets/a84f7e80-fdf7-4242-8f83-abc04ae52cbf" alt="Code 2" width="600">
<br/>
<figcaption style="font-size: 16px; text-align: center;"> Figure 4: Rest of the ChatGPT generated code for part 3 of the lab. </figcaption>
</div> 


## Test Equipment

1. Computer
2. Python IDE
   
## Test Procedures

**Part 1:**
   
   Testing for this section began by confirming that station.csv was readable and correctly parsed. The filtering function was run to ensure all monitoring sites were uniquely listed and that no locations were duplicated. The map output was inspected to check that every station appeared in a valid location with appropriate spacing and no missing coordinates. If errors such as NaNs or repeated names appeared, the script was adjusted and re-tested. Function outputs were validated against the raw CSV file opened in Excel or Google Sheets.

**Part 2:**

   For narrowresult.csv, tests focused on verifying that the correct water quality characteristic was selected and plotted over time. The resulting graphs were checked to make sure each station had a distinct line and that timestamps aligned with the data values. When the code was updated to include two parameters, testing involved selecting various combinations of characteristics and verifying that both were plotted clearly, with legends and color distinctions. Edge cases—such as selecting a rare parameter or a station with sparse data—were also tested to ensure the plot didn’t break or show misleading results.

**Part 3:**

  Streamlit app testing involved using the web interface to upload the two CSV files and interact with the filtering options. The contaminant selector was tested with both common and rare inputs to confirm accurate data handling. Range sliders for value and date were adjusted to verify responsive updates in the map and trend graph. If selecting extreme or empty ranges produced no data, the app was checked for error-handling behavior. The app’s map was confirmed to update based on user input, and the plot was evaluated for clarity and responsiveness. Final tests ensured that the app loaded successfully via the deployed Streamlit URL and performed consistently across browsers. The app’s functionality was cross-verified with the original Python scripts to ensure data alignment.


## Test Results:

**Website/App Output**

<div align="center">
<img src="https://github.com/user-attachments/assets/5abd1887-943f-4bfb-aade-faa9f5ae9fcd" alt="web" width="600">
<br/>
<figcaption style="font-size: 16px; text-align: center;"> Figure 5: Station locations map generated by streamlit app ChatGPT code. </figcaption>
</div> 

<br/>

<div align="center">
<img src="https://github.com/user-attachments/assets/7a83a752-2640-4ea6-8258-9c7412442957" alt="Water Quality Plotting" width="400">
<br/>
<figcaption style="font-size: 16px; text-align: center;"> Figure 6: Water quality parameters on site generated by code. </figcaption>
</div> 

<br/>

**Link to Code Repository**
https://github.com/SethDaniel23/BAE305-Lab-10

**Link to App**
https://bae305-lab-10.streamlit.app/

**AI Assistance For Part 1**

| Goal   | Give AI directions for accessing data for part 1 of the lab |
|--------|-------------------------------------------------------------|
| Model  | ChatGPT GPT-4-turbo                                         |
| Prompt | generate a Python function that accesses the database, filters for the names of water quality measurement sites, and displays the location information for all sites without repetition |


| Goal   | Give AI directions for making the map for part 1 of the lab |
|--------|-------------------------------------------------------------|
| Model  | ChatGPT GPT-4-turbo                                         |
| Prompt | create a map that pinpoints the location of every station in the database |


**AI Assistance For Part 2**

| Goal   | Tell AI to access data file for part 2 |
|--------|----------------------------------------|
| Model  | ChatGPT GPT-4-Turbo                    |
| Prompt | generate a Python function that accesses the narrowresults.csv database, filters for a desired water quality characteristic, and plots the results. Each site should be represented as a separate line with a different color, where the Y-axis represents the measured values and the X-axis represents time. |

| Goal   | Get ChatGPT to allow two characteristics at once |
|--------|--------------------------------------------------------------------|
| Model  | ChatGPT GPT-4-Turbo                                                |
| Prompt | modify the code such that you can ask for two characteristics at the same time. |

**AI Assistance for Part 3**

| Goal   | Ask AI to combine the code from Part 1 and Part 2 |
|--------|--------------------------------------------------------------------|
| Model  | ChatGPT GPT-4-Turbo                                                |
| Prompt | develop a Streamlit app that allows the user to upload both databases used in Part 1 and 2, to search for a contaminant in the databases. Once a contaminant has been selected you should be able to define the range of values and dates that you want to show. After modifying the ranges, update the map showing the location of the stations with the contaminant within that range and measured during the time frame. It should also show you a trend over time of the contaminant in all the stations shown. |

| Goal   | Debug code for streamlit application |
|--------|--------------------------------------|
| Model  | ChatGPT GPT-4-Turbo                  |
| Prompt | can the code just get the files from the repository |

| Goal   | Help AI understand station.csv file for streamlit application |
|--------|---------------------------------------------------------------|
| Model  | ChatGPT GPT-4-Turbo                                           |
| Prompt | station headers: OrganizationIdentifier	OrganizationFormalName	MonitoringLocationIdentifier	MonitoringLocationName	MonitoringLocationTypeName	MonitoringLocationDescriptionText	HUCEightDigitCode DrainageAreaMeasure/MeasureValue	DrainageAreaMeasure/MeasureUnitCode	ContributingDrainageAreaMeasure/MeasureValue	ContributingDrainageAreaMeasure/MeasureUnitCode	LatitudeMeasure	LongitudeMeasure	SourceMapScaleNumeric	HorizontalAccuracyMeasure/MeasureValue	HorizontalAccuracyMeasure/MeasureUnitCode	HorizontalCollectionMethodName	HorizontalCoordinateReferenceSystemDatumName	VerticalMeasure/MeasureValue	VerticalMeasure/MeasureUnitCode	VerticalAccuracyMeasure/MeasureValue	VerticalAccuracyMeasure/MeasureUnitCode	VerticalCollectionMethodName	VerticalCoordinateReferenceSystemDatumName	CountryCode	StateCode	CountyCode	AquiferName	LocalAqfrName	FormationTypeText	AquiferTypeName	ConstructionDateText	WellDepthMeasure/MeasureValue	WellDepthMeasure/MeasureUnitCode	WellHoleDepthMeasure/MeasureValue	WellHoleDepthMeasure/MeasureUnitCode	ProviderName |

## Discussion:
This lab demonstrated how AI-generated Python code can be applied to real-world environmental datasets for analysis and visualization. Using USGS water quality data, the lab explored the capabilities of tools like pandas and Streamlit to filter, map, and plot water quality trends by location and contaminant. While the AI-generated code provided a solid foundation, some corrections were needed, such as renaming undefined variables and ensuring consistency with the actual dataset structure.

One challenge was aligning the AI's assumptions with the dataset being used. For example, the variable df had to be changed to usgs_data, and column names had to be verified before plotting. Despite these small issues, the process highlighted how AI can accelerate the development of data-driven applications when paired with human judgment and debugging skills.

The use of Streamlit made it easy to turn the analysis into an interactive web app, allowing users to select monitoring stations and contaminants and instantly view time-series plots. This approach has real potential in public-facing tools that communicate environmental data in an accessible way.

## Conclusion:
This lab successfully combined Python programming, AI-generated code, and real-world USGS water quality data to create an interactive data visualization tool. Through this exercise, it became clear that AI tools can significantly streamline coding tasks, especially for building visualizations and interfaces. However, human oversight remains essential for debugging and contextual understanding.

The final Streamlit app allows users to explore trends in water contaminants over time at selected locations, demonstrating how environmental data can be turned into clear, actionable visuals. This hands-on experience improved both technical coding skills and an understanding of how AI can assist in environmental data analysis.
