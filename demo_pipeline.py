from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ExpenseItem:
    category: str
    amount: float
    comment: Optional[str] = None

@dataclass
class ShiftData:
    date: str
    cash_revenue: Optional[float]
    card_revenue: Optional[float]
    expenses: List[ExpenseItem]

def process_document_demo(filename: str) -> ShiftData:
    '''
    Showcase stub.

    The private version sends an image to an AI model,
    receives structured output, validates it and prepares
    the result for Excel export.
    '''
    return ShiftData(
        date="2026-09-18",
        cash_revenue=125000.0,
        card_revenue=310000.0,
        expenses=[
            ExpenseItem("supplies", 3200.0, "demo expense"),
            ExpenseItem("transport", 1400.0, "demo expense"),
        ],
    )

if __name__ == "__main__":
    print(process_document_demo("sample_receipt.jpg"))
