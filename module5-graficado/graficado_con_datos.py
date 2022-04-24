# Bokeh
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Purples
# Pandas
# import pandas
# Data
from data import provinces, dates, data

#   Todo
##  Show a legend with all the dates
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
        x_range=provinces,
        plot_height=650,
        plot_width=900,
        title='Women salary',
        title_location='above',
        x_axis_label='Provinces',
        y_axis_label='Salaries',
        background_fill_color='#3A3845',
        toolbar_location='above',
        tools='pan,wheel_zoom,save,reset',
    )

#*   Render glyph
    graph.vbar_stack(
        dates,
        x='provinces',
        width=0.9,
        color=Purples[3],
        fill_alpha=0.9,
        source=source
    )

    graph.y_range.start = 0
    graph.x_range.range_padding = 0.1
    graph.xgrid.grid_line_color = None
    graph.axis.minor_tick_line_color = None
    graph.outline_line_color = None
    # graph.add_tools(hover)


#?   Show or save results
    def show_or_save(option):
        if option == 1:
            show(graph)
        else:
            save(graph)
            print('_' * 3, 'Graph saved', '_' * 3,)

    show_or_save(0)
