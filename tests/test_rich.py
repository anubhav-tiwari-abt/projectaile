import rich

# ---------------------- print ----------------------

# normal print
rich.print('Whats up!?')

# print with styling
rich.print('[bold red]What\'s up?![/]')


# ---------------------- console API ----------------------

console = rich.console.Console()

# normal print
console.print('What is up there?')

# normal print with style
console.print('What is [red]up[/] there?', style='blink bold red underline on white')

# logging with time and file name
console.log('[bold red]Exception : [/] Something wen\'t wrong!!')

# ---------------------- status ----------------------

# separation of terminal with rule (horizontal line)
console.rule('[bold magenta] Status Demo [/]')

# status (progress)
with console.status('Loading libraries...'):
    import time
    time.sleep(2)
    console.log('[bold green]Done![/]')

# status with different spinners
# Run python -m rich.spinner for all spinners (CAUTION!! it goes in infinite loop)
with console.status('Initializing Pipelines...', spinner='point'):
    import time
    time.sleep(2)
    console.log('[bold green]Done![/]')
    
with console.status('Running Pipelines...', spinner='runner'):
    import time
    time.sleep(2)
    console.log('[bold green]Done![/]')

console.log('Finished Processing!', style='bold green')


# ---------------------- overflow texts ----------------------
console.rule('[bold magenta] Overflow Demo [/]')

console_narrow = rich.console.Console(width=14)
string = 'Stupendofantabuloslyphantasmagoricallymagical!'

console_narrow.rule('[green]fold[/]')
console_narrow.print(string, overflow='fold')
console_narrow.rule('[green]crop[/]')
console_narrow.print(string, overflow='crop')
console_narrow.rule('[green]ellipsis[/]')
console_narrow.print(string, overflow='ellipsis')

# ---------------------- i/o demos ----------------------
console.rule('[bold magenta] I/O Demo [/]')
# getting user input
name = console.input('What is [i]your[/i] [bold red]name[/]? :smiley: ')
console.print(f'Well [i]Helloo!![/] there [bold red]{name}[/]')

# writing logs to output file
console_out = rich.console.Console(record=True)
job = console_out.input(f'What do you [i]do[/i] [bold red]{name}[/]? :smiley: ')
console_out.print(f'Wow [i]{job}!![/] that sounds [bold red]amazing[/] 🎉')
# console_out.save_html('out.html')

# ---------------------- theming ----------------------
console.rule('[bold magenta] Theming Demo [/]')
custom_theme = rich.theme.Theme({
    "info" : "green",
    "warning": "yellow",
    "danger": "bold red"
})
console_themed = rich.console.Console(theme=custom_theme)
console_themed.print("This is information", style="info")
console_themed.print("[warning]The pod bay doors are locked[/warning]")
console_themed.print("Something terrible happened!", style="danger")


# ---------------------- links ----------------------
console.rule('[bold magenta] Links Demo [/]')
console.print('Visit My [link=https://github.com/abtExp]GitHub :cat:[/] for more')


# ---------------------- pretty printing ----------------------
console.rule('[bold magenta] Pretty Printing Demo [/]')

rich.pretty.pprint({
    'name' : 'Anubhav',
    'job' : 'ML Research Engineer',
    'quirks' : 'Lazy AF',
    'age' : 24,
    'skills' : ['python', 'tf', 'pytorch'],
    'is_fun' : False,
    'other_stuff':{
        'hobbies' : 'non_existent'
    }
}, expand_all=True)

# ---------------------- errors, exceptions and tracebacks ----------------------

console.rule('[bold magenta] Errors, Exceptions And Tracebacks Demo [/]')

import logging
from rich.logging import RichHandler

# setting as default logging handler
logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

log = logging.getLogger("rich")
try:
    print(1 / 0)
except Exception:
    log.exception("unable print!")
    
# case wise logging
try:
    a = 1/0
except Exception as e:
    console.print_exception(show_locals=True)
    
# ---------------------- prompt for input ----------------------
console.rule('[bold magenta] Prompts Demo [/]')

from rich.prompt import Prompt as prompt, Confirm as confirm

# text prompt
prompt_name = prompt.ask('WHAT IS YOUR NAME??')

# text prompt with default value
prompt_mind = prompt.ask('What is on your mind?', default='Nothing')

# choice prompt with default value
prompt_choice = prompt.ask('Favorite [red]c[/][blue]o[/][green]l[/][magenta]o[/][yellow]r[/]?', choices=['red', 'green', 'blue'], default='blue')

# confirmation prompt
prompt_answer = confirm.ask('Are you done?')


# ---------------------- column display ----------------------
console.rule('[bold magenta] Column Demo [/]')

import os
import sys
from rich.columns import Columns

if len(sys.argv) < 2:
    console.print("Usage: python columns.py DIRECTORY")
else:
    directory = os.listdir(sys.argv[1])
    columns = Columns(directory, equal=True, expand=True)
    console.print(columns)

# ---------------------- groups and panels ----------------------
console.rule('[bold magenta] Panel And Group Demo [/]')

from rich.panel import Panel

# normal panel display
console.print(Panel('Hellow There [red]Maestro!![/]', title='Greetings Human!'))

# fit panel width to content
console.print(Panel('Hellow There [red]Maestro!![/]', title='Greetings Human!', expand=False))

# different box style
console.print(Panel('Hellow There [red]Maestro!![/]', title='Greetings Human!', expand=False, box=rich.box.SIMPLE_HEAVY))

# grouping
from rich.console import Group

panel_group = Group(
    Columns([
        Panel('Hellow There [red]Maestro!![/]', title='Greetings Human', expand=False),
        Panel('Hellow There [red]Monster!![/]', title='Greetings Animal', expand=False)
    ], equal=True, expand=True)
)

console.print(Panel(panel_group, title='Different Greetings'))

# ---------------------- markdown ----------------------
console.rule('[bold magenta] Markdown Demo [/]')

md_txt = """
    # Let's test Markdown
    ####### Here's some stuff
    * Name : Anubhav
    * Classy : Yes
"""

from rich.markdown import Markdown
console.print(Markdown(md_txt))

# ---------------------- progressbar ----------------------
console.rule('[bold magenta] Progressbar Demo [/]')

from rich.progress import track, Progress

# simple loop tracking
import numpy as np
import time

loop_arr = np.random.random((1000))

for a in track(loop_arr, description='Reading...'):
    pass

# using progress object
with Progress() as prog:
    data_loader = prog.add_task('[red]Loading Data...', total=100)
    model_training = prog.add_task('[green]Training...', total=100)
    
    while not prog.finished:
        prog.update(data_loader, advance=0.5)
        prog.update(model_training, advance=0.1)
        time.sleep(0.01)
        
# hiding after completion (transient) and starting after sometime
with Progress(transient=True) as prog:
    data_loader = prog.add_task('[red]Loading Data...', total=100, start=False)
    model_training = prog.add_task('[green]Training...', total=100, start=False)
        
    time.sleep(2)
    prog.start_task(data_loader)
    
    while not prog.tasks[data_loader].finished:
        prog.update(data_loader, advance=0.5)
        time.sleep(0.01)
    
    prog.start_task(model_training)
    while not prog.tasks[model_training].finished:
        prog.update(model_training, advance=0.2)
        time.sleep(0.01)
        
console.print('Done Training.!')

# ---------------------- syntax highlighting ----------------------
console.rule('[bold magenta] Syntax Highlighting Demo [/]')

from rich.syntax import Syntax

with open('C:/Users/abtex/Desktop/projectaile/tests/prototypes/sample_usage.py', 'rt') as f:
    syntax = Syntax(f.read(), 'python', line_numbers=True, indent_guides=True)
    
console.print(syntax)

# ---------------------- tables ----------------------
console.rule('[bold magenta] Tables Demo [/]')

from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console.print(table)

# ---------------------- tree ----------------------
console.rule('[bold magenta] Tree Demo [/]')

import pathlib
from rich.tree import Tree
from rich.text import Text
from rich.markup import escape
from rich.filesize import decimal

def walk_directory(directory: pathlib.Path, tree: Tree) -> None:
    """Recursively build a Tree with directory contents."""
    # Sort dirs first then by filename
    paths = sorted(
        pathlib.Path(directory).iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    for path in paths:
        # Remove hidden files
        if path.name.startswith("."):
            continue
        if path.is_dir():
            style = "dim" if path.name.startswith("__") else ""
            branch = tree.add(
                f"[bold magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
                style=style,
                guide_style=style,
            )
            walk_directory(path, branch)
        else:
            text_filename = Text(path.name, "green")
            text_filename.highlight_regex(r"\..*$", "bold red")
            text_filename.stylize(f"link file://{path}")
            file_size = path.stat().st_size
            text_filename.append(f" ({decimal(file_size)})", "blue")
            icon = "🐍 " if path.suffix == ".py" else "📄 "
            tree.add(Text(icon) + text_filename)
            
try:
    directory = os.path.abspath(sys.argv[1])
except IndexError:
    print("[b]Usage:[/] python tree.py <DIRECTORY>")
else:
    tree = Tree(
        f":open_file_folder: [link file://{directory}]{directory}",
        guide_style="bold bright_blue",
    )
    walk_directory(pathlib.Path(directory), tree)
    console.print(tree)