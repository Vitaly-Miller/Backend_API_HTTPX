"""
Books
https://simple-books-api.click/books
"""
from api.base_api import BaseAPI

#=======================================================================================================================
class Books(BaseAPI):
    # 𝌆 DATA:
    ENDPOINT = '/books'


    # ==================================================== ✨HELPERS ===================================================
    def list_of_books(self):
        return self.get(self.ENDPOINT)

    def get_book(self, book_id):
        return self.get(f'{self.ENDPOINT}/{book_id}')
