# Bokeh
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Viridis256
# Pandas
# import pandas

from data import provinces, dates, data

if __name__ == '__main__':

#*   CSV
    # Read in csv
    # data_frame = pandas.read_csv('w_mean_tests.csv')

    # Create ColumnDataSource from data frame
    # source = ColumnDataSource(data_frame)

    output_file('women_salary.html')

    # date list
    # date = source.data['fecha'].tolist()

#*   Add plot
    graph = figure(
        x_range=provinces,
        plot_height=800,
        plot_width=900,
        title='Women salary',
        title_location='left',
        x_axis_label='Salaries',
        y_axis_label='Date',
        toolbar_location='above'
    )

#*   Render glyph
    graph.vbar_stack(
        dates,
        x='provinces',
        width=0.9,
        fill_color=factor_cmap(
            'provinces',
            palette=Viridis256,
            factors=provinces
        ),
        fill_alpha=0.9,
        source=data
    )

    graph.y_range.start = 0
    graph.x_range.range_padding = 0.1
    graph.xgrid.grid_line_color = None
    graph.axis.minor_tick_line_color = None
    graph.outline_line_color = None

    # # Add Tooltips
    hover = HoverTool()
    hover.tooltips = """
        <div>
            <h3>$name</h3>
            <div><b>Provincia</b> @provinces</div>
            <div><b>Salarie</b> @$dates</div>
        </div>
    """
    graph.add_tools(hover)

#?   Show or save results
    # show(graph)
    save(graph)
