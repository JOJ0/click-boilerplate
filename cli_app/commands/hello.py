import click

from cli_app.config import valid_conf


@click.command()
@click.argument('name', nargs=1)
def hello(name):
    """
    Simple command that says hello
    """
    click.echo(f'Hello {name}')
