"""
materials_analysis.py
----------------------
A pandas-based companion to the Alloy Atlas web app.

What it does:
1. Loads the materials dataset (materials_data.csv)
2. Computes derived engineering metrics:
      - specific strength   = yield_strength / density   (useful for weight-critical design, e.g. aerospace)
      - specific stiffness   = modulus / density
3. Prints category-wise summary statistics (mean property by material class)
4. Ranks materials by specific strength and specific stiffness
5. Saves a bar chart comparing specific strength across materials (specific_strength.png)

Run with:
    pip install pandas matplotlib --break-system-packages   # if not already installed
    python materials_analysis.py
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "materials_data.csv"


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["specific_strength"] = df["yield_strength_MPa"] / df["density_g_cm3"]
    df["specific_stiffness"] = df["modulus_GPa"] / df["density_g_cm3"]
    return df


def category_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("category")[
            ["density_g_cm3", "yield_strength_MPa", "modulus_GPa", "specific_strength"]
        ]
        .mean()
        .round(2)
        .sort_values("specific_strength", ascending=False)
    )


def top_n(df: pd.DataFrame, column: str, n: int = 5) -> pd.DataFrame:
    return df.sort_values(column, ascending=False)[["name", "category", column]].head(n)


def plot_specific_strength(df: pd.DataFrame, out_path: str = "specific_strength.png") -> None:
    ranked = df.sort_values("specific_strength", ascending=False)

    category_colors = {
        "Ferrous": "#a8b0b8",
        "Light Alloy": "#6fa89e",
        "Copper Alloy": "#c97c3d",
        "Polymer": "#d9b45f",
        "Ceramic": "#c77b83",
        "Composite": "#8e8fd9",
    }
    colors = ranked["category"].map(category_colors)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.barh(ranked["name"], ranked["specific_strength"], color=colors)
    ax.invert_yaxis()
    ax.set_xlabel("Specific strength  (MPa per g/cm³)")
    ax.set_title("Specific Strength Ranking — Alloy Atlas Dataset")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    print(f"\nSaved chart to {out_path}")


def main() -> None:
    df = load_data(DATA_FILE)

    pd.set_option("display.width", 120)

    print("=" * 60)
    print("CATEGORY-WISE AVERAGE PROPERTIES")
    print("=" * 60)
    print(category_summary(df))

    print("\n" + "=" * 60)
    print("TOP 5 BY SPECIFIC STRENGTH (best for weight-critical strength applications)")
    print("=" * 60)
    print(top_n(df, "specific_strength").to_string(index=False))

    print("\n" + "=" * 60)
    print("TOP 5 BY SPECIFIC STIFFNESS (best for weight-critical rigidity applications)")
    print("=" * 60)
    print(top_n(df, "specific_stiffness").to_string(index=False))

    plot_specific_strength(df)


if __name__ == "__main__":
    main()
