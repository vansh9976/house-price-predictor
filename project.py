import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def model(landArea, floorArea, bedrooms, bathrooms, garages, buildYear):
    data = pd.read_csv("C:\\Users\\vb_49\\OneDrive\\Desktop\\data mining\\perth.csv")
    

    data = data.dropna()

    x = data[['LAND_AREA', 'FLOOR_AREA', 'BEDROOMS', 'BATHROOMS', 'GARAGE', 'BUILD_YEAR']].values
    y = data['PRICE'].values

    poly = PolynomialFeatures(degree=2)
    x_poly = poly.fit_transform(x)

    model = LinearRegression() 
    model.fit(x_poly, y)

    values = model.predict(poly.fit_transform([[landArea, floorArea, bedrooms, bathrooms, garages, buildYear]]))
    return values