import { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import './BookForm.css'

const emptyForm = { judul: '', penulis: '', status: 'milik' }

function BookForm({ editingBook, onSubmit, onCancel }) {
  const [form, setForm] = useState(emptyForm)
  const [errors, setErrors] = useState({})

  useEffect(() => {
    if (editingBook) {
      setForm({ judul: editingBook.judul, penulis: editingBook.penulis, status: editingBook.status })
    } else {
      setForm(emptyForm)
    }
    setErrors({})
  }, [editingBook])

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm((prev) => ({ ...prev, [name]: value }))
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: '' }))
    }
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const newErrors = {}
    if (!form.judul.trim()) newErrors.judul = 'Hayy Judulnya jangan kosong!'
    if (!form.penulis.trim()) newErrors.penulis = 'Penulisnya siapa?'

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors)
      return
    }

    onSubmit(form)
    setForm(emptyForm)
    setErrors({})
  }

  return (
    <form className="book-form" onSubmit={handleSubmit} noValidate>
      <h2>{editingBook ? 'Edit Buku Nih ✨' : 'Input Buku Baru 📝'}</h2>

      <div className="form-group">
        <label>Judul Buku</label>
        <input
          type="text"
          name="judul"
          value={form.judul}
          onChange={handleChange}
          className={errors.judul ? 'error' : ''}
          placeholder="Mau baca apa nih?"
        />
        {errors.judul && <span className="error-msg">{errors.judul}</span>}
      </div>

      <div className="form-group">
        <label>Penulis</label>
        <input
          type="text"
          name="penulis"
          value={form.penulis}
          onChange={handleChange}
          className={errors.penulis ? 'error' : ''}
          placeholder="Siapa authornya?"
        />
        {errors.penulis && <span className="error-msg">{errors.penulis}</span>}
      </div>

      <div className="form-group">
        <label>Status</label>
        <select name="status" value={form.status} onChange={handleChange}>
          <option value="milik">Udah Punya</option>
          <option value="baca">Lagi Dibaca</option>
          <option value="beli">Wishlist</option>
        </select>
      </div>

      <div className="form-actions">
        <button type="submit" className="btn-primary">
          {editingBook ? 'Simpen Perubahan 💾' : 'Ayo Tambahin! 🚀'}
        </button>
        {editingBook && (
          <button type="button" className="btn-secondary" onClick={onCancel}>
            Batalin
          </button>
        )}
      </div>
    </form>
  )
}

BookForm.propTypes = {
  editingBook: PropTypes.shape({
    id: PropTypes.number,
    judul: PropTypes.string,
    penulis: PropTypes.string,
    status: PropTypes.oneOf(['milik', 'baca', 'beli']),
  }),
  onSubmit: PropTypes.func.isRequired,
  onCancel: PropTypes.func,
}

export default BookForm