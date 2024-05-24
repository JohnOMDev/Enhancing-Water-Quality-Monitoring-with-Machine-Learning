# Water Potability Prediction

## Project Summary

This project aims to develop a robust classification model to predict the potability of water samples based on various chemical properties. By leveraging machine learning techniques and addressing class imbalances through methods like SMOTE (Synthetic Minority Over-sampling Technique), we provide a tool that enhances water quality monitoring and decision-making for the city council. The ultimate goal is to promote public health by ensuring the safety of the drinking water supply through early identification of potential contamination.

## Goals

1. **Develop a Predictive Model**:
   - Create a reliable classification model to predict water potability based on chemical properties.

2. **Improve Water Quality Monitoring**:
   - Provide a tool for the city council to monitor water quality more effectively.

3. **Enhance Decision-Making**:
   - Enable data-driven decisions regarding water safety and resource allocation.

4. **Promote Public Health**:
   - Ensure the safety of the drinking water supply by identifying potential contamination early.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Virtual environment tools (venv)

### Installation

Follow these steps to set up the project:

1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the requirements**:
   ```sh
   make install
   ```

### Usage

To run the inference script and make predictions on the test data, use the following command:

```sh
make run
```

### Makefile Commands

The `Makefile` provides several useful commands for setting up and managing the project:

- **install**: Set up the virtual environment and install the required dependencies.
  ```sh
  make install
  ```
  
- **format**: Format the Python scripts using `black`.
  ```sh
  make format
  ```

- **lint**: Lint the Python scripts using `flake8`.
  ```sh
  make lint
  ```

- **security**: Check the Python scripts for security issues using `bandit`.
  ```sh
  make security
  ```

- **clean**: Remove the virtual environment and any compiled Python files.
  ```sh
  make clean
  ```

- **run**: Execute the inference script with the model, scaler, and test data.
  ```sh
  make run
  ```

- **all**: Run all the above commands in sequence (install, format, lint, security, clean, run).
  ```sh
  make all
  ```

### File Structure

- `inference.py`: The main script to run the water potability prediction.
- `requirements.txt`: List of dependencies required for the project.
- `model/water-potability.pkl`: Pre-trained model for predicting water potability.
- `scaler/scaler.pkl`: Scaler used for data normalization.
- `data/test_data_water_potability.csv`: Sample test data for inference.

## Conclusion

This project provides a comprehensive solution for predicting the potability of water samples, enhancing water quality monitoring, and promoting public health. The developed model, particularly the Random Forest classifier, demonstrated robust performance after addressing class imbalances using SMOTE. By integrating this model into the city's water quality monitoring system, we can ensure safer drinking water and enable informed decision-making for resource management.
