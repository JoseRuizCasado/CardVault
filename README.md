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
## 📊 Data Model

CardVault's data model is designed to be flexible, scalable, and support collection management, multi-owner capability, loan/renting operations, and deck composition with accurate tracking of inventory and transactions.

---

### **Entities**

---

#### **User**
- `id`: *int* — Unique identifier for the user.
- `username`: *str* — User's display name.
- `email`: *str* — User's email address.
- `full_name`: *str* - User's full name.
- `phone_number`: *str* - User's telephone number.
- `role`: *str* - User's role in the application.

---

#### **Card**
- `id`: *int* — This is a unique card identifier. It consists of the expansion code and the collection number.
- `name`: *str* — Card name.
- `color`: *enum* — One of: `white`, `blue`, `black`, `red`, `green`, `colorless`, `multicolor`.
- *(other optional fields: set, rarity, edition, etc.)*

---

#### **CollectionEntry**
Represents a user's (or owner's) actual owned copies of a specific card.  
- `id`: *int* — Unique identifier for the collection entry.
- `card_id`: *int* — Reference to `Card`.
- `owner_id`: *int* — Reference to `User` (or owner entity).
- `amount`: *int* — Number of owned (available + loaned) copies of this card.
- `for_sale`: *bool* — Whether these copies are marked for sale/renting.
- `price_bought`: *float* — Purchase price (optional, per owner).
- *(optional: condition, language, etc.)*

---

#### **Deck**
- `id`: *int* — Unique identifier for the deck.
- `name`: *str* — Deck name.
- `owner_id`: *int* — Reference to `User`.
- `description`: *str* — Optional description field.

---

#### **DeckEntry**
Relates a deck with cards in a user's collection, tracking the number of copies of each card in the deck.
- `id`: *int* — Unique identifier for the deck entry.
- `deck_id`: *int* — Reference to `Deck`.
- `collection_entry_id`: *int* — Reference to `CollectionEntry`.
- `amount`: *int* — Number of copies of the card present in the deck.
- *(optional: is_sideboard: bool)*

---

#### **Loan**
Represents a transaction where a user (borrower) rents/borrows cards or a deck.
- `id`: *int* — Unique identifier for the loan.
- `borrower_id`: *int* — Reference to the borrowing user.
- `owner_id`: *int* — Owner/lender of the cards/deck.
- `deck_id`: *int | null* — Reference to `Deck`, if the loan is for an entire deck (or null if only cards are loaned).
- `start_date`: *date* — Date the transaction starts.
- `end_date`: *date* — Expected return date.
- `status`: *str* — Status indicator: `'pending'`, `'active'`, `'returned'`, `'overdue'`, etc.
- `notes`: *str* — Optional notes on the loan.

---

#### **LoanItem**
Represents a specific card (or group of N copies) included in a loan.
- `id`: *int* — Unique identifier for the loan item.
- `loan_id`: *int* — Reference to the `Loan`.
- `collection_entry_id`: *int* — Reference to `CollectionEntry` of the loaned card.
- `amount`: *int* — Number of copies being loaned (for each card in the loan).

---

### **Entity/Relationship Diagram (text version)**
User 1---* CollectionEntry ---1 Card
1--- Deck
1---* Loan

Deck 1---* DeckEntry *---1 CollectionEntry

Loan 1---* LoanItem *---1 CollectionEntry

Loan (deck_id)---0..1 Deck


---

### **How it works**

- **A Card** = the card definition, e.g., "Lightning Bolt"
- **A CollectionEntry** = "I own 8 Lightning Bolt cards"
- **A Deck** = composition by a user of cards, via CollectionEntries
- **A DeckEntry** = "this deck has 4 Lightning Bolt from my collection"
- **A Loan** = "User A lent (or rented) these cards/decks to User B"
- **A LoanItem** = "In this loan, 2 Lightning Bolt (collection_entry) were loaned"
- All quantities and ownership are explicit and auditable.

---

### **Card color enum (allowed values):**
- `white`
- `blue`
- `black`
- `red`
- `green`
- `colorless`
- `multicolor`

---

> For detailed attribute definitions and table relationships, refer to the individual model docstrings.

## Contributing
All contributions are welcome! Please read [CONTRIBUTING.md](/CONTRIBUTING.md) for guidelines.

Open an issue or propose a pull request for improvements or bug fixes.
For new features or large changes, please discuss in the corresponding issue first.
Use feature branches and link your PRs to issues with `Closes #issue_number`.

### License
This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) .
You may not use this code for commercial purposes.

*This README will be updated as the project evolves.*


