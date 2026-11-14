import PropTypes from 'prop-types'
import './BookList.css'

const statusLabel = { milik: 'Udah Punya', baca: 'Lagi Dibaca', beli: 'Wishlist' }

function BookList({ books, onEdit, onDelete }) {
  if (books.length === 0) {
    return <p className="empty-msg">Rak buku lu masih kosong nih 🥲. Yuk isi!</p>
  }

  return (
    <div className="book-list">
      {books.map((book) => (
        <div key={book.id} className={`book-card ${book.status}`}>
          <div className="book-info">
            <h3>{book.judul}</h3>
            <p className="author">{book.penulis}</p>
            <span className={`badge ${book.status}`}>{statusLabel[book.status]}</span>
          </div>
          <div className="book-actions">
            <button onClick={() => onEdit(book)}>Edit</button>
            <button className="danger" onClick={() => onDelete(book.id)}>Hapus</button>
          </div>
        </div>
      ))}
    </div>
  )
}

BookList.propTypes = {
  books: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      judul: PropTypes.string.isRequired,
      penulis: PropTypes.string.isRequired,
      status: PropTypes.oneOf(['milik', 'baca', 'beli']).isRequired,
    })
  ).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
}

export default BookList