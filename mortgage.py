class Mortgage:
    # by default: 2 million, 20% down_payment_rate, %5.5 fixed_30yrs_rate, %4 discount_rate, 3 yrs_before_refinance, 3.5% refinance_rate
    def print_mortgage(sale_price = 2*(10**6),fixed_yrs = 30.0,fixed_30yrs_rate=0.055, down_payment_rate=0.2,discount_rate = 0.04, yrs_before_refinance = 3.0, refinance_rate = 0.035):
        r=fixed_30yrs_rate/12.0
        P=sale_price*(1-down_payment_rate)
        n=30*12
        '''
        M: the total monthly mortgage payment
        P: the principal loan amount
        r: your monthly interest rate -> Lenders provide you an annual rate so you’ll need to divide that figure by 12 (the number of months in a year) to get the monthly rate. If your interest rate is 5 percent, your monthly rate would be 0.004167 (0.05/12=0.004167).
        n: number of payments over the loan’s lifetime -> Multiply the number of years in your loan term by 12 (the number of months in a year) to get the number of payments for your loan. For example, a 30-year fixed mortgage would have 360 payments (30x12=360).
        M = P*(r*(1+r)**n)/((1+r)**n-1)
        '''
        M = P*r*((1+r)**n)/((1+r)**n-1)
        print('initial fixed 30yrs rate',''.join([str(fixed_30yrs_rate),'.']), 'sale price', ''.join([str(sale_price),'.']),'down payment rate', ''.join([str(down_payment_rate),'.']), 'discount rate', ''.join([str(discount_rate),'.']))
        print('the total inital loan', P)
        print('the total inital monthly mortgage payment:',M)
        pay_per_year=12.0*M
        total_pay_after_discounted_to_present=0.0
        ratio_of_before_refinance_and_fixed_yrs = yrs_before_refinance/fixed_yrs
    
        for i in range(int(fixed_yrs*ratio_of_before_refinance_and_fixed_yrs)):
            total_pay_after_discounted_to_present+= pay_per_year/((1.0+discount_rate)**i)
       
        loan_balance_remained = sale_price*(1-down_payment_rate)
    
        total_interest_paid_before_refinance = 0
        for i in range(int(n*ratio_of_before_refinance_and_fixed_yrs)):
          interest_paid_per_month = r*loan_balance_remained
          total_interest_paid_before_refinance += interest_paid_per_month
          loan_balance_remained = loan_balance_remained - (M - interest_paid_per_month)
        
        total_pay_after_discounted_to_present_before_refinance = 0
        for i in range(int(fixed_yrs*ratio_of_before_refinance_and_fixed_yrs)):
            total_pay_after_discounted_to_present_before_refinance+= pay_per_year/((1.0+discount_rate)**i)
        
        print('years before refinance',''.join([str(yrs_before_refinance),'.']), 'refinance rate', ''.join([str(refinance_rate),'.']))
        print('loan remained before refinance', loan_balance_remained)
        P = loan_balance_remained
        r = refinance_rate/12.0
        after_refinance_Monthly_morgate_pay = P*r*((1+r)**n)/((1+r)**n-1)
        print('the total after refinance monthly mortgage payment:',after_refinance_Monthly_morgate_pay)
    
        pay_per_year_after_refinance = 12*after_refinance_Monthly_morgate_pay
        for i in range(int(fixed_yrs*ratio_of_before_refinance_and_fixed_yrs), int(fixed_yrs*ratio_of_before_refinance_and_fixed_yrs+fixed_yrs)):
            total_pay_after_discounted_to_present += pay_per_year_after_refinance/((1.0+discount_rate)**i)
    
        print('total pay after discounted to present:',total_pay_after_discounted_to_present)
