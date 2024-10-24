from flask import request, jsonify
from config import db, app
from models import MostSixesAllSeasonsCombined , MostWicketsAllSeasons, MostRunsConcededPerInningsAllSeasonsCombine ,  MostRunsPerOverAllSeasonsCombine ,  MostRunsAllSeasonsCombine , MostFoursPerInningsAllSeasonsCombine, FastestCenturiesAllSeasonsCombine , MostDotBallsPerInnings , BestBowlingStrikeRatePerInningsAllSeasonsCombine , BestBowlingEconomyPerInningsAllSeasonsCombine


@app.route("/show_most_sixes", methods=["GET"])
def get_most_sixes_data():
    most_sixes_data = MostSixesAllSeasonsCombined.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_sixes_data))
    return jsonify({"most_sixes": json_data})

@app.route("/show_most_wickets", methods=["GET"])
def get_most_wickets_data():
    most_wickets_data = MostWicketsAllSeasons.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_wickets_data))
    return jsonify({"most_wickets": json_data})

@app.route("/show_most_runs_conceded", methods=["GET"])
def get_most_runs_conceded_data():
    most_runs_data = MostRunsConcededPerInningsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_runs_data))
    return jsonify({"most_runs_conceded": json_data})

@app.route("/show_most_runs_per_over", methods=["GET"])
def get_most_runs_per_over_data():
    most_runs_per_over_data =  MostRunsPerOverAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_runs_per_over_data))
    return jsonify({"most_runs_conceded": json_data})

@app.route("/show_most_runs", methods=["GET"])
def get_most_runs_data():
    most_runs_data =  MostRunsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_runs_data))
    return jsonify({"most_runs": json_data})

@app.route("/show_most_fours_per_innings", methods=["GET"])
def get_most_fours_per_innings_data():
    most_fours_per_innings_data =  MostFoursPerInningsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_fours_per_innings_data))
    return jsonify({"most_runs": json_data})

@app.route("/show_fastest_centuries", methods=["GET"])
def get_Fastest_Centuries_data():
    Fastest_Centuries_data = FastestCenturiesAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), Fastest_Centuries_data))
    return jsonify({"Fastest_Centuries": json_data})

@app.route("/show_most_dot_balls", methods=["GET"])
def get_most_dot_balls():
    most_dot_balls = MostDotBallsPerInnings.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_dot_balls))
    return jsonify({"Most_Dot_Balls": json_data})

@app.route("/show_best_bowling_strike_rate", methods=["GET"])
def get_best_bowling_strike_rate():
    best_bowling_strike_rate = BestBowlingStrikeRatePerInningsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), best_bowling_strike_rate))
    return jsonify({"Best Bowling Strike Rate": json_data})

@app.route("/show_best_bowling_economy", methods=["GET"])
def get_best_bowling_economy():
    best_bowling_economy = BestBowlingEconomyPerInningsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), best_bowling_economy))
    return jsonify({"Best Bowling Economy": json_data})

if __name__ == '__main__':
    app.run(debug=True)


    