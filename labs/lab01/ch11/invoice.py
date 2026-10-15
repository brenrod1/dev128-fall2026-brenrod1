# Starting file for Lab 1 Chapter 11 invoice.py program
# Bren Rodriguez, 10/15/26 DEV 128 Lab Activity 1
# AI-assisted: I used Claude to understand date vs datetime objects, try/except validation, and reading tracebacks


from datetime import datetime, date, timedelta

def get_invoice_date():
    # while True explains that the loop will continue until a valid invoice date is entered
    while True:
        try:
            invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")

            invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%Y").date()
            # comparing to today's date, if the invoice date is in the future, it is considered invalid and the user will be prompted again
            if invoice_date > date.today():
                print("Invoice date cannot be in the future.")
                print()
            else: 
                return invoice_date
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY.")
            print()

def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
