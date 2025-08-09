import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("=" * 60)
print("NUMPY STATISTICS VISUALIZATION TASKS 1-10")
print("=" * 60)

# Set up the plotting
plt.style.use('default')
fig = plt.figure(figsize=(20, 24))

# Task 1: Student Exam Scores Analysis
print("\n1. Student Exam Scores Analysis:")
np.random.seed(42)
scores = np.random.normal(70, 10, 100)

# Calculate z-scores
z_scores = (scores - np.mean(scores)) / np.std(scores)
outliers = np.abs(z_scores) > 2
outlier_count = np.sum(outliers)

print(f"Mean score: {np.mean(scores):.2f}")
print(f"Std deviation: {np.std(scores):.2f}")
print(f"Number of outliers (|z| > 2): {outlier_count}")
print(f"Outlier scores: {scores[outliers]}")

# Plot 1: Dot plot
plt.subplot(5, 2, 1)
jitter = np.random.normal(0, 0.1, len(scores))
plt.scatter(scores, jitter, alpha=0.6, s=30)
plt.title('Exam Scores Dot Plot')
plt.xlabel('Score')
plt.ylabel('Jitter')

# Plot 2: Histogram
plt.subplot(5, 2, 2)
plt.hist(scores, bins=15, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Exam Scores Distribution')
plt.xlabel('Score')
plt.ylabel('Frequency')

# Task 2: Fruit Sales Distribution
print("\n" + "="*50)
print("2. Fruit Sales Distribution:")
np.random.seed(42)
fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
sales = np.random.randint(50, 200, size=5)
explode = [0.1 if s == max(sales) else 0 for s in sales]

print(f"Sales data: {dict(zip(fruits, sales))}")
print(f"Highest selling fruit: {fruits[np.argmax(sales)]} ({max(sales)} units)")

plt.subplot(5, 2, 3)
plt.pie(sales, labels=fruits, explode=explode, autopct='%1.1f%%', startangle=90)
plt.title('Fruit Sales Distribution')

# Task 3: Temperature vs Ice Cream Sales
print("\n" + "="*50)
print("3. Temperature vs Ice Cream Sales:")
np.random.seed(42)
temp = np.linspace(20, 35, 30)
ice_cream_sales = 50 + 2 * temp + np.random.normal(0, 5, 30)

# Calculate correlation
correlation = np.corrcoef(temp, ice_cream_sales)[0, 1]
# Fit regression line
slope, intercept = np.polyfit(temp, ice_cream_sales, 1)

print(f"Pearson correlation: {correlation:.3f}")
print(f"Regression equation: Sales = {slope:.2f} * Temp + {intercept:.2f}")

plt.subplot(5, 2, 4)
plt.scatter(temp, ice_cream_sales, alpha=0.7)
plt.plot(temp, slope * temp + intercept, 'r-', linewidth=2, label=f'R = {correlation:.3f}')
plt.title('Temperature vs Ice Cream Sales')
plt.xlabel('Temperature (°C)')
plt.ylabel('Sales ($)')
plt.legend()

# Task 4: Income Distribution Across Professions
print("\n" + "="*50)
print("4. Income Distribution by Profession:")
np.random.seed(42)
engineers = np.random.exponential(80000, 100) + 40000
teachers = np.random.normal(55000, 8000, 100)
artists = np.random.lognormal(10.5, 0.4, 100)

income_data = [engineers, teachers, artists]
professions = ['Engineers', 'Teachers', 'Artists']

# Calculate statistics
for i, (prof, data) in enumerate(zip(professions, income_data)):
    median = np.median(data)
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    print(f"{prof} - Median: ${median:,.0f}, IQR: ${iqr:,.0f}")

plt.subplot(5, 2, 5)
plt.boxplot(income_data, labels=professions)
plt.title('Income Distribution by Profession')
plt.ylabel('Income ($)')
plt.xticks(rotation=45)

# Task 5: Study Hours vs Exam Scores Regression
print("\n" + "="*50)
print("5. Study Hours vs Exam Scores:")
np.random.seed(42)
hours = np.random.uniform(1, 10, 50)
exam_scores = 30 + 7 * hours + np.random.normal(0, 5, 50)

# Linear regression
slope, intercept = np.polyfit(hours, exam_scores, 1)
r_squared = np.corrcoef(hours, exam_scores)[0, 1] ** 2

print(f"Regression: Score = {slope:.2f} * Hours + {intercept:.2f}")
print(f"R-squared: {r_squared:.3f}")

plt.subplot(5, 2, 6)
plt.scatter(hours, exam_scores, alpha=0.7)
plt.plot(hours, slope * hours + intercept, 'r-', linewidth=2, label=f'R² = {r_squared:.3f}')
plt.title('Study Hours vs Exam Scores')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.legend()

# Task 6: Website Traffic Analysis
print("\n" + "="*50)
print("6. Website Traffic Analysis:")
np.random.seed(42)
traffic = np.random.poisson(lam=50, size=744)  # 31 days * 24 hours

# Calculate z-scores
traffic_mean = np.mean(traffic)
traffic_std = np.std(traffic)
traffic_z = (traffic - traffic_mean) / traffic_std
anomalies = np.abs(traffic_z) > 3

print(f"Mean traffic: {traffic_mean:.1f} visits/hour")
print(f"Std deviation: {traffic_std:.1f}")
print(f"Number of anomalies (|z| > 3): {np.sum(anomalies)}")
print(f"Peak traffic hours: {traffic[anomalies]}")

plt.subplot(5, 2, 7)
plt.hist(traffic, bins=20, alpha=0.7, color='lightgreen', edgecolor='black')
plt.title('Website Traffic Distribution')
plt.xlabel('Visits per Hour')
plt.ylabel('Frequency')

# Task 7: Advertising Spend vs Revenue
print("\n" + "="*50)
print("7. Advertising Spend vs Revenue:")
np.random.seed(42)
spend = np.linspace(1000, 10000, 12)
revenue = 5000 + 2.5 * spend + np.random.normal(0, 1000, 12)

# Calculate correlation
r_value, p_value = stats.pearsonr(spend, revenue)

print(f"Pearson R: {r_value:.3f}")
print(f"P-value: {p_value:.3f}")

plt.subplot(5, 2, 8)
plt.scatter(spend, revenue, alpha=0.7, s=60)
plt.title(f'Ad Spend vs Revenue (R = {r_value:.3f})')
plt.xlabel('Ad Spend ($)')
plt.ylabel('Revenue ($)')

# Task 8: Movie Genre Popularity
print("\n" + "="*50)
print("8. Movie Genre Popularity:")
np.random.seed(42)
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance']
tickets = np.random.randint(5000, 30000, size=6)
min_idx = np.argmin(tickets)
explode = [0.1 if i == min_idx else 0 for i in range(len(genres))]

print(f"Ticket sales: {dict(zip(genres, tickets))}")
print(f"Least popular: {genres[min_idx]} ({tickets[min_idx]} tickets)")

plt.subplot(5, 2, 9)
plt.pie(tickets, labels=genres, explode=explode, autopct='%1.1f%%', startangle=90)
plt.title('Movie Genre Popularity')

# Task 9: Housing Price Analysis
print("\n" + "="*50)
print("9. Housing Price Analysis:")
np.random.seed(42)
suburban = np.random.normal(350000, 50000, 100)
urban = np.random.lognormal(12.8, 0.3, 100)
rural = np.random.exponential(250000, 100) + 150000

price_data = [suburban, urban, rural]
neighborhoods = ['Suburban', 'Urban', 'Rural']

# Calculate statistics
for i, (neighborhood, data) in enumerate(zip(neighborhoods, price_data)):
    median = np.median(data)
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    print(f"{neighborhood} - Median: ${median:,.0f}, IQR: ${iqr:,.0f}")

plt.subplot(5, 2, 10)
plt.boxplot(price_data, labels=neighborhoods)
plt.title('Housing Prices by Neighborhood')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)

# Task 10: Athlete Performance Analysis (separate figure due to space)
print("\n" + "="*50)
print("10. Athlete Performance: Age vs Speed:")
np.random.seed(42)
age = np.random.randint(18, 40, 40)
speed = 10 - 0.15 * age + np.random.normal(0, 0.5, 40)

# Calculate correlation
age_speed_corr = np.corrcoef(age, speed)[0, 1]
slope_age, intercept_age = np.polyfit(age, speed, 1)

print(f"Correlation between age and speed: {age_speed_corr:.3f}")
print(f"Regression: Speed = {slope_age:.3f} * Age + {intercept_age:.2f}")

# Create separate figure for task 10
plt.tight_layout()
plt.show()

# Plot task 10 separately
plt.figure(figsize=(10, 6))
plt.scatter(age, speed, alpha=0.7, s=60)
plt.plot(age, slope_age * age + intercept_age, 'r-', linewidth=2, 
         label=f'R = {age_speed_corr:.3f}')
plt.title('Athlete Age vs Sprint Speed')
plt.xlabel('Age (years)')
plt.ylabel('Speed (m/s)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

