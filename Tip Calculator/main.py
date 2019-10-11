# THIS PROGRAM WILL BE A TIP CALCULATOR

name = input("Enter your first name. ")
meal_price = float(input("Enter the price of the meal. "))
state = input("Enter the state you are in. ")
tip_level = input("How was the service? (Excellent, Good, Poor, or Terrible) ")

# This will decide how much will be tipped, based on the service quality
if tip_level == "Excellent" or tip_level == "excellent":
  tip_percentage = 25
elif tip_level == "Good" or tip_level == "good":
  tip_percentage = 15
elif tip_level == "Poor" or tip_level == "poor":
  tip_percentage = 5
elif tip_level == "Terrible" or tip_level == "terrible":
  tip_percentage = 0
else:
  print("ERROR: Invalid tip level input!")

# This will calculate your tax rate based on where you are in the US
# Warning! This section might be extensive, it includes all 50 state stats
# https://taxfoundation.org/sales-tax-rates-2019/ (This is where the stats are from)
if state == "AL" or state == "al" or state == "Alabama" or state == "alabama":
  tax_percentage = 9.14
elif state == "AK" or state == "ak" or state == "Alaska" or state == "alaska":
  tax_percentage = 1.43
elif state == "AZ" or state == "az" or state == "Arizona" or state == "arizona":
  tax_percentage = 8.37
elif state == "CA" or state == "ca" or state == "California" or state == "california":
  tax_percentage = 8.56
elif state == "CO" or state == "co" or state == "Colorado" or state == "colorado":
  tax_percentage = 7.63
elif state == "CT" or state == "ct" or state == "Connecticut" or state == "connecticut":
  tax_percentage = 6.35
elif state == "DE" or state == "de" or state == "Delaware" or state == "delaware":
  tax_percentage = 0.00
elif state == "FL" or state == "fl" or state == "Florida" or state == "florida":
  tax_percentage = 7.05
elif state == "GA" or state == "ga" or state == "Georgia" or state == "georgia":
  tax_percentage = 7.29
elif state == "HI" or state == "hi" or state == "Hawaii" or state == "hawaii":
  tax_percentage = 4.41
elif state == "ID" or state == "id" or state == "Idaho" or state == "idaho":
  tax_percentage = 6.03
elif state == "Il" or state == "il" or state == "Illinois" or state == "illinois":
  tax_percentage = 8.74
elif state == "IN" or state == "in" or state == "Indiana" or state == "indiana":
  tax_percentage = 7.00
elif state == "IA" or state == "ia" or state == "Iowa" or state == "iowa":
  tax_percentage = 6.82
elif state == "KS" or state == "ks" or state == "Kansas" or state == "kansas":
  tax_percentage = 8.67
elif state == "KY" or state == "ky" or state == "Kentucky" or state == "kentucky":
  tax_percentage = 6.00
elif state == "LA" or state == "la" or state == "Louisiana" or state == "louisiana":
  tax_percentage = 9.45
elif state == "ME" or state == "me" or state == "Maine" or state == "maine":
  tax_percentage = 5.50
elif state == "MD" or state == "md" or state == "Maryland" or state == "maryland":
  tax_percentage = 6.00
elif state == "MA" or state == "ma" or state == "Massachussetts" or state == "massachussetts":
  tax_percentage = 6.25
elif state == "MI" or state == "mi" or state == "Michigan" or state == "michigan":
  tax_percentage = 6.00
elif state == "MN" or state == "mn" or state == "Minnesota" or state == "minnesota":
  tax_percentage = 7.43
elif state == "MS" or state == "ms" or state == "Mississippi" or state == "mississippi":
  tax_percentage = 7.07
elif state == "MO" or state == "mo" or state == "Missouri" or state == "missouri":
  tax_percentage = 8.13
elif state == "MT" or state == "mt" or state == "Montana" or state == "montana":
  tax_percentage = 0.00
elif state == "NE" or state == "ne" or state == "Nebraska" or state == "nebraska":
  tax_percentage = 6.85
elif state == "NV" or state == "nv" or state == "Nevada" or state == "nevada":
  tax_percentage = 8.14
elif state == "NH" or state == "nh" or state == "New Hampshire" or state == "new hampshire":
  tax_percentage = 0.00
elif state == "NJ" or state == "nj" or state == "New Jersey" or state == "new jersey":
  tax_percentage = 6.60
elif state == "NM" or state == "nm" or state == "New Mexico" or state == "new mexico":
  tax_percentage = 7.82
elif state == "NY" or state == "ny" or state == "New York" or state == "new york":
  tax_percentage = 8.49
elif state == "NC" or state == "nc" or state == "North Carolina" or state == "north carolina":
  tax_percentage = 6.97
elif state == "ND" or state == "nd" or state == "North Dakota" or state == "north dakota":
  tax_percentage = 6.85
elif state == "OH" or state == "oh" or state == "Ohio" or state == "ohio":
  tax_percentage = 7.17
elif state == "OK" or state == "ok" or state == "Oklahoma" or state == "oklahoma":
  tax_percentage = 8.92
elif state == "OR" or state == "or" or state == "Oregon" or state == "oregon":
  tax_percentage = 0.00
elif state == "PA" or state == "pa" or state == "Pennyslvania" or state == "pennyslvania":
  tax_percentage = 6.34
elif state == "RI" or state == "ri" or state == "Rhode Island" or state == "rhode island":
  tax_percentage = 7.00
elif state == "SC" or state == "sc" or state == "South Carolina" or state == "south carolina":
  tax_percentage = 7.43
elif state == "SD" or state == "sd" or state == "South Dakota" or state == "south dakota":
  tax_percentage = 6.40
elif state == "TN" or state == "tn" or state == "Tennessee" or state == "tennessee":
  tax_percentage = 9.47
elif state == "TX" or state == "tx" or state == "Texas" or state == "texas":
  tax_percentage = 8.19
elif state == "UT" or state == "ut" or state == "Utah" or state == "utah":
  tax_percentage = 6.94
elif state == "VT" or state == "vt" or state == "Vermont" or state == "vermont":
  tax_percentage = 6.18
elif state == "VA" or state == "va" or state == "Virginia" or state == "virginia":
  tax_percentage = 6.35
elif state == "WA" or state == "wa" or state == "Washington" or state == "washington":
  tax_percentage = 9.17
elif state == "WV" or state == "wv" or state == "West Virginia" or state == "west virginia":
  tax_percentage = 6.39
elif state == "WI" or state == "wi" or state == "Wisconsin" or state == "wisconsin":
  tax_percentage = 5.44
elif state == "WY" or state == "wy" or state == "Wyoming" or state == "wyoming":
  tax_percentage = 5.36
elif state == "DC" or state == "dc" or state == "District of Columbia" or state == "district of columbia":
  tax_percentage = 6.00
else:
  print("ERROR: Invalid state input!")

# Here, we calculate the price that will be paid by the customer
tax = (tax_percentage / 100) + 1
subtotal = round((meal_price * tax), 2)
tip = round(((tip_percentage / 100) * meal_price), 2)
full_price = subtotal + tip
rounded_price = round(full_price, 2)

# Here is the output that will print to the console to give the customer a run down of what happened
print("Your meal was: $" + str(meal_price))
print("Because your service was " + tip_level + ", you decided to tip " + str(tip_percentage) + "%")
print("You said you are in " + state + ", so your tax percentage is " + str(tax_percentage) + "%")
print("Your calculated tip was $" + str(tip) + " and your subtotal after tax is $" + str(subtotal))
print("In conlusion, you must pay a total of $" + str(rounded_price))
print("Have a nice day, " + name + "!")