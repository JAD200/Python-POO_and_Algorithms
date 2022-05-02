# Maths
from math import pi
#? Bokeh
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import Legend, LegendItem
from bokeh.models.tools import HoverTool, PanTool
from bokeh.transform import cumsum
from bokeh.palettes import viridis
#? Pandas
import pandas

#   Todo
##  Show legend with all the provinces


if __name__ == '__main__':


#*   CSV
    # Read in csv
    df = pandas.read_csv('./w_mean_complete.csv', usecols=['provinces' , 'salaries'])
    print('\n', df.info())
    # Create ColumnDataSource from data frame

    output_file('women_salary.html')


    # Group by provinces and sum up the salaries
    total_salaries = df.groupby('provinces')['salaries'].apply(sum)

    # Set provinces for the legend and color palette
    provinces = df['provinces']
    provinces = set(provinces)# Remove duplicates
    provinces = sorted(provinces)# Sort provinces

    # Show dataframes
    # print(total_salaries, '\n -' * 2)
    # print(provinces, '\n -' * 2)

    # Prepare data for the graph
    data = pandas.Series(total_salaries).reset_index(name='value').rename(columns={'index': 'province'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = viridis(len(provinces))


#*   Add plot
    graph = figure(
        background_fill_color='#BFAE8E',
        plot_height=700,
        plot_width=700,
        title_location='above',
        title='Women salary \nOrdered by province',
        tools='save, reset',
    )

#*   Render glyph
    graph.wedge(x=0, y=1, radius=0.6,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', source=data)

#   Plot arrangements
    graph.axis.minor_tick_line_color = None
    graph.axis.visible = False
    graph.grid.grid_line_color = None
    graph.outline_line_color = None
    graph.title.background_fill_color = '#F2EFDF'
    graph.title.text_color = '#278C5D'
    graph.title.text_font_size = '25px'
    graph.x_range.range_padding = 0.68
    graph.y_range.range_padding = 0.07

#*   Annotations
##   Toolbar
    hover = HoverTool()
    hover.tooltips = [
        ('Provincia:', '@provinces'),
        ('Salarios:', '@value{$0,0.00}')
    ]
    graph.add_tools(hover)
    graph.add_tools(PanTool(dimensions='width'))
    graph.toolbar.autohide = True

##   Legend
    # graph.legend.location = 'top_left'
    # graph.legend.click_policy='mute'
    # graph.legend.orientation = 'vertical'


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
