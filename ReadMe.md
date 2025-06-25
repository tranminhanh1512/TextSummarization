# TextSummarizer Using HuggingFace
This project implements a complete text summarization pipeline using Hugging Face's Transformers, designed for modularity, scalability, and ease of deployment. The system is trained to generate concise and accurate summaries from dialogues or text passages, leveraging state-of-the-art transformer models like Pegasus, fine-tuned on the SAMSum dataset. The architecture includes all key ML pipeline stages—data ingestion, transformation, training, evaluation, and inference—exposed via a user-friendly FastAPI interface. The project is also containerized using Docker and integrated with GitHub Actions to support Continuous Integration and Continuous Delivery (CI/CD).

## Workflows

1. Config.yaml
2. Params.yaml
3. Config Entity
4. Configuration Manager
5. Update the components - Data Ingestion, Data Transformation, Model Trainer
6. Create our Pipeline - Training Pipeline, Prediction Pipeline
7. Front End - API's, Training API's, Batch Prediction API's

### Project Structure
```
TextSummarization
├── app.py                          # FastAPI application with training and prediction endpoints
├── config
│   └── config.yaml                 # Configuration for directory paths and project settings
├── Dockerfile                      # Docker image specification for deployment
├── logs
│   └── continous_logs.log          # Output log for pipeline processes
├── main.py                         # Main script to run the full training pipeline
├── params.yaml                     # Hyperparameter and preprocessing configuration
├── ReadMe.md                       # Project overview, usage guide, and instructions
├── requirements.txt                # Python package dependencies
├── research                        # Jupyter notebooks for each pipeline stage
│   ├── 1_data_ingestion.ipynb      # EDA and ingestion experiments for SAMSum dataset
│   ├── 2_data_transformation.ipynb # Tokenization and input formatting trials
│   ├── 3_model_trainer.ipynb       # Model training experiments using Pegasus
│   ├── 4_model_evaluation.ipynb    # Evaluate summaries with ROUGE and compare outputs
│   ├── research.ipynb              # General research and observations
│   └── textsummarizer.ipynb        # Summary demo and integration notes
├── setup.py                        # Install project as a pip module for import
├── src
│   └── TextSummarization
│       ├── components
│       │   ├── data_ingestion.py       # Module to download, read, and structure dataset
│       │   ├── data_transformation.py  # Converts raw data to tokenized format
│       │   ├── model_evaluation.py     # Measures performance with ROUGE metrics
│       │   └── model_trainer.py        # Fine-tunes transformer model on dataset
│       ├── config
│       │   └── configuration.py        # Class to parse and load YAML configurations
│       ├── constants                   # Global static values used across modules
│       ├── entity                      # Data schema definitions for component I/O
│       ├── logging                     # Centralized logging configuration
│       ├── pipeline
│       │   ├── prediction_pipeline.py              # Inference logic for summarization
│       │   ├── stage_1_data_ingestion_pipeline.py  # Triggers ingestion component
│       │   ├── stage_2_data_transformation_pipeline.py # Triggers transformation logic
│       │   ├── stage_3_model_trainer_pipeline.py   # Handles training orchestration
│       │   └── stage_4_model_evaluation_pipeline.py # Executes evaluation logic
│       └── utils
│           └── common.py              # Utility functions shared across modules
└── template.py                     # Template structure or reference for model I/O

```
## Set Up Instruction

### 1. Clone the repository
```
git clone https://github.com/<your-username>/TextSummarization.git
cd Text Summarization
```
### 2. Create a Virtual Environment & Install dependencies
```
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
```
### 3. Run the application in your local machine
```
python app.py
```
You access the API documentation at http://127.0.0.1:8000.

## Docker Instructions
### 1. Build Docker Image
```
docker build -t text-summarization .
```
### 2. Run Docker Container
```
docker run -d -p 8000:8000 --env-file .env text-summarization
```
## AWS Continuous Integration and Continuous Delivery with Github Actions Instructions
### 1. Login to AWS console.
### 2. Create IAM user for deployment
#### With specific access
1. EC2 access : It is virtual machine
2. ECR: Elastic Container registry to save your docker image in aws
#### Description: About the deployment
1. Build docker image of the source code
2. Push your docker image to ECR
3. Launch Your EC2 
4. Pull Your image from ECR in EC2
5. Lauch your docker image in EC2
#### Policy:
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess
### 3. Create ECR repo to store/save docker image
### 4. Set up Github Secrets
```
AWS_ACCESS_KEY_ID = your_acess_key_id
AWS_SECRET_ACCESS_KEY = your_access_key
AWS_REGION = your_region
ECR_REPOSITORY_NAME = your_ecr_repo_name
```
### 8.  Push Code to GitHub

## Key Components
### 1. Data Ingestion
- Loads and preprocesses the SAMSum dataset, a high-quality resource for training dialogue summarizers.
- Performs cleaning, normalization, and structured storage.
### 2. Data Transformation
- Uses Hugging Face’s tokenizer to convert raw text into token IDs.
- Applies preprocessing steps like attention masks for model compatibility.
### 3. Model Training
- Fine-tunes a pre-trained Pegasus model on the dataset using efficient training strategies (e.g., early stopping, gradient accumulation).
- Supports configurable training parameters and logging.
- Stores the trained model and tokenizer artifacts for deployment.
### 4. Model Evaluation
- Evaluates model output using ROUGE scores, a standard for summarization tasks.
- Logs metrics for monitoring and experimentation.
### 5. Prediction Pipeline
- Loads the fine-tuned model and generates summaries from new text inputs.
- Supports both real-time and batch prediction modes.
### 6. FastAPI Interface
- Provides RESTful endpoints for:
  - GET /train: Triggering training via API.
  - POST /predict: Submitting text and receiving generated summaries.
- Allows easy integration into applications or frontend interfaces.
### 7. Containerization with Docker
- Encapsulates the entire pipeline in a Docker image for consistent runtime behavior across systems.
- Simplifies local testing, deployment to cloud, or orchestration platforms like Kubernetes.
### 8. Continuous Integration and Continuous Delivery (CI/CD)
- GitHub Actions workflow automates the entire development lifecycle:
- Linting and static checks to ensure code quality.
- Automated testing of model training and prediction logic.
- Container build and push to registries like Docker Hub or AWS ECR.
- Deployment triggers for updating live applications on EC2, ECS, or similar platforms.
- Ensures that every code push to main is validated, tested, and ready for production.
## Technologies Used
- **Python**: Core programming language.
- **FastAPI**: Web framework for API development.
- **Hugging Face Transformers**: Library for pre-trained models and tokenizers.
- **Docker**: Containerization for deployment.
- **GitHub Actions**: Automates CI/CD pipelines.
- **Jupyter Notebooks**: Research and experimentation.
- **PyYAML**: Configuration management.
## Test Validation
| Metric     | Score                 |
|------------|-----------------------|
| ROUGE-1    | 0.020833008179609033  |
| ROUGE-2    | 0.000000000000000000  |
| ROUGE-L    | 0.020791843247882455  |
| ROUGE-Lsum | 0.020770536317329953  |
## Test Prediction
**Input**: Elara, a young squirrel known for her cleverness, was diligently collecting nuts for the coming winter. She carefully sorted them, burying some in easy-to-remember locations and hiding others in less obvious spots. One day, a grasshopper named Finley mocked her efforts, saying, "Why toil so hard? Enjoy the sunshine! There's plenty of time before winter." Elara, though amused, continued her work. When winter arrived, Finley, shivering and hungry, sought shelter and food. Elara, having prepared well, was warm and well-fed in her cozy nest. She shared some of her stored nuts with Finley, who learned a valuable lesson about the importance of preparing for the future.

**Output**
<img width="1412" alt="Screenshot 2025-06-25 at 00 09 05" src="https://github.com/user-attachments/assets/7f10f862-9825-4edd-9a75-989ff966e9d8" />


