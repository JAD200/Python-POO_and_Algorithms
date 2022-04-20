from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
import pandas


if __name__ == '__main__':

#   CSV
    # Read in csv
    data_frame = pandas.read_csv('w_mean_todos.csv')

    # Create ColumnDataSource from data frame
    source = ColumnDataSource(data_frame)

    output_file('women_salary.html')

    # Car list
    car_list = source.data['fecha'].tolist()

#   Add plot
    graph = figure(
        y_range=car_list,
        plot_width=700,
        plot_height=600,
        title='Women salary',
        title_location='left',
        x_axis_label='Salaries',
        y_axis_label='Date',
        toolbar_location='above',
    )

#   Render glyph
    graph.hbar(
        y='fecha',
        right='w_mean',
        left=0,
        height=0.4,
        color='blue',
        fill_alpha=0.5,
        source=source
    )


#*   Show or save results
    # show(graph)
    save(graph)
