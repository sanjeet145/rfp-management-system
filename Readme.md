# RFP (Request for Proposal) Management system

## Problem statement
Many companies run procurement through Requests for Proposal (RFPs): they define what they want to buy,
email that out to multiple vendors, collect responses (often messy emails and attachments), and then
someone manually compares all the quotes to decide who to award the work to.
This process is:
1. Slow and error-prone
2. Full of unstructured data (emails, PDFs, free-form descriptions)
3. Repetitive: similar RFPs, similar evaluations, similar comparisons


## AI - powered solution
[Diagram](Design/)
1. User and vendor both register to the platform.
2. User loges into the platform
3. User enters their procurement in natural language and clicks on save RFP.
4. LLM takes the user input and then process it. After processing it structures the data saves it into db.
5. RFPs button will list down all the RFPs created by the user. Where user can find the vendors and their responses.
6. According to the order category the system will show the vendors where user can send the request.
7. LLM crafts the email based on the requirements to the vendor.
8. Vendor gets the request over their mail in which same email vendor can reply ( inbound email service ).
9. Vendor can also send into unstructed way including attachments (PDFs, Excel, Docs).
10. LLM get the vendor response and craft it into structure manner to save into DB.
11. LLM also summarize and score the response based on the rules defined.
12. User can now see the response and place the order. 

## Pre-requisites
1. Python
2. Node


[backend](backend/)
Steps:
```python
# create a virtual environment for the packages installation
python -m venv temp 
```
```bash
# activate the venv
temp\Scripts\activate
cd backend 
```
```python
pip install -r requirements.txt
python app.py

```
[frontend](frontend/)
```bash
cd frontend
npm install
npm start
```