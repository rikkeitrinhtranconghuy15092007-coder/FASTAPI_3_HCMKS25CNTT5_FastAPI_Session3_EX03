from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Python Basic", "author": "Nguyen Van A", "category": "programming", "year": 2022, "is_available": True},
    {"id": 2, "title": "Web API Design", "author": "Tran Van B", "category": "web", "year": 2021, "is_available": False},
    {"id": 3, "title": "Database System", "author": "Le Minh C", "category": "database", "year": 2020, "is_available": True},
    {"id": 4, "title": "Clean Code", "author": "Le Anh D", "category": "programming", "year": 2008, "is_available": False},
    {"id": 5, "title": "Computer Network", "author": "Vu Hong V", "category": "network", "year": 2019, "is_available": True},
    {"id": 6, "title": "FastAPI Basic", "author": "Nguyen Van A", "category": "web", "year": 2023, "is_available": True}
]

# API 1: Thống kê số lượng
@app.get("/books/statistics")
def get_statistics():
    total = len(books)
    available = len([b for b in books if b["is_available"] == True])
    borrowed = total - available
    return {
        "total_books": total,
        "available_books": available,
        "borrowed_books": borrowed
    }

# API 2: Lấy danh sách thể loại không trùng lặp
@app.get("/books/categories")
def get_categories():
    # Dùng set() để lọc trùng tự động, sau đó chuyển lại thành list
    categories = list(set(b["category"] for b in books))
    return {"categories": categories}

# API 3: Lấy cuốn sách mới nhất
@app.get("/books/latest")
def get_latest_book():
    if not books:
        return {"message": "No books available"}
    
    # Dùng hàm max() với key là giá trị 'year'
    latest_book = max(books, key=lambda b: b["year"])
    return latest_book