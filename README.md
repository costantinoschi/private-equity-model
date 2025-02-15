
# Private Equity Model

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)

A comprehensive Python-based financial modeling template designed for private equity transactions. This model integrates Discounted Cash Flow (DCF) analysis, Leveraged Buyout (LBO) metrics, sensitivity analysis, and operating leverage effects to evaluate investment scenarios.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This project simulates key aspects of private equity deals. By adjusting assumptions such as revenue growth, EBITDA margin, debt structure, and exit multiples, you can assess impacts on enterprise and equity value, as well as calculate LBO metrics like MOIC (Multiple on Invested Capital) and IRR (Internal Rate of Return). The model includes robust sensitivity analyses to help you explore different operating leverage scenarios.

## Features

- **Dynamic Financial Modeling:** Forecast revenue, EBITDA, and free cash flows over a multi-year horizon.
- **LBO Return Metrics:** Calculate MOIC and IRR based on sponsor equity investment.
- **Sensitivity Analysis:** Evaluate how changes in revenue growth, exit multiples, and fixed cost levels affect key metrics.
- **Operating Leverage Assessment:** Analyze the impact of varying fixed costs on overall performance.
- **Customizable Parameters:** Easily adjust assumptions to simulate different deal scenarios.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/private-equity-model.git
   cd private-equity-model

2. **Install required Python packages:**

This model requires Python 3.8+ and the following libraries:
`numpy`
`pandas`

Install them via pip:

`pip install numpy pandas`

## Usage
Run the model directly from the command line. The main code is in `PrivateEquityModel.py`.

Example:

`python PrivateEquityModel.py`

The script includes sample usage with default parameters. Feel free to modify the parameters in the code or create a configuration file for enhanced flexibility.

## Model Details

The function private_equity_model accepts parameters such as:
- `revenue_growth`: Annual revenue growth rate.
- `ebitda_margin`: EBITDA margin (as a decimal).
- `depreciation_rate`: Depreciation rate.
- `capex_ratio`: Capital expenditures as a fraction of revenue.
- `nwc_ratio`: Change in net working capital as a fraction of revenue.
- `tax_rate`: Corporate tax rate.
- `discount_rate`: Discount rate for DCF calculations.
- `exit_multiple`: Exit multiple for valuation.
- `debt_ratio`: Initial debt as a percentage of revenue.
- `interest_rate`: Interest rate on debt.
- `repayment_schedule`: Dictionary specifying debt repayments per year.
- `years`: Forecast period (default is 5 years).
- `entry_multiple`: Entry multiple for initial equity valuation.
- `sponsor_equity`: Sponsor equity percentage.
- `fixed_costs_ratio`: Fixed costs as a percentage of revenue.

It returns key metrics including:

- Enterprise Value
- Equity Value
- NPV of Cash Flows
- Discounted Terminal Value
- Annual Free Cash Flows
- LBO metrics: MOIC and IRR
- Detailed sensitivity analysis outputs

## Contributing
Contributions are welcome! Please fork the repository and submit a pull   request. For major changes, open an issue first to discuss your ideas.

## License
This project is licensed under the **MIT License**. See the **LICENSE** file for more details.

## Contact
For questions or feedback, please contact Your Name.
