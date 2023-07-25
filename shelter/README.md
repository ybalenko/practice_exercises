### Project overview

Create a solution for a local shelter to manage their donation inventory. This shelter is in need to record and track the inflow and outflow of donations, and to generate reports about their donation management.

Here are the core functionalities your solution should address:

1. Donation Registration: A feature that allows the shelter staff to record details of the donations, 
such as the donor's name, type of donation (money, food, clothing, etc.), quantity or amount donated, and the date of the donation.

2. Donation Distribution: A feature to log when and how much of the donations are distributed, capturing the type of donation, quantity or amount distributed, and the date of distribution.
<!-- Since I do not have a strict format, I decided to aggregate by date and within it by type -->

3. Donation Reports: Your solution should have the capacity to generate two types of reports:

(1) An inventory report displaying the current status of donations, grouped by type. 
<!-- Since I do not have a strict format, an inventory report shows type and its quantity -->

(2) A donator report, summarizing the total contributions received from each donor.
<!-- Since I do not have a strict format, a donator report shows total donations per a donator -->

### Instructions

To run a program, go to a directory and execute:

```
python shelter.py
```


To run unit tests, go to a directory and execute:

```
python shelter_tests.py
``````
