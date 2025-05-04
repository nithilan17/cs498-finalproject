from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)

# 1) (AirBnB search) Display the listings available for a particular two-day period for Portland, OR with details: name, neighborhood, room
# type, how many guests it accommodates, property type and amenities, and per night’s cost, in descending order of average rating.
@app.route("/listings", methods=["GET"])
def get_listings():
    start_date = request.args.get("start")
    end_date = request.args.get("end")
    
    # TODO: Filter calendar for Portland listings available on both days
    # Join with listings.csv to get listing details
    # Sort by average rating

    return jsonify({
        "results": [
            {
                "name": "Modern Loft",
                "neighborhood": "Downtown",
                "room_type": "Entire home/apt",
                "guests": 4,
                "property_type": "Apartment",
                "amenities": ["Wifi", "Kitchen", "Washer"],
                "price_per_night": 135,
                "average_rating": 4.87
            },
            ...
        ]
    })

# 2) What neighborhoods in any of the cities that have no listings for a given month?
@app.route("/inactive_neighborhoods", methods=["GET"])
def get_inactive_neighborhoods():
    city = request.args.get("city")
    year = request.args.get("year")
    month = request.args.get("month")

    # TODO: Load neighborhoods.csv for that city
    # Filter calendar.csv for listings with availability in that month
    # Compare to listings' neighborhoods

    return jsonify({
        "city": city,
        "year": year,
        "month": month,
        "inactive_neighborhoods": [
            "Northgate",
            "Woodlawn",
            "Edgewater"
        ]
    })
    
# 4) (Booking trend, by month) For “Entire home/apt” type listings in Portland provide the total number of available nights (as per Query 3 
# for each month March through August of a given year.
@app.route("/portland_booking_trend", methods=["GET"])
def get_portland_booking_trend():
    year = request.args.get("year")

    # TODO: Filter calendar.csv for Portland listings of type "Entire home/apt"
    # Count available nights from March to August for each month

    return jsonify({
        "year": year,
        "city": "Portland",
        "monthly_available_nights": {
            "March": 15432,
            "April": 16327,
            "May": 15810,
            "June": 17002,
            "July": 17520,
            "August": 16200
        }
    })
    
# 5) (Booking trend, by city) For each city, how many reviews are received for December of each year?
@app.route("/december_reviews", methods=["GET"])
def get_december_reviews():
    # Optional: add a start_year / end_year filter
    # TODO: Count reviews in December by year and city

    return jsonify({
        "reviews": [
            {
                "city": "Los Angeles",
                "year": 2022,
                "december_reviews": 2301
            },
            {
                "city": "Portland",
                "year": 2022,
                "december_reviews": 1190
            },
            {
                "city": "Salem",
                "year": 2022,
                "december_reviews": 842
            },
            {
                "city": "San Diego",
                "year": 2022,
                "december_reviews": 3015
            }
        ]
    })