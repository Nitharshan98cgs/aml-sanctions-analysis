
import pandas as pd
import matplotlib.pyplot as plt

# Load the OFAC SDN list
df = pd.read_csv('sdn.csv', header=None, encoding='latin-1')

# Correct 12 columns
df.columns = ['ID', 'Name', 'Type', 'Program', 'Title', 
              'Call_Sign', 'Vessel_Type', 'Tonnage', 'GRT', 
              'Vessel_Flag', 'Vessel_Owner', 'Remarks']

# Basic stats
print("=== OFAC SDN LIST ANALYSIS ===")
print(f"Total sanctioned entries: {len(df)}")

# Entity type breakdown
print("\n--- Entity Types ---")
print(df['Type'].value_counts())

# Top sanctions programs
print("\n--- Top 15 Sanctions Programs ---")
print(df['Program'].value_counts().head(15))

# Plot 1 - Entity Types
df['Type'].value_counts().plot(kind='bar', 
    title='OFAC SDN — Entity Type Breakdown',
    color='navy', figsize=(8,5))
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('entity_types.png')
plt.show()

# Plot 2 - Top Sanctions Programs  
df['Program'].value_counts().head(15).plot(kind='barh',
    title='Top 15 OFAC Sanctions Programs',
    color='steelblue', figsize=(10,6))
plt.xlabel('Count')
plt.tight_layout()
plt.savefig('sanctions_programs.png')
plt.show()

print("\nDone. Charts saved to your AML_Projects folder.")