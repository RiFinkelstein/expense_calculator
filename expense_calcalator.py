import os


class Budget(object):
    def __init__(self):
        os.system('cls')
        while True:
            try:
                self.budget = float(input("how much is your budget\n"))
                break
            except ValueError:
                print("Error: Please enter a number")
        self.spending = self.budget * 0.5
        self.expenses = {} 
        self.main()


    def main(self):
        os.system('cls')
        print("this calculator follows the 50-20-30 budget rule.\n")
        print("yourtotal budget is $", '{:.2f}'.format(self.budget))
        main_option = int(input(
            '\n what do you want to do? \n 1) View overall budget \n2)View spending budget?\n3) Add expense\n4) Exit\n'))
        if main_option == 1:
            self.overall_budget()
        elif main_option == 2:
            self.spending_budget()
        elif main_option == 3:
            self.add_expense()
        elif main_option == 4:
            quit()
        else:
            self.new_budget()

    def overall_budget(self):
        os.system('cls')
        option = int(input("how much do you want to save? 1)2% 2)10% 2)30%"))
        if option == 1:
            self.saving = 0.2
        elif option == 2:
            self.saving = 0.1
        elif option == 3:
            self.saving = 0.3
        else:
            print("error. please select only 1 or 2!")
        self.final_saving = self.budget*self.saving
        self.extra = self.budget-self.final_saving-self.spending
        print("\nSpending: $", self.spending, '\nTo save: $',
              self.final_saving, '\nExtra: $', self.extra)
        os.system('pause')
        self.main()

    def spending_budget(self):
        os.system('cls')
        print('Spending Budget: $', '{:.2f}'. format(self.spending))
        rent = float(input('\n how much rent do you pay monthly?\n'))
        bills = float(input('\n how much are your monthly bills?\n'))
        groceries = self.spending-rent-bills
        print('\nEXPENSES: \n Rent: $', '{:.2f}'.format(rent), '\nbills:$', '{:.2f}'.format(
            bills), '\nGroceries''{:.2f}'.format(groceries),)
        os.system('pause')
        self.main()
    
    def add_expense(self):
        os.system('cls')
        print("Add an expense:")
        category = input("Category: ")
        amount = float(input("Amount: "))
        self.expenses[category] = self.expenses.get(category, 0) + amount
        print(category, "expense of $", '{:.2f}'.format(amount), "added.")
        os.system('pause')
        self.main()

    def new_budget(self):
        os.system('cls')
        option = input("Do you want to enter a new budget? (y/n)")
        if option.lower() == 'y':
            self.__init__()
        else:
            quit()


Budget()
