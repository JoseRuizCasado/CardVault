# CardVault

**CardVault** is an open-source Magic: The Gathering TCG collection manager, built with FastAPI.

> **Note:** This project is licensed under [CC BY-NC 4.0](LICENSE). Commercial use is strictly prohibited.

## Features (MVP 0.0)

- CardVault API built with FastAPI
- Clean, collaborative project structure
- Basic `/` endpoint for health-check/welcome
- Ready for further development and contribution

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

```bash
# Clone this repository
git clone https://github.com/<your-username>/cardvault.git
cd cardvault

# Create virtual environment and activate it
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


# Running the development server
uvicorn app.main:app --reload
```

### Project Structure
```bash
cardvault/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── routers/
│        └── __init__.py
├── .gitignore
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── requirements.txt
```
### Contributing
All contributions are welcome! Please read [CONTRIBUTING.md](/CONTRIBUTING.md) for guidelines.

Open an issue or propose a pull request for improvements or bug fixes.
For new features or large changes, please discuss in the corresponding issue first.
Use feature branches and link your PRs to issues with `Closes #issue_number`.

### License
This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) .
You may not use this code for commercial purposes.

*This README will be updated as the project evolves.*


