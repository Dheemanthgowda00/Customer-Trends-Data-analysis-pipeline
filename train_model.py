# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder
# import joblib
#
#
# def prepare_and_train():
#     # 1. Load Data
#     df = pd.read_csv(r'C:\Users\Dheemanth\Downloads\customer_shopping_behavior.csv')
#
#     # 2. FEATURE ENGINEERING
#     # Since we don't have real dates in this static CSV, we will simulate
#     # churn based on 'Frequency of Purchases' and 'Review Rating' for this demo.
#     # In a real scenario, we'd use (Current Date - Last Purchase Date).
#
#     # Let's create a 'Churn' label based on low rating and low frequency
#     # (This is the pattern the AI will try to learn)
#     df['is_churned'] = ((df['Review Rating'] < 3.0) & (df['Frequency of Purchases'] == 'Fortnightly')).astype(int)
#
#     # 3. Encoding Categorical Data (Turning text into numbers)
#     le = LabelEncoder()
#     df['gender_n'] = le.fit_transform(df['Gender'])
#     df['category_n'] = le.fit_transform(df['Category'])
#     df['season_n'] = le.fit_transform(df['Season'])
#
#     # 4. Selecting Features (The inputs for the AI)
#     features = ['Age', 'Purchase Amount (USD)', 'Review Rating', 'gender_n', 'category_n', 'season_n']
#     X = df[features]
#     y = df['is_churned']
#
#     # 5. Split and Train
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
#     model = RandomForestClassifier(n_estimators=100, random_state=42)
#     model.fit(X_train, y_train)
#
#     # 6. Save the "Brain"
#     joblib.dump(model, 'churn_model.pkl')
#     print("✅ Model trained and saved as 'churn_model.pkl'")
#
#
# if __name__ == "__main__":
#     prepare_and_train()

# ======================================================================================================================================================

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder
# import joblib
#
#
# def prepare_and_train():
#     # 1. Load Data (Using your exact columns)
#     df = pd.read_csv(r'C:\Users\Dheemanth\Downloads\customer_shopping_behavior.csv')
#
#     # 2. DEFINE REALISTIC CHURN (Multi-Factor)
#     # A customer is churned (1) if:
#     # - They shop rarely (Annually)
#     # - OR They have low previous purchases AND low ratings
#     # - OR They have a very high gap between purchases (purchase_frequency_days)
#
#     cond_1 = (df['frequency_of_purchases'] == 'Annually')
#     cond_2 = (df['review_rating'] < 3.0) & (df['previous_purchases'] < 5)
#     cond_3 = (df['purchase_frequency_days'] > 300)  # Assuming > 300 days is a 'lost' customer
#
#     df['is_churned'] = (cond_1 | cond_2 | cond_3).astype(int)
#
#     # 3. ENCODING (Turning your specific text columns into numbers)
#     le = LabelEncoder()
#     # We create a dictionary to keep track of encoders for the pipeline later
#     df['gender_n'] = le.fit_transform(df['gender'])
#     df['category_n'] = le.fit_transform(df['category'])
#     df['subscription_n'] = le.fit_transform(df['subscription_status'])
#     df['freq_n'] = le.fit_transform(df['frequency_of_purchases'])
#
#     # 4. SELECTING FEATURES
#     # We use your new engineered columns like age_group and purchase_frequency_days
#     features = [
#         'age', 'purchase_amount', 'review_rating',
#         'previous_purchases', 'purchase_frequency_days',
#         'gender_n', 'category_n', 'subscription_n', 'freq_n'
#     ]
#
#     X = df[features]
#     y = df['is_churned']
#
#     # 5. TRAIN
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
#     # Random Forest is great for handling 'categories' and 'numbers' together
#     model = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42)
#     model.fit(X_train, y_train)
#
#     # 6. SAVE
#     joblib.dump(model, 'churn_model.pkl')
#     print(f"✅ Model trained on {len(features)} features and saved!")
#
#
# if __name__ == "__main__":
#     prepare_and_train()

# ======================================================================================================================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib


def prepare_and_train():
    # 1. Load your cleaned dataset
    # Make sure this path points to your actual file
    df = pd.read_csv(r'C:\Users\Dheemanth\Downloads\customer_shopping_behavior.csv')

    # Standardize names immediately for logic
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    # 2. THE REAL-WORLD LOGIC (Defining the "Churn" Label)
    # 1 = Churned (Likely to leave), 0 = Loyal
    cond_1 = (df['frequency_of_purchases'] == 'Annually')
    cond_2 = (df['review_rating'] < 3.0) & (df['previous_purchases'] < 5)

    df['is_churned'] = (cond_1 | cond_2).astype(int)

    # 3. ENCODING (Turning text into numbers for the AI)
    le = LabelEncoder()
    df['gender_n'] = le.fit_transform(df['gender'])
    df['category_n'] = le.fit_transform(df['category'])
    df['freq_n'] = le.fit_transform(df['frequency_of_purchases'])

    # 4. SELECTING FEATURES
    # We use the columns that actually impact behavior
    features = ['age', 'purchase_amount_usd', 'review_rating', 'previous_purchases', 'gender_n', 'category_n', 'freq_n']

    X = df[features]
    y = df['is_churned']

    # 5. TRAINING
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 6. SAVE
    joblib.dump(model, 'churn_model.pkl')
    print("✅ Step 1 Complete: 'churn_model.pkl' created successfully.")


if __name__ == "__main__":
    prepare_and_train()