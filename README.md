```bash
Index(['volume', 'underlying_price', 'underlying_index', 'quote_currency',
       'price_change', 'open_interest', 'mid_price', 'mark_price', 'low',
       'last', 'interest_rate', 'instrument_name', 'high',
       'estimated_delivery_price', 'creation_timestamp', 'bid_price',
       'base_currency', 'ask_price', 'expiry', 'strike', 'type', 'dollar_bid',
       'dollar_ask', 'dollar_mid', 'time'],
      dtype='object')
[numpy.datetime64('2021-10-05T00:00:00.000000000'), numpy.datetime64('2021-10-06T00:00:00.000000000'), numpy.datetime64('2021-10-08T00:00:00.000000000'), numpy.datetime64('2021-10-15T00:00:00.000000000'), numpy.datetime64('2021-10-22T00:00:00.000000000'), numpy.datetime64('2021-10-29T00:00:00.000000000'), numpy.datetime64('2021-11-26T00:00:00.000000000'), numpy.datetime64('2021-12-31T00:00:00.000000000'), numpy.datetime64('2022-03-25T00:00:00.000000000'), numpy.datetime64('2022-06-24T00:00:00.000000000')]
     strike    dollar_bid    dollar_mid    dollar_ask      time
63    45000   5241.233670  15760.960965  26280.688260  0.468493
86   200000     24.839970    471.959430    919.078890  0.468493
89    25000     24.839970  17686.058640  35347.277310  0.468493
128   30000           NaN           NaN  32639.720580  0.468493
131   55000     49.679940   7725.230670  15400.781400  0.468493
177   50000     24.839975   5862.234100  11699.628225  0.468493
181   60000   8445.589800   8532.529695   8619.469590  0.468493
207   40000  15947.260740  16158.400485  16369.540230  0.468493
215  150000   1540.078140   1564.918110   1589.758080  0.468493
232   35000  14680.425225  18518.201362  22355.977500  0.468493
233  100000   2483.997000   2707.556730   2931.116460  0.468493
##################################################
Calculated BS 26230.809376051733
From api call 26280.688260000003
STRIKE =  45000
##################################################
Calculated BS 906.667344691351
From api call 919.07889
STRIKE =  200000
##################################################
Calculated BS 35311.29379891059
From api call 35347.277310000005
STRIKE =  25000
##################################################
Calculated BS 15361.009965591105
From api call 15400.7814
STRIKE =  55000
##################################################
Calculated BS 11672.115590076533
From api call 11699.628224999999
STRIKE =  50000
##################################################
Calculated BS 8589.575495688017
From api call 8619.46959
STRIKE =  60000
##################################################
Calculated BS 16345.941535447128
From api call 16369.540230000002
STRIKE =  40000
##################################################
Calculated BS 1571.9340387783159
From api call 1589.75808
STRIKE =  150000
##################################################
Calculated BS 22327.198933994194
From api call 22355.9775
STRIKE =  35000
##################################################
Calculated BS 2907.755443602391
From api call 2931.11646
STRIKE =  100000
```
