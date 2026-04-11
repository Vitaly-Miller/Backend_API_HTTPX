"""
Books
https://simple-books-api.click/books
"""
from client.api_client import APIClient

#=======================================================================================================================
class Books(APIClient):
    # 𝌆 DATA:
    ENDPOINT = '/books'


    # ==================================================== ✨HELPERS ===================================================
    def list_of_books(self):
        return self.get(self.ENDPOINT)

    def get_book(self, book_id):
        return self.get(f'{self.ENDPOINT}/{book_id}')
