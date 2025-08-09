square_meters = float(input())

price_per_sqm = 7.61
initial_total_price = square_meters * price_per_sqm
discount = initial_total_price * 0.18
final_price = initial_total_price - discount

print(f"The final price is: {final_price:.2f} USD.")
print(f"The discount is: {discount:.2f} USD.")
