# Bokeh
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource, Legend, LegendItem
from bokeh.models.tools import HoverTool, PanTool
from bokeh.palettes import viridis
# Pandas
# import pandas
# Data
from data import provinces, dates, data

#   Todo
##  Show a hover with detailed information


if __name__ == '__main__':


#*   CSV
    # Read in csv
    # df = pandas.read_csv('w_mean_complete.csv')

    # # Create ColumnDataSource from data frame
    # source = ColumnDataSource(df)

    output_file('women_salary.html')


#*   Add plot
    graph = figure(
        background_fill_color='#595260',
        plot_height=750,
        plot_width=1400,
        title_location='above',
        title='Women salary',
        tools='save, reset',
        x_axis_label='Salaries',
        y_range=dates,
        y_axis_label='Dates',
    )

#*   Render glyph
    graph.hbar_stack(
        provinces,
        y='dates',
        height=0.9,
        color=viridis(len(provinces)),
        fill_alpha=0.9,
        legend_label=provinces,
        source=data,
    )

#   Plot arrangements
    graph.y_range.range_padding = 0.07
    graph.x_range.range_padding = 0.68
    graph.xgrid.grid_line_color = None
    graph.ygrid.grid_line_color = None
    graph.axis.minor_tick_line_color = None
    graph.outline_line_color = None

#   Toolbar
    hover = HoverTool()
    hover.tooltips = [
        ('Provincia:', '$name'),
        ('Fecha:', '@dates'),
        # ('Salarios:', '$y{0,0.0}')
    ]
    graph.add_tools(hover)
    graph.add_tools(PanTool(dimensions='width'))
    graph.toolbar.autohide = True

#   Legend
    graph.legend.location = "top_left"
    graph.legend.click_policy="mute"
    graph.legend.orientation = "vertical"


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
