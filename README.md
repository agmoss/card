<!DOCTYPE html>
<html>
	<head>
		<style>
			#card {
			width: 100%;
			max-width:400px;
            height:auto;
			}
		</style>
	</head>
	<body>
		<h1 align="center">Card</h1>
		<div align="center" >
			<img id="card" src="./dist/card.png" alt="Logo" />
		</div>
		<div align="center">
			<i>Generative Art Business Card</i>
		</div>
		<br />
		<div align="center">
			<!-- Dependencies -->
			<a>
			<img src="https://img.shields.io/david/agmoss/m0ss" alt="Dependencies" />
			</a>
			<!-- Size -->
			<a>
			<img src="https://img.shields.io/github/languages/code-size/agmoss/card" alt="Code Size" />
			</a>
			<!-- Style -->
			<a>
			<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
			</a>
			<!-- Pylint -->
			<a>
			<img alt="Pylint Score" src="./dist/pylint.svg">
			</a>
			<!-- Language -->
			<a>
			<img alt="language" src="https://img.shields.io/github/languages/top/agmoss/card">
			</a>
			<!-- Language -->
			<a>
			<img alt="Python3.7" href="https://www.python.org/downloads/release/python-373/" src="https://img.shields.io/badge/python-3.7.3-blue.svg">
			</a>
			<!-- License -->
			<a>
			<img alt="license" src="https://img.shields.io/github/license/agmoss/card">
			</a>
		</div>
		<br />
		<div align="center">
			<sub>Built by
			<a href="https://github.com/agmoss">Andrew Moss</a>
		</div>
		<br />
	</body>
</html>

## Code

```python
"""Card"""
import numpy as np
import scipy.special
import matplotlib.cm as cm
import matplotlib.pyplot as plt

if __name__ == "__main__":

    FIG, AX = plt.subplots()
    FIG.set_size_inches(3.5, 2, forward=True)

    # Remove the plot frame lines
    AX.spines["top"].set_visible(False)
    AX.spines["bottom"].set_visible(True)
    AX.spines["right"].set_visible(False)
    AX.spines["left"].set_visible(True)

    # Text
    AX.text(
        45,
        0.7,
        "Andrew Moss",
        fontsize=14,
        style="oblique",
        horizontalalignment="right",
        weight="bold",
    )
    AX.text(45, 0.45, "W: m0ss.dev", fontsize=8, horizontalalignment="right")
    AX.text(45, 0.32, "E: andrew@m0ss.dev", fontsize=8, horizontalalignment="right")
    AX.text(45, 0.16, "P: 403 690 2015", fontsize=8, horizontalalignment="right")

    # Plot Chi square survival function
    CMAP = cm.get_cmap("winter")
    COLOR = iter(CMAP(np.linspace(0, 1, 10)))
    X = np.linspace(0, 50, 500)
    for i in range(10):
        c = next(COLOR)
        AX.plot(X, scipy.special.chdtrc(i, X), c=c)

    FIG.tight_layout(pad=0.5)
    plt.savefig("./dist/card.png", bbox_inches="tight", pad_inches=0, dpi=900)
    plt.show()
```
