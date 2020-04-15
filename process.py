import json
import Connectors
import Transformations
import AutoML
try:
    BostonHousingPricingApp_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5e96f2ea4ee8f39cc9b615d1", spark, "{'url': '/Demo/BostonTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapi0ef076722999cf4cd8859e9aafdb7b76', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    BostonHousingPricingApp_AutoFE = Transformations.TransformationMain.run(["5e96f2ea4ee8f39cc9b615d1"], {"5e96f2ea4ee8f39cc9b615d1": BostonHousingPricingApp_DBFS}, "5e96f2ea4ee8f39cc9b615d2", spark, json.dumps({"FE": [{"transformationsData": {}, "feature": "CRIM", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "4.71", "stddev": "11.7", "min": "0.01301", "max": "88.9762", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "ZN", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "9.08", "stddev": "18.96", "min": "0.0", "max": "100.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "INDUS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "11.24", "stddev": "6.62", "min": "0.46", "max": "27.74", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "CHAS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "0.06", "stddev": "0.25", "min": "0.0", "max": "1.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "NOX", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "0.57", "stddev": "0.12", "min": "0.392", "max": "0.871", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "RM", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "6.26", "stddev": "0.73", "min": "3.561", "max": "8.725", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "AGE", "type": "real", "selected": "True", "replaceby": "mean", "stats": {
                                                                            "count": "140", "mean": "71.58", "stddev": "26.56", "min": "6.5", "max": "100.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "DIS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "3.71", "stddev": "2.07", "min": "1.3459", "max": "9.2229", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "RAD", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "10.08", "stddev": "8.95", "min": "1.0", "max": "24.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "TAX", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "415.13", "stddev": "172.51", "min": "188.0", "max": "711.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "PTRATIO", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "18.31", "stddev": "2.11", "min": "13.0", "max": "21.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "B", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "349.07", "stddev": "103.57", "min": "0.32", "max": "396.9", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "LSTAT", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "13.36", "stddev": "7.29", "min": "2.87", "max": "34.02", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "MEDV", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "140", "mean": "21.56", "stddev": "9.39", "min": "5.0", "max": "50.0", "missing": "0"}, "transformation": ""}]}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionRegression(BostonHousingPricingApp_AutoFE, [
                              "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"], "MEDV")

except Exception as ex:
    print(ex)
