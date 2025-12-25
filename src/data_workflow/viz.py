from pathlib import Path
import plotly.express as px
import pandas as pd


def save_fig(fig, path: Path, *, scale: int = 2) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_image(str(path), scale=scale)


def bar_sorted(df: pd.DataFrame, x: str, y: str, title: str):
    d = df.sort_values(y, ascending=False)
    fig = px.bar(d, x=x, y=y, title=title)
    fig.update_layout(
        title={"x": 0.02},
        margin={"l": 60, "r": 20, "t": 60, "b": 60},
    )
    fig.update_xaxes(title_text=x)
    fig.update_yaxes(title_text=y)
    return fig


def time_line(df: pd.DataFrame, x: str, y: str, color=None, title: str = ""):
    fig = px.line(df, x=x, y=y, color=color, title=title)
    fig.update_layout(title={"x": 0.02})
    fig.update_xaxes(title_text=x)
    fig.update_yaxes(title_text=y)
    return fig


def histogram_chart(df: pd.DataFrame, x: str, nbins: int = 30, title: str = ""):
    fig = px.histogram(df, x=x, nbins=nbins, title=title)
    fig.update_layout(title={"x": 0.02})
    fig.update_xaxes(title_text=x)
    fig.update_yaxes(title_text="Count")
    return fig