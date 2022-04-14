from bokeh.plotting import figure, output_file, show


if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_values = int(input('Cuantos valores quieres graficar? '))
    x_values = list(range(total_values))
    y_values = []

    for x in x_values:
        value = int(input(f'Valor "Y" para {x: }'))
        y_values.append(value)

    fig.line(x_values, y_values, line_width=2)
    show(fig)