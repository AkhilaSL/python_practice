def main():
    income=float(input("Enter your income:"))
    expenses={}
    while True:
        expense_names=input("Enter the expense name (or done if it is over):")
        if expense_names.lower()=="done":
            break
        expense_values=float(input("Enter the expenses for "+ expense_names+":"))
        expenses[expense_names]=expense_values

        total_expenses=sum(expenses.values())
        surplus_or_deficit=income-total_expenses
    print("\nExpense Summary")
    print("****************************")
    print("Budget breakdown")
    for name,values in expenses.items():
        print(f"{name}:{values}")
    print("Total expense :",round(total_expenses,2))
    print("Surplus or deficit : ",round(surplus_or_deficit,2))

if __name__=="__main__":
    main()

        