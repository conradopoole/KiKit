import click

@click.command()
@click.argument("board", type=click.Path(dir_okay=False, exists=True))
@click.option("--show/--hide", "-s", help="Show/hide references mathing a pattern")
@click.option("--show_values/--hide_values", "-s", help="Show/hide values mathing a pattern")
@click.option("--pattern", "-p", type=str, help="Regular expression for references")
def references(board, show, showValues,pattern):
    """
    Show or hide references on the board matching a pattern.
    """
    from kikit import modify
    b = modify.pcbnew.LoadBoard(board)
    modify.x(b, show, showValues, pattern)
    b.Save(board)

@click.group()
def modify():
    """
    Modify board items
    """
    pass

modify.add_command(references)