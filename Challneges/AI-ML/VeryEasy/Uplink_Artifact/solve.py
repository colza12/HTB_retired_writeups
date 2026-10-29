import pandas as pd
import plotly.express as px

# load data
df = pd.read_csv('uplink_spatial_auth.csv')

# 3d plot image
fig_3d = px.scatter_3d(df, x="x", y="y", z="z", color="label", opacity=0.7)
fig_3d.write_html("check_3d.html")
print("save 3d image check_3d.html")


# extract label 1
qr_points = df[df["label"] == 1]

# scatter 2d plot
fig_2d = px.scatter(
    qr_points,
    x="x",
    y="y",
    title="QR Code Projection",
    color_discrete_sequence=["black"],
)

# Adjust appearance
fig_2d.update_traces(marker=dict(size=18, symbol="square"))
fig_2d.update_yaxes(autorange="reversed")

fig_2d.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title=""),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title=""),
    plot_bgcolor="white",
    paper_bgcolor="white",
    width=600,
    height=600,
    margin=dict(l=10, r=10, t=10, b=10),
)

# save 2d image
fig_2d.write_html("qr_projection.html")
print("save 2d image qr_projection.html")
