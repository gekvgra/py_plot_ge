"""This module provides functions for the layout of plots or similar in line with the corprorate design of GE KVG."""


def plotly_gelayout(
    plotly_object,
    plot_title='',
    xaxis_title='',
    yaxis_title='',
    yaxis2_title='',
    legend_title='',
    legend_h_adjust=-0.2,
    hovermode='x',
    yaxis2=False,
    yaxis2_args=None,
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
    yaxis2_args_default = {
        'overlaying': 'y',
        'side': 'right',
        'title': yaxis2_title,
        'titlefont': {'size': font_size},
        'showgrid': False,
        'fixedrange': True,
        'zeroline': False
    }

    if yaxis2_args is None:
        yaxis2_args_default.update({
            'dtick': 100 / 7,
            'tick0': 100 / 7,
            'tickformat': '.0f'
        })
    else:
        yaxis2_args_default.update(yaxis2_args)

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
            orientation='h',
            itemclick='toggle',
            itemdoubleclick='toggleothers',
            y=legend_h_adjust,
            x=0.5,
            xanchor='center',
            title=dict(
                text=legend_title,
                side='top'
            )
        ),
        font=dict(family='arial', size=font_size),
        hovermode=hovermode,
        clickmode='select',
        autosize=True,
        plot_bgcolor='white',
        margin=dict(l=50, r=50, b=50, t=50, pad=4),
        modebar_remove=[
            'pan',
            'zoom',
            'zoomIn',
            'zoomOut',
            'autoScale',
            'resetScale',
            'toggleSpikelines',
            'lasso2d',
            'select2d',
            'hoverClosestCartesian',
            'hoverCompareCartesian'
        ]
    )

    return plotly_object


def adjust_plotly_axis(y1_data, y2_data):
    """
    Adjust ticks of second y-axis in plotly

    Args:
        y1_data,y2_data: Vectors or dataframe columns with the data.
    Returns:
        A dict with y1 & y2 range min & max and the dticks.
    """
    # y1
    y1_min = min(y1_data, default=None)
    y1_max = max(y1_data, default=None)

    if y1_min is not None and y1_min < 0:
        y1_range = y1_max - y1_min
    else:
        y1_range = y1_max

    y1_dtick = int(str(y1_range)[0]) * 10 ** (len(str(int(y1_range))) - 1)

    # y2
    y2_min = min(y2_data, default=None)
    y2_max = max(y2_data, default=None)

    if y2_min is not None and y2_min < 0:
        y2_range = y2_max - y2_min
    else:
        y2_range = y2_max

    y2_dtick = int(str(y2_range)[0]) * 10 ** (len(str(int(y2_range))) - 1)

    # dtick ratio
    y1_dtick_ratio = y1_range / y1_dtick
    y2_dtick_ratio = y2_range / y2_dtick

    global_dtick_ratio = max(y1_dtick_ratio, y2_dtick_ratio)

    # Range minimums
    negative = False

    if y1_min is not None and y1_min < 0:
        negative = True
        y1_negative_ratio = abs(y1_min / y1_range) * global_dtick_ratio
    else:
        y1_negative_ratio = 0

    if y2_min is not None and y2_min < 0:
        negative = True
        y2_negative_ratio = abs(y2_min / y2_range) * global_dtick_ratio
    else:
        y2_negative_ratio = 0

    # Increase the ratio by 0.1 so that your range minimums are extended just far enough to not cut off any part of your lowest value
    global_negative_ratio = max(y1_negative_ratio, y2_negative_ratio) + 0.1

    if negative:
        y1_range_min = (global_negative_ratio) * y1_dtick * -1
        y2_range_min = (global_negative_ratio) * y2_dtick * -1
    else:
        y1_range_min = 0
        y2_range_min = 0

    # Range maximums
    y1_positive_ratio = abs(y1_max / y1_range) * global_dtick_ratio
    y2_positive_ratio = abs(y2_max / y2_range) * global_dtick_ratio

    global_positive_ratio = max(y1_positive_ratio, y2_positive_ratio) + 0.1

    y1_range_max = global_positive_ratio * y1_dtick
    y2_range_max = global_positive_ratio * y2_dtick

    out_dict = {
        "y1_range_min": y1_range_min,
        "y1_range_max": y1_range_max,
        "y1_dtick": y1_dtick,
        "y2_range_min": y2_range_min,
        "y2_range_max": y2_range_max,
        "y2_dtick": y2_dtick
    }

    return out_dict
