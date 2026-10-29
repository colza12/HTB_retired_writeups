# Uplink Artifact : AI/ML

During an analysis of a compromised satellite uplink, a suspicious dataset was recovered. Intelligence indicates it may encode physical access credentials hidden within the spatial structure of Volnaya’s covert data infrastructure.

Attachment  
a12c73b3-d0b8-47a7-94ad-42e5ce03b2f6.zip

# Solution

`uplink_spatial_auth.csv` is likely following:
```
x,y,z,label
23.618963638077386,1.6361824037129158,0.1868367359337949,2
21.0,22.0,0.5112963800310468,1
24.90563183083653,9.090546357672864,0.16593716012369497,2
6.0,24.0,0.4936907020272587,1
10.371859590422677,4.076531869693981,0.14996290922730326,2
12.32341650432917,10.006683484159732,0.49200490912773354,2
```
Plot the data in a 3D space and analyse it.
```python solve.py
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
```
![ql](qr_projection.html)

Read the data using QR code reader.

Got the flag!

`HTB{clu5t3r_k3y_l34k3d}`

# References

# Result
https://labs.hackthebox.com/achievement/challenge/2059414/941
