from nseutility.nseutility import NseUtils

nse = NseUtils()
data = nse.get_live_price('RELIANCE')
print(data)
