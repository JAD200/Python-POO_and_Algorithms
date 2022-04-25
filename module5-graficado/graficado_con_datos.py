# Bokeh
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool, PanTool
from bokeh.transform import factor_cmap
from bokeh.palettes import PuOr
# Pandas
# import pandas
# Data
from data import provinces, dates, data

#   Todo
##  Erease the metrics of x axis and improve the annotations
##  Show a hover with detailed information


if __name__ == '__main__':


#*   CSV
    # Read in csv
    # data_frame = pandas.read_csv('w_mean_tests.csv')
    data_frame = data

    # Create ColumnDataSource from data frame
    source = ColumnDataSource(data_frame)

    output_file('women_salary.html')

    # date list
    # date = source.data['fecha'].tolist()

#*   Add plot
    graph = figure(
        background_fill_color='#3A3845',
        plot_height=750,
        plot_width=1000,
        title_location='above',
        title='Women salary',
        tools='save, reset, hover',
        tooltips = 'Fecha: $name',
        x_axis_label='Provinces',
        x_range=provinces,
        y_axis_label='Salaries',
    )

#*   Render glyph
    graph.vbar_stack(
        dates,
        x='provinces',
        width=0.9,
        color=PuOr[len(dates)],
        fill_alpha=0.9,
        legend_label=dates,
        source=source
    )

#   Plot arrangements
    graph.y_range.start = 0
    graph.x_range.range_padding = 0.07
    graph.xgrid.grid_line_color = None
    graph.ygrid.grid_line_color = None
    graph.axis.minor_tick_line_color = None
    graph.outline_line_color = None

#   Toolbar
    # graph.add_tools(hover)
    graph.add_tools(PanTool(dimensions='width'))
    graph.toolbar.autohide = True

#   Legend
    graph.legend.location = "top_left"
    graph.legend.orientation = "horizontal"


#?   Show or save results
    def show_or_save(option):
        """show_or_save Determines if it generates a new HTML file or saves the current one

        Args:
            option (int): Number to choose between show or save
        """
        if option == 1:
            show(graph)
            print('\n' * 4,'Graph created here: http://127.0.0.1:5500/module5-graficado/women_salary.html')
        else:
            save(graph)
            print('_' * 3, 'Graph saved', '_' * 3,)

    show_or_save(0)
