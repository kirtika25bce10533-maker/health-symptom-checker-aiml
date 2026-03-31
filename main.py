Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
... from sklearn.tree import DecisionTreeClassifier
... from sklearn.model_selection import train_test_split
... from sklearn.metrics import accuracy_score, classification_report
... 
... 
... data = {
...     'fever':       [1,1,0,0,1,1,0,1,0,1,1,0],
...     'cough':       [1,1,1,0,1,1,0,1,0,1,1,0],
...     'headache':    [1,1,0,1,1,1,0,1,0,1,1,0],
...     'fatigue':     [1,1,1,0,1,1,0,1,0,1,1,0],
...     'body_pain':   [1,1,0,0,1,1,0,1,0,1,1,0],
...     'sore_throat': [1,1,1,0,1,1,0,1,0,1,1,0],
...     'runny_nose':  [1,1,1,1,0,1,0,0,1,1,1,0],
...     'disease': [
...         'Flu', 'Viral Fever', 'Cold', 'Allergy', 'Flu', 'Infection',
...         'Allergy', 'Viral Fever', 'Allergy', 'Infection',
...         'Viral Fever', 'Cold'
...     ]
... }
... 
... df = pd.DataFrame(data)
... 
... X = df.drop('disease', axis=1)
... y = df['disease']
... 
... X_train, X_test, y_train, y_test = train_test_split(
...     X, y, test_size=0.2, random_state=42
... )
... 
... model = DecisionTreeClassifier()
... model.fit(X_train, y_train)
... 
... y_pred = model.predict(X_test)
... 
... accuracy = accuracy_score(y_test, y_pred)
... print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nEnter symptoms (1 = Yes, 0 = No):")

user_input = []
for symptom in X.columns:
    value = int(input(f"{symptom.replace('_', ' ').title()}: "))
    user_input.append(value)
    
prediction = model.predict([user_input])

print("\nPredicted Disease:", prediction[0])
