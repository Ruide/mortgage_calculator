# mortgage_calculator
This is used for calculation on mortgage

See the example usage in main.py. We can get monthly pay before and after refinance (notice that we also need to pay for maintainence and etc, so multiple this by 1.3 to be sure you have positive cash flow). We can also get discounted to present pay. We can tweak sale_price, fixed_30yrs_rate, down_payment_rate, discount_rate, yrs_before_refinance, refinance_rate by setting them when passing parameters at main.py.

e.g.
> python3 main.py

```
initial fixed 30yrs rate: 0.055. sale price: 2000000. down payment rate: 0.2. discount rate: 0.04.
the total inital loan: 1600000.0
the total inital monthly mortgage payment: 9084.624021552008
years before refinance: 3.0. refinance rate: 0.035.
loan remained before refinance: 1531623.7772012928
the total after refinance monthly mortgage payment: 6877.675208739256
total pay after discounted to present: 1634107.4454846573
```
