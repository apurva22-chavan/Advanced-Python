import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('data of gurugram real Estate.csv')
print(df)
print(df.head())
print(df.shape)
print(df.info())

df.columns=df.columns.str.strip().str.lower().str.replace(' ','_')
print(df.columns)

df['price']=df['price'].astype(str).str.replace(',','').astype(int)
df['area']=df['area'].astype(str).str.replace(',','').astype(int)
df['rate_per_sqft']=df['rate_per_sqft'].astype(str).str.replace(',','').astype(int)

df['status']=df['status'].str.strip().str.lower()
df['rera_approval']=df['rera_approval'].str.strip().str.lower()
df['flat_type']=df['flat_type'].str.strip().str.lower()

df=df.drop_duplicates()
print(df)

#Question 1: Which is the costliest flat?
costliest_flat=df.loc[df['price'].idxmax()]
print(costliest_flat)

#Question 2: Which locality has the highest average price?
highest_avg_price=df.groupby("locality")['price'].mean().sort_values(ascending=False) 
print(highest_avg_price)


# Question 3: Which locality has the highest rate per square foot?
highest_rate_per_square=df.groupby('locality')['rate_per_sqft'].mean().sort_values(ascending=False)
print(highest_rate_per_square)

#Question 4: Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price=df[df['status']=='ready to move']['price'].mean()
under_construction_avg_price=df[df['status']=='under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready-to-move properties cost more than under-construction properties.")
else:
    print("Under-construction properties cost more than ready-to-move properties.")

# Question 5: Does RERA approval affect pricing?
rera_approval_affect_price=df.groupby('rera_approval')['price'].mean()
print(rera_approval_affect_price)

# Question 6: How does area (sqft) impact property price?
sns.scatterplot(x='area',y='price',data=df)
plt.show()

# Question 7: Which BHK configuration is the most expensive on average?
bhk_configuration=df.groupby('bhk_count')['price'].mean()
print(bhk_configuration)

# Question 8: Which property type (Apartment, Floor, Plot) is the costliest?
property_type=df.groupby('flat_type')['price'].mean()
print(property_type)

# Question 9: Do certain builders or companies consistently price higher?
builders_price=df.groupby('company_name')['price'].mean().sort_values(ascending=False)


# Question 10:Are larger homes always more expensive per square foot?
sns.scatterplot(x='area',y='rate_per_sqft',data=df)
plt.show()