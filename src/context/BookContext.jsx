import { createContext, useContext } from 'react'
import PropTypes from 'prop-types'
import useLocalStorage from '../hooks/useLocalStorage'

const BookContext = createContext()

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('bukuku_books', [])

  const addBook = (book) => setBooks((prev) => [...prev, { ...book, id: Date.now() }])
  const updateBook = (id, data) => setBooks((prev) => prev.map((b) => (b.id === id ? { ...b, ...data } : b)))
  const deleteBook = (id) => setBooks((prev) => prev.filter((b) => b.id !== id))

  return (
    <BookContext.Provider value={{ books, addBook, updateBook, deleteBook }}>
      {children}
    </BookContext.Provider>
  )
}

BookProvider.propTypes = { children: PropTypes.node.isRequired }

export function useBooks() {
  const ctx = useContext(BookContext)
  if (!ctx) throw new Error('useBooks harus dipakai di dalam BookProvider')
  return ctx
}