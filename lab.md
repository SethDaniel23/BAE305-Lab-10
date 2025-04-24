# BAE305 Lab 10: Python and AI
**Author: Seth Daniel**

**Date: April 23rd, 2025**

## Introduction
In this lab, we created software tools using Python and help from an AI language model to work with water quality data. By using libraries like pandas, matplotlib, and Streamlit, we built easy-to-use programs that can filter, clean, and display real data from the U.S. Geological Survey (USGS). The main goal was to learn how AI can help speed up coding and make complex information easier to understand through interactive web apps.

We used two datasets: one with information about water monitoring stations and another with detailed water quality test results. With Python and AI-generated code, we wrote functions to find site locations, show trends in contaminant levels over time, and build a Streamlit app that lets users explore the data.

This lab helped us better understand data science and environmental engineering, and it showed us useful tools for working with real-world data and building interactive apps.

## Materials
1. A computer running Arduino IDE
2. Chrome

## Assembly Methods
**Part 1:**

The lab started by setting up the coding environment and loading the data files. The station.csv file, which was provided on Canvas, was uploaded to a cloud-based coding platform such as Google Colab or Anaconda. With help from an AI language model, a Python script was created to read the CSV file using the pandas library and pull out important information about each monitoring station.

We looked at the data to find useful columns like the station name, latitude, and longitude. A filtering function was then written to remove duplicate stations and organize the data clearly. After that, we generated a function to create a basic map using either matplotlib or folium, which showed each station as a point on the map based on its location.

The code for this part of the lab was written using GPT-4-turbo (ChatGPT), and the prompts used to generate the code are included in the Test Results section. The final code is shown below.

<div align="center">
<img src="https://github.com/user-attachments/assets/f5d134a1-717f-4653-8f16-a870d522c0fc" alt="1" width="600">
<br/>
<figcaption style="font-size: 16px; text-align: center;"> Figure 1: ChatGPT Python pandas database code for Part 1 of the lab. </figcaption>
</div> 

<br/>


**Part 2:**

   In the second part of the lab, we uploaded and explored the narrowresult.csv file. Using help from an AI language model, we wrote a Python script to read the file and filter it by a specific water quality characteristic—like dissolved oxygen or nitrate. The script grouped the data by monitoring station and date, then created a line plot showing how the contaminant levels changed over time at each station, using different colors for each line.

Once the first plot was working, we updated the script to handle two contaminants at the same time. This required changes to how the data was selected and displayed, so both characteristics could be shown together in the same graph, each with clear labels and different colors.

<div align="center">
<img src="https://github.com/user-attachments/assets/0a842836-0a8f-4369-a520-160d9e89d9b5" alt="2" width="600">
<br/>
<figcaption style="font-size: 16px; text-align: center;"> Figure 2: ChatGPT generated code for narrowresults data from part 2. </figcaption>
</div> 

<br/>

**Part 3:**

 In the final phase, a GitHub repository was set up to host the Streamlit application. The project initiated with a new file, streamlit_app.py, added to the main branch. The app was deployed through the Streamlit portal by connecting it to the GitHub repository. Utilizing a large language model (LLM), Python code was generated to develop an interactive platform where users could upload CSV files, choose a contaminant, and define value and date ranges.

The app was designed to automatically refresh a map displaying station locations with relevant data and a time-series graph that visualized trends in the selected contaminant. Once the app was fully functional, a requirements.txt file was created, listing essential libraries such as pandas, Streamlit, and matplotlib, to facilitate the installation of dependencies during deployment.

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
   
Testing for this section started by checking that the station.csv file was read and parsed correctly. The filtering function was run to make sure that each monitoring site appeared only once and there were no duplicate locations. The map output was reviewed to ensure every station was placed in the correct spot, with proper spacing and no missing coordinates. If there were any errors, like NaNs or repeated station names, the script was updated and retested. Results were compared to the raw CSV file opened in Excel or Google Sheets to verify accuracy.

**Part 2:**

For narrowresult.csv, testing focused on making sure the correct water quality characteristic was selected and plotted over time. The graphs were checked to ensure each station had a separate line, and that the timestamps matched the data values. When the code was updated to handle two parameters, testing involved selecting different combinations of characteristics and ensuring both were plotted clearly with distinct colors and labels. Edge cases, like choosing rare parameters or stations with limited data, were tested to make sure the plot didn’t break or show incorrect results.

**Part 3:**

Testing the Streamlit app involved using the web interface to upload the two CSV files and check the filtering options. The contaminant selector was tested with both common and rare inputs to confirm that the data was handled properly. The value and date sliders were tested to make sure the map and trend graph updated correctly. If extreme or empty ranges resulted in no data, the app’s error-handling was checked. The map was confirmed to update based on user input, and the plot was tested for clarity and responsiveness. Final tests ensured the app loaded correctly from the deployed Streamlit URL and worked consistently across different browsers. The app’s outputs were also checked against the original Python scripts to make sure the data matched.


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
This lab demonstrated the application of AI-generated Python code to analyze and visualize real-world environmental datasets. Using USGS water quality data, the lab explored how tools like pandas and Streamlit can filter, map, and plot trends in water quality by location and contaminant. While the AI-generated code provided a strong starting point, some adjustments were necessary, such as renaming undefined variables and ensuring that the dataset structure was correctly aligned.

One challenge was ensuring the AI’s assumptions matched the actual dataset. For instance, the variable df had to be renamed to usgs_data, and column names had to be double-checked before plotting. Despite these minor issues, the lab highlighted how AI can accelerate the development of data-driven applications when combined with human problem-solving and debugging skills.

Using Streamlit to create an interactive web app made it easy for users to select monitoring stations, choose contaminants, and instantly view time-series plots. This approach shows great potential for creating public-facing tools that make environmental data more accessible and understandable.

## Conclusion:
This lab successfully integrated Python programming, AI-generated code, and real-world USGS water quality data to create an interactive data visualization tool. It demonstrated how AI can significantly streamline tasks like coding visualizations and building user interfaces. However, human oversight is still crucial for debugging and ensuring the results are contextually accurate.

The final Streamlit app allows users to explore trends in water contaminants over time at selected locations, showing how environmental data can be transformed into clear and actionable visuals. This hands-on experience not only improved technical coding skills but also provided insight into how AI can support environmental data analysis.
