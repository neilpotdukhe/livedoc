import plotly.express as px
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


df = pd.read_csv("test2.csv")
fig = px.line_polar(df, r="points",
                    theta="categories",
                    color="player",
                    line_close=True,
                    #color_discrete_sequence=["#00eb93", "#4ed2ff"],
                    template="plotly_dark"
                    )                   

fig.update_polars(angularaxis_showgrid=False,
                  radialaxis_gridwidth=0,
                  gridshape='linear',
                  bgcolor="#494b5a",
                  radialaxis_showticklabels=False
                  #legend_title_font_color="green"
                  )

fig.update_layout(legend_font_color="black",title = "Player Comparison")


#ig.update_layout(paper_bgcolor="#2c2f36")
st.plotly_chart(fig, theme="streamlit", use_container_width = False)



def draw_table(df, theme, table_height):
    columns = df.columns

    thead1="""<thead><th scope="col"></th>"""
    thead_temp = []
    for k in range(len(list(columns))):
        thead_temp.append("""<th scope="col" class="text-white">"""+str(list(columns)[k])+"""</th>""")

    header = thead1+"".join(thead_temp)+"""</tr></thead>"""

    rows = []
    rows_temp = []

    for i in range(df.shape[0]):
        rows.append("""<th scope="row">"""+str(i+1)+"""</th>""")
        rows_temp.append(df.iloc[i].values.tolist())

    td_temp = []
    for j in range(len(rows_temp)):
        for m in range(len(rows_temp[j])):
            td_temp.append("""<td class="text-white">"""+str(rows_temp[j][m])+"""</td>""")


    td_temp2 = []

    for n in range(len(td_temp)):
        td_temp2.append(td_temp[n:n+df.shape[1]])

    td_temp3 = []

    for x in range(len(td_temp2)):
        if int(x % (df.shape[1])) == 0:
            td_temp3.append(td_temp2[x])

    td_temp4 = []

    for xx in range(len(td_temp3)):
        td_temp4.append("".join(td_temp3[xx]))

    td_temp5 = []
    for v in range(len(td_temp4)):
        td_temp5.append("""<tr><th scope="row" class="text-white">"""+str(v+1)+"""</th>"""+str(td_temp4[v])+"""</tr>""")

    table_html = """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">"""+\
    """<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>"""+\
    """<table class="table text-center table-bordered """+str(theme)+'"'+">""" + \
    header+"""<tbody>"""+"".join(td_temp5)+"""</tbody></table>"""

    return components.html(table_html,height=table_height, scrolling=True)

theme ="bg-primary"
draw_table(df, theme=theme, table_height=300)




