import pandas as pd


def add_data(is_no, temperature, humidity, gas):
    timestamp = datetime.datetime.now().timestamp()
    try:
        dfb = pd.DataFrame(
            {"Timestamp": [int(timestamp)], "Temperature": [int(temperature)], "Humidity": [int(humidity)], "gas": [int(gas)]})
        df = pd.read_csv(f"data/{is_no}.csv")
        df = pd.concat([df, dfb])
        print(df)
        df.to_csv(f"data/{is_no}.csv", index=False)
    except:
        dfb.to_csv(f"data/{is_no}.csv", index=False)