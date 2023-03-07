"""This module provides functions for the layout of plots or similar in line with the corprorate design of GE KVG."""


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
    """
    Update a plotly object with the layout defaults of GE KVG.

    Args:
        plotly_object: A plotly object.
        plot_title,xaxis_title,yaxis_title,yaxis2_title,legend_title: Character vectors with the titles.
        legend_h_adjust: Numeric value which can be positive and negative. Default is -0.1.
        hovermode: Character vector with default "x". Other possible values are "y", "closest", FALSE, "x unified" and "y unified".
        legend_title_space: Character vector with white space to align legend title.
        yaxis2: Logical if a secondary y-axis is desired. Default is FALSE.
        yaxis2_args: Further arguments which are passed on to \code{layout}.
        font_size: Integer with the font size.
    Returns:
        A plotly object with the updated layout.
    """
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
            showgrid=True,
            gridcolor='grey',
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
        plot_bgcolor='white',
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
