from itertools import combinations
from collections import defaultdict

# Expanded dataset for Master's students (50 transactions)
transactions = [
    {'Data Mining', 'Machine Learning', 'Library Study', 'Research Papers'},
    {'Data Mining', 'Artificial Intelligence', 'Online Courses', 'Research Papers'},
    {'Machine Learning', 'Data Visualization', 'Group Study', 'Hackathons'},
    {'Artificial Intelligence', 'Data Visualization', 'Library Study'},
    {'Data Mining', 'Machine Learning', 'Artificial Intelligence', 'Research Papers'},
    {'Data Mining', 'Data Visualization', 'Online Courses', 'Group Study'},
    {'Machine Learning', 'Artificial Intelligence', 'Library Study', 'Research Papers'},
    {'Data Visualization', 'Online Courses', 'Hackathons', 'Research Papers'},
    {'Data Mining', 'Machine Learning', 'Online Courses', 'Hackathons'},
    {'Artificial Intelligence', 'Data Visualization', 'Group Study', 'Research Papers'},
    {'Data Mining', 'Machine Learning', 'Library Study'},
    {'Artificial Intelligence', 'Machine Learning', 'Hackathons', 'Online Courses'},
    {'Data Visualization', 'Research Papers', 'Group Study'},
    {'Artificial Intelligence', 'Research Papers', 'Library Study'},
    {'Data Mining', 'Artificial Intelligence', 'Hackathons', 'Research Papers'},
    {'Machine Learning', 'Group Study', 'Library Study'},
    {'Online Courses', 'Hackathons', 'Research Papers'},
    {'Data Mining', 'Artificial Intelligence', 'Online Courses'},
    {'Machine Learning', 'Research Papers', 'Hackathons'},
    {'Artificial Intelligence', 'Data Visualization', 'Online Courses'},
    {'Library Study', 'Group Study', 'Research Papers'},
    {'Machine Learning', 'Artificial Intelligence', 'Group Study'},
    {'Data Mining', 'Data Visualization', 'Library Study'},
    {'Artificial Intelligence', 'Hackathons', 'Research Papers'},
    {'Data Mining', 'Machine Learning', 'Online Courses'},
    {'Data Visualization', 'Library Study', 'Research Papers'},
    {'Machine Learning', 'Artificial Intelligence', 'Research Papers'},
    {'Data Mining', 'Group Study', 'Hackathons'},
    {'Artificial Intelligence', 'Library Study', 'Online Courses'},
    {'Machine Learning', 'Data Visualization', 'Research Papers'},
    {'Data Mining', 'Library Study', 'Research Papers'},
    {'Artificial Intelligence', 'Group Study', 'Hackathons'},
    {'Machine Learning', 'Data Mining', 'Research Papers'},
    {'Data Visualization', 'Group Study', 'Library Study'},
    {'Artificial Intelligence', 'Machine Learning', 'Library Study'},
    {'Data Mining', 'Artificial Intelligence', 'Research Papers'},
    {'Online Courses', 'Hackathons', 'Group Study'},
    {'Machine Learning', 'Library Study', 'Research Papers'},
    {'Artificial Intelligence', 'Data Visualization', 'Library Study'},
    {'Data Mining', 'Machine Learning', 'Hackathons'},
    {'Artificial Intelligence', 'Online Courses', 'Research Papers'},
    {'Machine Learning', 'Data Visualization', 'Hackathons'},
    {'Data Mining', 'Library Study', 'Group Study'},
    {'Artificial Intelligence', 'Machine Learning', 'Research Papers'},
    {'Data Visualization', 'Hackathons', 'Online Courses'},
    {'Machine Learning', 'Data Mining', 'Online Courses'},
    {'Artificial Intelligence', 'Library Study', 'Hackathons'},
    {'Data Visualization', 'Library Study', 'Online Courses'},
    {'Machine Learning', 'Artificial Intelligence', 'Hackathons'},
    {'Data Mining', 'Online Courses', 'Library Study'},
    {'Artificial Intelligence', 'Research Papers', 'Hackathons'}
]

# Parameters
min_support = 0.3  # Minimum support threshold
min_confidence = 0.7  # Minimum confidence threshold

# Function to calculate support of itemsets
def calculate_support(itemset, transactions):
    count = sum(1 for transaction in transactions if itemset.issubset(transaction))
    return count / len(transactions)

# Generate frequent itemsets
def apriori(transactions, min_support):
    single_items = {frozenset([item]) for transaction in transactions for item in transaction}
    current_itemsets = single_items
    frequent_itemsets = []
    support_data = {}

    k = 1
    while current_itemsets:
        valid_itemsets = {itemset for itemset in current_itemsets if calculate_support(itemset, transactions) >= min_support}
        frequent_itemsets.extend(valid_itemsets)

        for itemset in valid_itemsets:
            support_data[itemset] = calculate_support(itemset, transactions)

        current_itemsets = {i.union(j) for i in valid_itemsets for j in valid_itemsets if len(i.union(j)) == k + 1}
        k += 1

    return frequent_itemsets, support_data

# Generate association rules
def generate_rules(frequent_itemsets, support_data, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        if len(itemset) > 1:
            for consequent in map(frozenset, combinations(itemset, 1)):
                antecedent = itemset - consequent
                if antecedent:
                    confidence = support_data[itemset] / support_data[antecedent]
                    if confidence >= min_confidence:
                        rules.append((antecedent, consequent, confidence))
    return rules

# Run Apriori algorithm
frequent_itemsets, support_data = apriori(transactions, min_support)
rules = generate_rules(frequent_itemsets, support_data, min_confidence)

# Display results
print("Frequent Itemsets:")
for itemset in frequent_itemsets:
    print(f"{set(itemset)}: Support = {support_data[itemset]:.2f}")

print("\nAssociation Rules:")
for antecedent, consequent, confidence in rules:
    print(f"{set(antecedent)} => {set(consequent)} (Confidence = {confidence:.2f})")
