def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    discounted_drinks_cost = drinks_cost * 0.7
    pretax_total = discounted_drinks_cost + meal_cost
    posttax_total = pretax_total * 1.15
    return posttax_total


