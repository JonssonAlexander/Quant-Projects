# Given data for AAPL DCF valuation
eps_without_nri = 74.84*10**9/1821936744 - 3 #Utdelning  # EPS without NRI
discount_rate = 6.11 / 100  # WACC
growth_rate_growth_stage = 15 / 100  # Growth rate during the growth stage, capped at 20%
growth_rate_terminal_stage = 8 / 100  # Growth rate during the terminal stage
years_growth_stage = 10  # Number of years in growth stage
years_terminal_stage = 10  # Number of years in terminal stage

# Growth Stage Value Calculation
growth_stage_value = sum([eps_without_nri * ((1 + growth_rate_growth_stage) ** t) / ((1 + discount_rate) ** t) 
                          for t in range(1, years_growth_stage + 1)])

# Terminal Stage Value Calculation
terminal_value_multiplier = (1 + growth_rate_growth_stage) ** years_growth_stage / (1 + discount_rate) ** years_growth_stage
terminal_stage_value = sum([eps_without_nri * terminal_value_multiplier * ((1 + growth_rate_terminal_stage) ** t) / ((1 + discount_rate) ** t) 
                            for t in range(1, years_terminal_stage + 1)])

# Total Intrinsic Value Calculation
total_intrinsic_value = growth_stage_value + terminal_stage_value

print('growth_stage_value',growth_stage_value)
print('terminal_stage_value', terminal_stage_value)
print('total_intrinsic_value',total_intrinsic_value)