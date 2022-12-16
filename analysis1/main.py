from linear import linear_answer
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
def data(x):
    return datetime.fromtimestamp(int(float(x)))

def data1(x):
    return datetime.fromtimestamp(int(float(x[0])))

def linear_plot(file, xvar, yvar):
    df = pd.read_csv(f"data/{file}.csv")
    df[xvar] = df[xvar].apply(data)
    ok = linear_answer(f"data/{file}", xvar, yvar)
    fig = go.Figure(data=go.Scatter(x=df[xvar].to_numpy(), y=df[yvar].to_numpy(),mode="lines"))
    fig.write_html(f"templates/{file}.html")
    return True


def quadratic_plot(file, xvar, yvar):
  df = pd.read_csv(f"data/{file}.csv")
  df[xvar] = df[xvar].apply(data)
  ok = quadratic_answer(f"data/{file}", xvar, yvar)
  fig = go.Figure(data=go.Scatter(x=df[xvar].to_numpy(), y=df[yvar].to_numpy(),mode="markers"))
  fig.add_trace(go.Scatter(x=df[xvar], y=ok[1],
                    mode='lines',
                    name='lines'))
  fig.write_html(f"templates/{file}.html")
  return True


def lin_and_quad(file,xvar,yvar):
    fig = make_subplots(rows=2, cols=1)
    fig.update_layout(autotypenumbers='convert types')
    df = pd.read_csv(f"data/{file}.csv")
    df[xvar] = df[xvar].apply(data)
    oa = [df[xvar],df[yvar]]
    f1 = go.Scatter(x=oa[0],
                   y=oa[1],
                   mode="markers")
    fig.append_trace(f1, row=1, col=1)
    fig.append_trace(f1,row=2,col=1)
    ok = linear_answer(f"data/{file}", xvar, yvar)
    fig.append_trace(
          go.Scatter(
              x=oa[0],
              y=ok[1],
              mode="lines",
              name=yvar,
              line=go.scatter.Line(color="gray"),
              showlegend=True), row=1, col=1)
    ok = quadratic_answer(f"data/{file}",xvar,yvar)
    fig.append_trace(
            go.Scatter(
                x=oa[0],
                y=ok[1],
                mode="lines",
                name=yvar,
                line=go.scatter.Line(color="gray"),
                showlegend=True), row=2, col=1)
    fig.write_html(f"templates/{file}.html")
    return True
def get_all_data(file):
    fig = make_subplots(rows=2, cols=2)
    fig.update_layout(autotypenumbers='convert types')
    df = pd.read_csv(f"data/{file}.csv")
    xvar = "Timestamp"
    df[xvar] = df[xvar].apply(data)
    yvart = "Temperature"
    yvarh = "Humidity"
    yvarg = "gas"
    oa = [df[xvar],df[yvart]]
    ok = linear_answer(f"data/{file}", xvar, yvart)
    fig.append_trace(
        go.Scatter(
            x=oa[0],
            y=ok[1],
            mode="lines",
            name=yvart,
            line=go.scatter.Line(color="gray"),
            showlegend=True), row=1, col=1)
    fig.append_trace(
          go.Scatter(
              x=oa[0],
              y=oa[1],
              mode="markers",
              name = yvart,
              line=go.scatter.Line(color="blue"),
              showlegend=True), row=1, col=1)

    oa = [df[xvar],df[yvarh]]
    ok = linear_answer(f"data/{file}", xvar, yvarh)
    fig.append_trace(
        go.Scatter(
            x=oa[0],
            y=ok[1],
            mode="lines",
            name=yvarh,
            line=go.scatter.Line(color="gray"),
            showlegend=True), row=1, col=2)
    fig.append_trace(
          go.Scatter(
              x=oa[0],
              y=oa[1],
              mode="markers",
              name = yvarh,
              line=go.scatter.Line(color="green"),
              showlegend=True), row=1, col=2)

    oa = [df[xvar],df[yvarg]]
    ok = linear_answer(f"data/{file}", xvar, yvarg)
    fig.append_trace(
        go.Scatter(
            x=oa[0],
            y=ok[1],
            mode="lines",
            name=yvarg,
            line=go.scatter.Line(color="gray"),
            showlegend=True), row=2, col=1)
    fig.append_trace(
          go.Scatter(
              x=oa[0],
              y=oa[1],
              mode="markers",
              name = yvarg,
              line=go.scatter.Line(color="green"),
              showlegend=True), row=2, col=1)
    fig.write_html(f"templates/{file}.html")
    return True
  