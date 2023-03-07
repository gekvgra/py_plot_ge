"""Main module."""


def plotly_gelayout(
    plotly_object,
    plot_title="",
    xaxis_title="",
    yaxis_title="",
    legend_title="",
    legend_h_adjust=-0.2,
    hovermode="x",
    font_size=12
):
    plotly_object.update_layout(
        title=plot_title,
        xaxis=dict(
            title=xaxis_title,
            titlefont=dict(size=font_size),
            showgrid=False
        ),
        yaxis=dict(
            title=yaxis_title,
            titlefont=dict(size=font_size),
            zeroline=False
        ),
        legend=dict(
            orientation="h",
            itemclick="toggle",
            itemdoubleclick="toggleothers",
            y=legend_h_adjust,
            x=0.5,
            xanchor="center",
            title=dict(
                text=legend_title,
                side="top"
            )
        ),
        font=dict(family="arial", size=font_size),
        hovermode=hovermode,
        clickmode="select",
        autosize=True,
        margin=dict(l=50, r=50, b=20, t=20, pad=4),
        modebar_remove=[
            "pan",
            "zoom",
            "zoomIn",
            "zoomOut",
            "autoScale",
            "resetScale",
            "toggleSpikelines",
            "lasso2d",
            "select2d",
            "hoverClosestCartesian",
            "hoverCompareCartesian"
        ]
    )

    return plotly_object
