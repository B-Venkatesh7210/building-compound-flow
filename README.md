# Building Compound Flows

This repository demonstrates how to use the **Mira SDK** to build, deploy, and manage compound flows on the Mira Marketplace. Compound flows enable the integration of multiple individual flows into a cohesive workflow, providing enhanced flexibility and reusability for complex processes.

---

## **Features**
- Initialize the Mira SDK client with an API key.
- Build and deploy compound flows that combine multiple elemental flows.
- Execute compound flows with dynamic user inputs.
- Retrieve and manage compound flow details and metadata.
- Securely manage sensitive data using environment variables.

---

## **Prerequisites**
1. **Mira Account**: Ensure you have created an account at [Mira Marketplace](https://console.mira.network/).
2. **API Key**: Generate an API Key from your [Mira Account Dashboard](https://console.mira.network/account/api-keys).
3. **Python**: Ensure you have Python version >3.9.0 and <3.13.0 installed.
4. **Dependencies**: Install the required libraries using the steps in the **Setup** section.

---

## **Setup**

### 1. Clone the Repository
```bash
git clone https://github.com/B-Venkatesh7210/building-compound-flow.git
cd building-compound-flow
```

### 2. Install Dependencies
```bash
pip install mira-sdk python-dotenv
```

### 3. Configure the API Key
- Create a `.env` file in the root of the project:
  ```bash
  touch .env
  ```
- Add your Mira Marketplace API key to the `.env` file:
  ```plaintext
  API_KEY=your_api_key_here
  ```

### 4. Run the Example Scripts
Run the example scripts for creating, executing, and managing compound flows:
```bash
python test-local.py
python deploy-flow.py
```

---

## **Usage**

### Example Input
The script allows you to define compound flows by combining multiple sub-flows. For example:
```python
input_data = {
    "content": sample_content,
    "content-type": "medium blog",
    "tone": "professional & authentic"
}
```

### Example Output
The output of the compound flow execution will be printed in the terminal:
```plaintext
{'result': {'report': 'Detailed user insights report'}}
```

---

## **Project Structure**
```plaintext
.
├── flow.yaml                       #  A YAML file describing your copound flow
├── test-local.py                   # Script to test the flow locally
├── deploy-flow.py                  # Script to deploy the flow in the marketplace
├── .env                            # Environment variables file (not tracked in Git)
├── .env.example                    # Example environment variables file
├── README.md                       # Project documentation
├── compound flow workflow.png      # Workflow diagram of the sample compound flow
```

---

## **How It Works**
1. The `MiraClient` is initialized with an API key from the `.env` file.
2. **Create Compound Flow**: The `flow.yaml` script demonstrates how to define a new compound flow.
3. **Execute Compound Flow**: The `test-local.py` script shows how to execute the compound flow with dynamic input data locally.
4. **Manage Compound Flows**: The `deploy-flow.py` script deploys the compound flow on the marketplace.

---

## **Dependencies**
- **[mira-sdk](https://pypi.org/project/mira-sdk/)**: To interact with the Mira Marketplace.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: To securely load environment variables.

Install all dependencies with:
```bash
pip install mira-sdk python-dotenv
```

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Commit your changes.
4. Push the branch and open a pull request.

---

## **Contact**
If you have any questions or feedback, feel free to open an issue or contact [B-Venkatesh7210](https://github.com/B-Venkatesh7210).
