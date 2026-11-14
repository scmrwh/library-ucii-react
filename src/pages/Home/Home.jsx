import { useState, useMemo } from 'react'
import { useBooks } from '../../context/BookContext'
import BookForm from '../../components/BookForm/BookForm'
import BookList from '../../components/BookList/BookList'
import BookFilter from '../../components/BookFilter/BookFilter'
import './Home.css'

function Home() {
  const { books, addBook, updateBook, deleteBook } = useBooks()
  const [filter, setFilter] = useState('semua')
  const [search, setSearch] = useState('')
  const [editingBook, setEditingBook] = useState(null)

  const filteredBooks = useMemo(() => {
    return books
      .filter((b) => filter === 'semua' || b.status === filter)
      .filter((b) => b.judul.toLowerCase().includes(search.toLowerCase()) || b.penulis.toLowerCase().includes(search.toLowerCase()))
  }, [books, filter, search])

  const handleSubmit = (form) => {
    if (editingBook) {
      updateBook(editingBook.id, form)
      setEditingBook(null)
    } else {
      addBook(form)
    }
  }

  const handleDelete = (id) => {
    if (window.confirm('Yakin nih mau ngehapus buku ini? 🥺')) deleteBook(id)
  }

  return (
    <div className="home">
      <BookForm editingBook={editingBook} onSubmit={handleSubmit} onCancel={() => setEditingBook(null)} />
      <BookFilter filter={filter} search={search} onFilterChange={setFilter} onSearchChange={setSearch} />
      <p className="result-count">Nemu {filteredBooks.length} buku nih ✨</p>
      <BookList books={filteredBooks} onEdit={setEditingBook} onDelete={handleDelete} />
    </div>
  )
}

export default Home