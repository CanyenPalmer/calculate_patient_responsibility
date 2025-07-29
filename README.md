# Background

Using Brightree, a medical equipment processing system for DME companies, I can run Ad-Hoc reports to find a variety of things.
In this example, an ad-hoc report was run to obtain every invoice sent through our system with applicable information.
The list output is a range of 15,000 rows with 20+ columns of information on patients' invoices in a CSV file.
After performing some different analytical techniques with the CSV file, I were able to isolate CGM patients only.
This can be performed by only targetting the specific HPCPS codes that are associated with the CGM items
- CGM: Continuous Glucose Monitor

After this was done, I isolated very specific groups of data for future analysis.
This code specifically manipulates the data of the CGM patients to directly reflect the business's intitives.
I then create a function for calculating 'Patient Responsibility' so that it was included in our needed metrics.
This was then output as a new CSV file.

# Calculating Patient Responsibility using Python
What does this project do?
- This project specifically takes an upload of a CSV file and extracts specific information to create an output of our 'wanted' metrics

Summary:
CSV/EXCEL upload, organization, mining, creation, and output through Python
Creation of CSV output with targeted metrics only
