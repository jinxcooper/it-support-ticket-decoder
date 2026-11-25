# IT Support Ticket Decoder

A beginner Python project inspired by my experience in IT support.

This script uses string slicing to extract information from a ticket ID and display a readable summary.

## What it extracts

- Ticket type
- Year
- Support team
- Ticket number, including leading zeros

## What I practiced

- Start and stop indices
- Slices with omitted boundaries
- Negative indices
- Variables and labeled console output

## How to run

With Python 3 installed, open a terminal in the project folder and run:

```bash
python ticket_decoder.py
```

## Example output

```text
IT SUPPORT TICKET DECODER
Original ID: INC-2026-NET-0042
Ticket type: INC
Year: 2026
Support Team: NET
Ticket number: 0042
```

## Current scope

This version expects ticket IDs in the fixed format
`XXX-YYYY-XXX-NNNN`. It does not yet validate the input.
