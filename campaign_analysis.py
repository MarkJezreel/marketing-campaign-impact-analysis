import pandas as pd
from scipy.stats import ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
file_path = 'Dataset.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Segregate data
no_campaign_group = df[df['AcceptedCmpOverall'] == 0]  # Group with no campaign influence
campaign_influenced_group = df[df['AcceptedCmpOverall'] > 0]  # Group with campaign influence

# Extract corresponding 'MntTotal' values for each group
mnt_total_no_campaign = no_campaign_group['MntTotal']
mnt_total_campaign_influenced = campaign_influenced_group['MntTotal']

# Function to perform a t-test
def stat(column_1, column_2):
    # Perform an independent t-test
    t_stat, p_value = ttest_ind(column_1, column_2)

    # Display the results
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")

    # Interpret the result
    if p_value < 0.05:
        print("There is a significant difference between the two groups.")
    else:
        print("There is no significant difference between the two groups.")

# Perform the t-test between the two groups
stat(mnt_total_no_campaign, mnt_total_campaign_influenced)

# Add a new column for segmentation
df['CampaignGroup'] = df['AcceptedCmpOverall'].apply(lambda x: 'No Campaign' if x == 0 else 'Campaign Influenced')

# Create a boxplot for MntTotal segmented by CampaignGroup
plt.figure(figsize=(8, 8))
sns.boxplot(data=df, x='CampaignGroup', y='MntTotal', hue='CampaignGroup', palette='Set2', showfliers=True)

# Calculate mean
mean_no_campaign = df[df['CampaignGroup'] == 'No Campaign']['MntTotal'].mean()
mean_campaign_influenced = df[df['CampaignGroup'] == 'Campaign Influenced']['MntTotal'].mean()

# Add mean
plt.axhline(mean_no_campaign ,color='blue', linestyle='--', label=f'Mean (No Campaign): {mean_no_campaign:.2f}')
plt.axhline(mean_campaign_influenced, color='orange', linestyle='--', label=f'Mean (Campaign Influenced): {mean_campaign_influenced:.2f}')

# Customize the plot
plt.title('Boxplot of MntTotal by Campaign Influence', fontsize=16)
plt.xlabel('Campaign Influence', fontsize=14)
plt.ylabel('Total Spending (MntTotal)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show legend
plt.legend()

# Display the plot
plt.show()
