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