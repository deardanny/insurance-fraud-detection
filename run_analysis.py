"""Execute the public analysis in this Python environment; write outputs locally."""
from pathlib import Path
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager


def main():
    root = Path(__file__).resolve().parent
    notebook_path = next((root / 'notebooks').glob('*.ipynb'))
    output = root / 'outputs'
    output.mkdir(exist_ok=True)
    notebook = nbformat.read(notebook_path, as_version=4)
    manager = KernelManager(kernel_name='python3')
    manager.kernel_spec.argv = [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}']
    def progress(cell, cell_index, **kwargs):
        if cell.cell_type == 'code':
            print(f'Running cell {cell_index}', flush=True)
    client = NotebookClient(notebook, km=manager, timeout=1800,
                            resources={'metadata': {'path': str(root)}}, on_cell_start=progress)
    client.execute()
    target = output / notebook_path.name
    nbformat.write(notebook, target)
    print(f'Completed: {target}')


if __name__ == '__main__':
    main()
