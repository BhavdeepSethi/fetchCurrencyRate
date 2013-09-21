fetchCurrencyRate
=================

Script which fetches the exchange rates from Financial Times and mails the result to the given email id.

Script Usage: 

`python currencyList.py toEmail currencyFrom(csv) currencyTo(csv)`

Examples:  

- To get notification about conversion rate of US Dollar to Indian Rupee. This also the defaul implementaion: 
`python currencyList.py "sethibhavdeep@gmail.com" "USD" "INR"`
`python currencyList.py "sethibhavdeep@gmail.com"`

- To get notification about conversion rate of US Dollar, UK Pound and Euro to Indian Rupee: 
`python currencyList.py "sethibhavdeep@gmail.com" "USD,GBP,EUR" "INR"`

- To get notification about conversion rate of US Dollar to Canadian Dollar and Indian Rupee: 
`python currencyList.py "sethibhavdeep@gmail.com" "USD" "CAD,INR"`


NOTE: The quotes around the arguments are optional. 

---

Here is the list of supported currencies:

- GBP UK Pound
- ARS Argentinian Nuevo Peso
- AUD Australian Dollar
- BHD Bahraini Dinar
- BRL Brazilian Real
- BND Brunei Dollar
- CAD Canadian Dollar
- CLP Chilean Peso
- CNY Chinese Yuan Renminbi
- CZK Czech Koruna
- DKK Danish Krone
- EUR Euro
- FJD Fiji Dollar
- XPF French Pacific Franc
- HKD Hong Kong Dollar
- HUF Hungarian Forint
- INR Indian Rupee
- IDR Indonesian Rupiah
- ILS Israeli Shekel
- JPY Japanese Yen
- KWD Kuwaiti Dinar
- MYR Malaysian Ringgit
- MXN Mexican New Peso
- MAD Moroccan Dirham
- NZD New Zealand Dollar
- NOK Norwegian Krone
- OMR Omani Rial
- PKR Pakistani Rupee
- PGK Papua New Guinean Kina
- PEN Peruvian New Sol
- PHP Philippine Peso
- PLN Polish New Zloty
- KRW Republic of Korean Won
- WST Samoan Tala
- SAR Saudi Riyal
- SCR Seychelles Rupee
- SGD Singapore Dollar
- SBD Solomon Islands Dollar
- ZAR South African Rand
- LKR Sri Lankan Rupee
- SEK Swedish Krona
- CHF Swiss Franc
- TWD Taiwan Dollar
- THB Thai Baht
- TOP Tongan Pa'anga
- TRY Turkish Lira
- AED UAE Dirham
- USD US Dollar
- VUV Vanuatu Vatu
- VND Vietnamese Dong