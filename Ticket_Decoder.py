#IT Support Ticket Decoder 

ticket_id = 'INC-2026-NET-0042'
ticket_year = ticket_id[4:8]


ticket_type = ticket_id[:3]


ticket_team = ticket_id[9:12]


ticket_number = ticket_id[-4:]

print('IT SUPPORT TICKET DECODER')
print('Original ID:', ticket_id)
print('Ticket type: ', ticket_type)
print('Year: ', ticket_year)
print('Support Team:', ticket_team)
print('Ticket number: ', ticket_number)