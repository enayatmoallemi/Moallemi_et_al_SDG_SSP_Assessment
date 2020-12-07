# Source model files and their required input spreadsheets for running in Vensim or Python.

The folder contains the following files:
* FeliX3_SDGs_v38.mdl: This is the Venism original model file to be used for simulation within Vensim.
* FeliX3_SDGs_v38.vpmx: This is the Venism model package file to be used by Python when running the model e.g. through the EMA workbench.
* 'InitialValues.xlsx': This lists some of the input data (e.g., the initial value of stock variables) to the Vensim model.
* 'New_DietData.xlsx': This lists some of the input data (diet change) to the Vensim model.
* 'TotalPopulationbyAge.xlsx': This lists some of the input data (education) to the Vensim model.
* 'ScenarioFramework.xlsx': This contains essential input data used in running codes. It's not needed when you open the model directly in Vensim.
* `SSP1.vdfx` to `SSP5.vdfx`: They list the SSP 1 to SSP 5 projected data from the IIASA Database with the SSP 1 to SSP 5 marker model to be used for calibration.

The 'ScenarioFramework.xlsx' file includes the following tabs:
* 'Outcomes': These are the list of outcome variables used in sensitivity analysis and model calibration.
* 'Uncertainties': This lists the initial uncertain socioeconomic parameters in FeliX used for sensitivity analysis.
* 'Important_Uncertainties': This lists the important uncertain socioeconomic parameters in FeliX identified through sensitivity analysis. They were parameters eventually used in calibration of the model under SSPs.
* 'Correlation_analysis': This lists a summary of the correlation analysis conducted to identify the number of top important parameters.
* 'SSP_parameters_assumptions': This lists the variation rate of model parameters from BAU assumptions according to the narratives of the SSPs scenarios also informed by projections in IIASA database.
* 'SSP_parameters_values': This lists the actual quantitative values of parameters across the SSPs, calculated based on the variation rate in the previous tab.
* 'Exploratory_analysis_constants': This lists the values of the model parameters under each SSP from the previous tab that we did not vary in exploratory analysis.
* 'Exploratory_analysis_SSP1' to 'Exploratory_analysis_SSP': They list the uncertainty ranges of model parameters for SSP 1 to SSP 5.
* 'SDG_indicator_metadata': This is the metadata tab for indicator target setting with almost all necessary information and links to other tabs .
* 'SDG_indicator_target': This is a summary of SDG_indicator_metadata for those indicators with targets and included in the current version of analysis to be read in codes.
