# Bokeh
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Magma256
# Pandas
import pandas


if __name__ == '__main__':

#*   CSV
    # Read in csv
    data_frame = pandas.read_csv('w_mean_tests.csv')

    # Create ColumnDataSource from data frame
    source = ColumnDataSource(data_frame)

    output_file('women_salary.html')

    # Car list
    year = source.data['fecha'].tolist()

#*   Add plot
    graph = figure(
        x_range=year,
        plot_width=700,
        plot_height=600,
        title='Women salary',
        title_location='left',
        x_axis_label='Salaries',
        y_axis_label='Date',
        toolbar_location='above',
    )

#*   Render glyph
    graph.vbar_stack(
        'w_mean',
        x='fecha',
        width=0.9,
        fill_color=factor_cmap(
            'fecha',
            palette=Magma256,
            factors=year
        ),
        fill_alpha=0.9,
        source=source
    )

    graph.y_range.start = 0
    graph.x_range.range_padding = 0.1
    graph.xgrid.grid_line_color = None
    graph.axis.minor_tick_line_color = None
    graph.outline_line_color = None

    # Add Legend
    # graph.legend.orientation = 'vertical'
    # graph.legend.location = 'top_right'
    # graph.legend.label_text_font_size = '10px'

    # Add Tooltips
    hover = HoverTool()
    hover.tooltips = """
        <div>
            <h3>@zona_prov</h3>
            <div><b>Fecha</b> @fecha</div>
            <div><b>Salarie</b> @w_mean</div>
        </div>
    """
    graph.add_tools(hover)

#?   Show or save results
    # show(graph)
    save(graph)
