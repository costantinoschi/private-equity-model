import numpy as np
import pandas as pd

def private_equity_model(
    revenue_growth, ebitda_margin, depreciation_rate, capex_ratio,
    nwc_ratio, tax_rate, discount_rate, exit_multiple, debt_ratio,
    interest_rate, repayment_schedule, years=5, entry_multiple=6, 
    sponsor_equity=0.5, fixed_costs_ratio=0.2
):
    # Initial Assumptions
    revenue = 100  # Starting revenue in millions
    debt = revenue * debt_ratio
    equity_value = revenue * entry_multiple
    depreciation = revenue * depreciation_rate
    capex = revenue * capex_ratio
    nwc_change = revenue * nwc_ratio
    sponsor_investment = equity_value * sponsor_equity
    
    free_cash_flows = []
    debt_balances = [debt]
    interest_expenses = []
    
    for year in range(1, years + 1):
        revenue *= (1 + revenue_growth)
        fixed_costs = revenue * fixed_costs_ratio
        variable_costs = revenue * (1 - ebitda_margin)
        ebitda = revenue - fixed_costs - variable_costs
        depreciation = revenue * depreciation_rate
        ebit = ebitda - depreciation
        interest_expense = debt * interest_rate
        tax = (ebit - interest_expense) * tax_rate
        net_income = ebit - interest_expense - tax
        free_cash_flow = net_income + depreciation - capex - nwc_change
        free_cash_flows.append(free_cash_flow)
        
        # Debt Repayment
        if year in repayment_schedule:
            debt -= repayment_schedule[year]
        
        interest_expenses.append(interest_expense)
        debt_balances.append(debt)
    
    # Discounted Cash Flow (DCF) Calculation
    discount_factors = [(1 / (1 + discount_rate) ** i) for i in range(1, years + 1)]
    npv = sum([cf * df for cf, df in zip(free_cash_flows, discount_factors)])
    terminal_value = (free_cash_flows[-1] * (1 + revenue_growth)) / (discount_rate - revenue_growth)
    terminal_value_discounted = terminal_value / ((1 + discount_rate) ** years)
    enterprise_value = npv + terminal_value_discounted
    equity_value = enterprise_value - debt
    
    # LBO Return Metrics
    moic = equity_value / sponsor_investment  # Multiple on Invested Capital
    irr = ((equity_value / sponsor_investment) ** (1 / years)) - 1  # Internal Rate of Return
    
    # Sensitivity Analysis (Operating Leverage & Exit Multiples)
    sensitivity_results = {}
    for fixed_cost_scenario in [fixed_costs_ratio - 0.05, fixed_costs_ratio, fixed_costs_ratio + 0.05]:
        for exit_scenario in [exit_multiple - 1, exit_multiple, exit_multiple + 1]:
            adjusted_fixed_costs = revenue * fixed_cost_scenario
            adjusted_ebitda = revenue - adjusted_fixed_costs - variable_costs
            adjusted_ebit = adjusted_ebitda - depreciation
            adjusted_net_income = adjusted_ebit - interest_expense - tax
            adjusted_free_cash_flow = adjusted_net_income + depreciation - capex - nwc_change
            adj_terminal_value = (adjusted_free_cash_flow * (1 + revenue_growth)) / (discount_rate - revenue_growth)
            adj_terminal_value_discounted = adj_terminal_value / ((1 + discount_rate) ** years)
            adj_enterprise_value = npv + adj_terminal_value_discounted
            adj_equity_value = adj_enterprise_value - debt
            adj_moic = adj_equity_value / sponsor_investment
            adj_irr = ((adj_equity_value / sponsor_investment) ** (1 / years)) - 1
            
            sensitivity_results[f'Fixed Cost {fixed_cost_scenario:.2%}, Exit {exit_scenario}x'] = {
                'Enterprise Value': round(adj_enterprise_value, 2),
                'Equity Value': round(adj_equity_value, 2),
                'MOIC': round(adj_moic, 2),
                'IRR': round(adj_irr * 100, 2)
            }
    
    return {
        'Enterprise Value': round(enterprise_value, 2),
        'Equity Value': round(equity_value, 2),
        'NPV of Cash Flows': round(npv, 2),
        'Terminal Value (Discounted)': round(terminal_value_discounted, 2),
        'Annual Free Cash Flows': [round(cf, 2) for cf in free_cash_flows],
        'Interest Expenses': [round(ie, 2) for ie in interest_expenses],
        'Debt Balances': [round(db, 2) for db in debt_balances],
        'MOIC': round(moic, 2),
        'IRR': round(irr * 100, 2),  # Converted to percentage
        'Sensitivity Analysis': sensitivity_results
    }

# Example Usage
repayment_schedule = {1: 10, 3: 15, 5: 20}  # Example debt repayment structure
model_results = private_equity_model(
    revenue_growth=0.05, ebitda_margin=0.3, depreciation_rate=0.05,
    capex_ratio=0.08, nwc_ratio=0.02, tax_rate=0.25, discount_rate=0.1,
    exit_multiple=8, debt_ratio=0.4, interest_rate=0.05,
    repayment_schedule=repayment_schedule, entry_multiple=6, sponsor_equity=0.5,
    fixed_costs_ratio=0.2
)
print(model_results)
