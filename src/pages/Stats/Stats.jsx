import { useBooks } from '../../context/BookContext'
import useBookStats from '../../hooks/useBookStats'
import './Stats.css'

function Stats() {
  const { books } = useBooks()
  const stats = useBookStats(books)

  return (
    <div className="stats">
      <h2>My Reading Stats 📊</h2>
      <div className="stats-grid">
        <div className="stat-card total"><span className="stat-num">{stats.total}</span><span className="stat-label">Total Koleksi</span></div>
        <div className="stat-card milik"><span className="stat-num">{stats.milik}</span><span className="stat-label">Udah Punya</span></div>
        <div className="stat-card baca"><span className="stat-num">{stats.baca}</span><span className="stat-label">Lagi Dibaca</span></div>
        <div className="stat-card beli"><span className="stat-num">{stats.beli}</span><span className="stat-label">Wishlist</span></div>
      </div>
    </div>
  )
}

export default Stats