"""
This example demonstrates the justify argument to print.
"""

from rich.console import Console
from rich.panel import Panel

console = Console(width=20)

style = "bold white on blue"
panel = Panel("Rich", style="on red", expand=False)
console.print(panel, =style)
console.print(panel, =style, justify="left")
console.print(panel, =style, justify="center")
console.print(panel, =style, justify="right")
