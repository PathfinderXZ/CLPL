# Chemistry Lab Python Library (CLPL) v1.2

CLPL is a specialized script library tailored for chemists, offering essential tools for simplifying daily laboratory
operations.

## Overview
All units in CLPL are referenced to grams.
### Labtools
The Labtools module contains a collection of scripts designed to automate routine laboratory tasks.

#### Molar Mass Calculation
The Molar Mass script computes the molar mass of a molecule based on its formula. It accommodates organic chemistry
groups such as i-PrOH, PhOTs, Et2S, NEt3, etc., if specified in the configuration. This creates a potential conflict
between the "Ac" symbol representing both the acetate group and actinium. Optionally, it can provide molar masses of
common laboratory reagents and solvents like DMSO, THF, NHS, DEAD, LDA, and more.

#### Reagent Scaling
The Scale Reagents script offers straightforward mathematical functionality to scale up or down the quantities of
reagents in a reaction.

#### Yield Computation
The Yields script facilitates the computation of theoretical and percentage yields based on the limiting reagent of a reaction.

#### Safety sheet lookup
The Safety sheet lookup script utilizes the Google Custom Search Engine to retrieve safety data sheets for specified substances. It automatically opens the relevant safety sheets in a browser.

## Installation and Setup

1. Ensure you have a functional Python interpreter (3.7+) and pip.
2. Create python virtual env (optional).
3. In the folder `/CLPL` run `pip install requirements.txt` to install the necessary dependencies
4. Some modules within CLPL may require individual setup steps due to the safeguarding of private API keys and
customization based on personal preferences.

### Initial Configuration Steps

After downloading CLPL, follow these steps:

1. Rename the `env.templ` file located in the `/config` directory to `.env`. This renaming is crucial for the program to identify the configuration file.

### Molar Mass Module Configuration

In the `.env` file located in the `/config` directory:

- Set the organic mode variable to either `True` or `False`, based on your preference.
- Note: Organic mode's drawback is the inability to differentiate between "Ac" (Actinium) and "Ac" (acetate). If needed, change the acetate symbol to an alternative that avoids collisions (e.g., "ac"). By default, organic group functionality is disabled.

### Safety Module Configuration

For the Safety module, you'll need to generate your own Google API key and Google Custom Search Engine key. 
Refer to this guide: [Google search engine API Key Generation](https://www.youtube.com/watch?v=TddYMNVV14g). Then, paste the generated values 
into the `.env` file.

## Contribution

All contributions are welcome. If you would like to contribute, feel free to create a pull request. Note that CLPL is not yet available on PyPI.

## License

CLPL is distributed under the GNU GPL 3. For detailed information, refer to the LICENCE file.