# src/plot_utils.py

import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

def find_project_root(marker_file="README.md"):
    """
    Traverse up the directory tree until we find the marker_file (default: 'README.md').
    """
    current_path = Path.cwd()
    for parent in [current_path] + list(current_path.parents):
        if (parent / marker_file).exists():
            return parent
    raise FileNotFoundError(f"Could not find {marker_file} in any parent directories of {current_path}")

def save_plot(filename: str, subfolder: str = "", dpi: int = 300):
    """
    Save the current matplotlib plot to outputs/visuals/<subfolder>/<filename>,
    relative to project root, regardless of notebook/script location.
    """
    project_root = find_project_root()
    output_dir = project_root / "outputs" / "visuals" / subfolder
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / filename
    plt.savefig(file_path, dpi=dpi, bbox_inches="tight")
    print(f"Plot saved to: {file_path}")

def save_text_output(content, filename: str, subfolder: str = ""):
    """
    Save textual content (e.g., string, list of strings, or pandas DataFrame) to outputs/textual/<subfolder>/<filename>,
    relative to project root.

    Parameters:
    - content: str | list[str] | pd.DataFrame
    - filename: Name of the file to save (e.g., 'top_clutch.txt' or 'summary.csv')
    - subfolder: Optional subfolder within 'outputs/textual'
    """
    project_root = find_project_root()
    output_dir = project_root / "outputs" / "textual" / subfolder
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / filename

    if isinstance(content, pd.DataFrame):
        if filename.endswith(".csv"):
            content.to_csv(file_path, index=False)
        else:
            content.to_string(buf=open(file_path, "w"))
    elif isinstance(content, (str, list)):
        with open(file_path, "w", encoding="utf-8") as f:
            if isinstance(content, list):
                f.write("\n".join(content))
            else:
                f.write(content)
    else:
        raise TypeError("Unsupported content type. Provide str, list of str, or pandas DataFrame.")

    print(f"Textual output saved to: {file_path}")
