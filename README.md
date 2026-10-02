# Hazardous Near-Earth Objects (NEOs)

This repository contains an exploratory notebook for classifying whether a near-Earth object (NEO) is labeled hazardous in the referenced dataset. It is a machine-learning exercise, not an operational planetary-defense system.

## Repository contents

- `Project_NEOs.ipynb` — exploratory data analysis and several baseline model experiments.
- `NASA_Data.txt` — URL to the dataset source; it is not a copy of the data.

The CSV dataset is **not included** in this repository. No model artifact or independently verified performance result is provided.

## Obtain the dataset

1. Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/ivansher/nasa-nearest-earth-objects-1910-2024/data) and obtain the CSV according to Kaggle's access and data-use terms.
2. Save the downloaded file in the repository root with this exact name: `nearest-earth-objects(1910-2024).csv`.
3. Do not commit Kaggle credentials, API tokens, or private account configuration. This project does not require credentials embedded in the notebook.

The notebook checks for the expected local file and raises an explanatory error if it is absent.

## Run the notebook

Use Python with Jupyter and the libraries imported by the notebook: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, and `imbalanced-learn`.

For example, in a fresh Python environment:

```bash
python -m pip install jupyter pandas numpy matplotlib seaborn scikit-learn imbalanced-learn
jupyter notebook Project_NEOs.ipynb
```

Run Jupyter from the repository root so the relative dataset path resolves. The repository does not currently pin dependency versions; results can vary with package versions. Restart the kernel and run cells in order after obtaining the dataset.

## Limitations

- The source CSV is absent, so a clean checkout cannot run the analysis end-to-end without a manual download.
- The notebook contains exploratory, incrementally developed experiments. Its saved cell outputs have been cleared; reported metrics must be regenerated and reviewed against the downloaded data and current environment.
- This repository does not provide a validated model, a production inference workflow, or evidence that any reported performance generalizes beyond the notebook's train/test split. In particular, accuracy alone is not sufficient for judging hazardous-object detection.
- No test suite or data-validation pipeline is currently included.
