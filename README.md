# Background

Using Brightree, a medical equipment processing system for DME companies, we can run Ad-Hoc reports to find a variety of things.
In this example, an ad-hoc report was run to obtain every invoice sent through our system with applicable information
The list output is a range of 15,000 rows with 20+ columns of information on patients' invoices in a CSV file
After performing some different analytical techniques with the CSV file, we were able to isolate CGM patients only
- CGM: Continuous Glucose Monitor

# Calculating Patient Responsibility using Python
What does this project do?
- This project specifically takes an upload of a CSV file and extracts specific information to create an output of our 'wanted' metrics

Summary:
CSV/EXCEL upload, organization, mining, creation, and output through Python
Creation of CSV output with targeted metrics only
