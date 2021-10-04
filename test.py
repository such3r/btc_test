# Based on https://www.codearmo.com/python-tutorial/crypto-currency-options

from deribit_options_data import DeribitOptionsData
from bs_option import BsOption

if __name__ == "__main__":
	optObj = DeribitOptionsData('BTC')
	opts = optObj.options
	print(opts.columns)
	
	exp = optObj.expiries()
	print(exp)
	
	calls = optObj.get_side_exp('Call', exp[-2])
	print(calls[['strike', 'dollar_bid', 'dollar_mid', 'dollar_ask', 'time']].head(20))
	
	calls = calls[calls.dollar_mid >0]
	calls['Bs_price'] = BsOption(calls.underlying_price, calls.strike, calls.time, calls.interest_rate, 0.8303).price('C')
	vols_a = []
	
	for row in calls.itertuples():
		sigma = optObj.option_info(row.instrument_name)['result']['ask_iv'] / 100
		V = BsOption(row.underlying_price, row.strike , row.time, 0, float(sigma)).price('C')
		vols_a.append(sigma)
		print('#'*50)
		print(f'Calculated BS {V}')
		print(f'From api call {row.dollar_ask}')
		print('STRIKE = ', row.strike)
		
	calls['implied_vol_ask'] = vols_a
