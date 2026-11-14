import PropTypes from 'prop-types'
import './BookFilter.css'

function BookFilter({ filter, search, onFilterChange, onSearchChange }) {
  return (
    <div className="book-filter">
      <input
        type="text"
        placeholder="Cari buku inceran lu... 🔍"
        value={search}
        onChange={(e) => onSearchChange(e.target.value)}
        className="search-input"
      />
      <div className="filter-buttons">
        <button className={filter === 'semua' ? 'active' : ''} onClick={() => onFilterChange('semua')}>Semua</button>
        <button className={filter === 'milik' ? 'active' : ''} onClick={() => onFilterChange('milik')}>Udah Punya</button>
        <button className={filter === 'baca' ? 'active' : ''} onClick={() => onFilterChange('baca')}>Lagi Dibaca</button>
        <button className={filter === 'beli' ? 'active' : ''} onClick={() => onFilterChange('beli')}>Wishlist</button>
      </div>
    </div>
  )
}

BookFilter.propTypes = {
  filter: PropTypes.string.isRequired,
  search: PropTypes.string.isRequired,
  onFilterChange: PropTypes.func.isRequired,
  onSearchChange: PropTypes.func.isRequired,
}

export default BookFilter