"""
Football Club Finance Calculator
Interactive web app to analyze financial impact of wage-to-revenue ratios
"""

import streamlit as st
import pandas as pd

# ============ PAGE CONFIGURATION ============
st.set_page_config(
    page_title="Football Finance Calculator",
    page_icon="⚽",
    layout="wide"
)

# ============ HEADER ============
st.title("⚽ Football Club Finance Calculator")
st.markdown("**Women's Football Club Financial Analysis Tool**")
st.markdown("Adjust income sources and wage-to-revenue ratio to see financial impact")

st.divider()

# ============ INPUT SECTION ============
st.header("📊 Input Parameters")

# Create two columns for inputs
col_input1, col_input2 = st.columns(2)

with col_input1:
    st.subheader("Income Sources (EUR)")
    
    # All income inputs from your Excel
    gate_receipts = st.number_input(
        "Gate Receipts",
        min_value=0,
        value=50000,
        step=1000
    )
    
    sponsorship = st.number_input(
        "Sponsorship and Advertising",
        min_value=0,
        value=100000,
        step=5000
    )
    
    broadcasting = st.number_input(
        "Broadcasting Rights",
        min_value=0,
        value=30000,
        step=5000
    )
    
    commercial = st.number_input(
        "Commercial Activities",
        min_value=0,
        value=20000,
        step=1000
    )
    
    uefa_solidarity = st.number_input(
        "UEFA Solidarity and Prize Money",
        min_value=0,
        value=10000,
        step=1000
    )
    
    subsidies = st.number_input(
        "Subsidies, Donations, Contributions and Other Grants",
        min_value=0,
        value=5000,
        step=500
    )
    
    other_income = st.number_input(
        "Other Operating Income",
        min_value=0,
        value=5000,
        step=500
    )

with col_input2:
    st.subheader("Expenses (EUR)")
    
    other_operating_expenses = st.number_input(
        "Other Operating Expenses",
        min_value=0,
        value=20000,
        step=1000
    )
    
    player_transfers = st.number_input(
        "Net Expense/(Income) from Player Transfers",
        min_value=0,
        value=50000,
        step=5000,
        help="Positive number = net expense"
    )
    
    non_operating = st.number_input(
        "Net Non-Operating Expense/(Income) - Other",
        min_value=0,
        value=5000,
        step=500,
        help="Positive number = net non-operating expense"
    )
    
    tax_expense = st.number_input(
        "Tax Expense/(Income)",
        min_value=0,
        value=5000,
        step=500,
        help="Positive number = tax expense"
    )
    
    st.markdown("---")
    
    st.subheader("🎯 Wage Ratio Control")
    st.markdown("**Adjust to see financial impact**")
    
    wage_ratio = st.slider(
        "Wage to Revenue Ratio (%)",
        min_value=0,
        max_value=200,
        value=None,
        step=1,
        help="Exceeding 100 % indicates wages are greater than total revenue"
    )

st.divider()

# ============ CALCULATIONS ============
# Calculate total revenue
total_revenue = (
    gate_receipts + 
    sponsorship + 
    broadcasting + 
    commercial + 
    uefa_solidarity + 
    subsidies + 
    other_income
)

# Calculate new employee benefit expenses based on wage ratio
if wage_ratio is not None:
    new_employee_expenses = total_revenue * (wage_ratio / 100)
    
    # Calculate total expenses
    total_operating_expenses_excl_wages = other_operating_expenses
    total_operating_expenses = new_employee_expenses + total_operating_expenses_excl_wages
    
    # Total expenses including non-operating items
    total_expenses = (
        new_employee_expenses + 
        other_operating_expenses + 
        player_transfers + 
        non_operating + 
        tax_expense
    )
    
    # Calculate profit/loss
    profit_loss = total_revenue - total_expenses
    
    # Determine surplus/deficit
    surplus_deficit = "Surplus" if profit_loss > 0 else "Deficit"
    
    # Calculate related ratios
    wage_to_profit_ratio = new_employee_expenses / profit_loss if profit_loss != 0 else float('inf')
    wage_to_total_exp_ratio = new_employee_expenses / total_expenses if total_expenses > 0 else 0

    # ============ RESULTS DISPLAY ============
    st.header("📈 Results")
    
    # Main metrics in columns
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.metric(
            "Total Revenue",
            f"€{total_revenue:,.0f}",
            help="Sum of all income sources"
        )
    
    with metric_col2:
        st.metric(
            "Employee Benefit Expenses",
            f"€{new_employee_expenses:,.0f}",
            help=f"Calculated as {wage_ratio}% of total revenue"
        )
    
    with metric_col3:
        st.metric(
            "Total Expenses",
            f"€{total_expenses:,.0f}",
            help="Employee expenses + other operating expenses + transfers + non-operating + tax"
        )
    
    with metric_col4:
        # Color-coded profit/loss
        delta_color = "normal" if profit_loss >= 0 else "inverse"
        st.metric(
            "Profit/Loss",
            f"€{profit_loss:,.0f}",
            delta=surplus_deficit
        )
    
    # Status indicator
    if surplus_deficit == "Surplus":
        st.success(f"✅ **{surplus_deficit}** - The club is profitable at this wage ratio")
    else:
        st.error(f"⚠️ **{surplus_deficit}** - The club is operating at a loss")
    
    st.divider()
    
    # ============ DETAILED BREAKDOWN ============
    with st.expander("📋 Detailed Financial Breakdown", expanded=False):
        
        detail_col1, detail_col2 = st.columns(2)
        
        with detail_col1:
            st.subheader("Income Breakdown")
            income_data = {
                "Source": [
                    "Gate Receipts",
                    "Sponsorship & Advertising",
                    "Broadcasting Rights",
                    "Commercial Activities",
                    "UEFA Solidarity & Prize Money",
                    "Subsidies & Grants",
                    "Other Operating Income"
                ],
                "Amount (EUR)": [
                    gate_receipts,
                    sponsorship,
                    broadcasting,
                    commercial,
                    uefa_solidarity,
                    subsidies,
                    other_income
                ],
                "% of Total": [
                    f"{(gate_receipts/total_revenue*100):.1f}%" if total_revenue > 0 else "0%",
                    f"{(sponsorship/total_revenue*100):.1f}%" if total_revenue > 0 else "0%",
                    f"{(broadcasting/total_revenue*100):.1f}%" if total_revenue > 0 else "0%",
                    f"{(commercial/total_revenue*100):.1f}%" if total_revenue > 0 else "0%",
                    f"{(uefa_solidarity/total_revenue*100):.1f}%" if total_revenue > 0 else "0%",
                    f"{(subsidies/total_revenue*100):.1f}%" if total_revenue > 0 else "0%",
                    f"{(other_income/total_revenue*100):.1f}%" if total_revenue > 0 else "0%"
                ]
            }
            st.dataframe(income_data, hide_index=True, use_container_width=True)
        
        with detail_col2:
            st.subheader("Expense Breakdown")
            expense_data = {
                "Category": [
                    "Employee Benefits",
                    "Other Operating Expenses",
                    "Player Transfers (Net)",
                    "Non-Operating Items",
                    "Tax"
                ],
                "Amount (EUR)": [
                    new_employee_expenses,
                    other_operating_expenses,
                    player_transfers,
                    non_operating,
                    tax_expense
                ],
                "% of Total": [
                    f"{(new_employee_expenses/total_expenses*100):.1f}%" if total_expenses > 0 else "0%",
                    f"{(other_operating_expenses/total_expenses*100):.1f}%" if total_expenses > 0 else "0%",
                    f"{(player_transfers/total_expenses*100):.1f}%" if total_expenses > 0 else "0%",
                    f"{(non_operating/total_expenses*100):.1f}%" if total_expenses > 0 else "0%",
                    f"{(tax_expense/total_expenses*100):.1f}%" if total_expenses > 0 else "0%"
                ]
            }
            st.dataframe(expense_data, hide_index=True, use_container_width=True)
    
    # ============ KEY RATIOS ============
    with st.expander("📊 Key Financial Ratios", expanded=False):
        ratio_col1, ratio_col2, ratio_col3 = st.columns(3)
        
        with ratio_col1:
            st.metric(
                "Wage to Revenue Ratio",
                f"{wage_ratio}%",
                help="Employee expenses as % of total revenue"
            )
        
        with ratio_col2:
            if profit_loss != 0 and wage_to_profit_ratio != float('inf'):
                st.metric(
                    "Wage to Profit Ratio",
                    f"{wage_to_profit_ratio:.2f}",
                    help="Employee expenses divided by profit"
                )
            else:
                st.metric(
                    "Wage to Profit Ratio",
                    "N/A",
                    help="Not applicable when profit is zero"
                )
        
        with ratio_col3:
            st.metric(
                "Wage to Total Expenditure Ratio",
                f"{wage_to_total_exp_ratio:.2%}",
                help="Employee expenses as % of total expenses"
            )

else:
    # No wage ratio selected yet
    st.info("👈 **Please set the Wage to Revenue Ratio slider** to see calculated results")
    
    # Show total revenue even without wage ratio
    st.metric("Total Revenue (from inputs)", f"€{total_revenue:,.0f}")

# ============ FOOTER ============
st.divider()
st.caption("Women's Football Club Finance Calculator | Built with Streamlit")
