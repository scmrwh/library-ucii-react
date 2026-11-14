import { Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home/Home'
import Stats from './pages/Stats/Stats'
import { BookProvider } from './context/BookContext'
import './App.css'

function App() {
  return (
    <BookProvider>
      <div className="app">
        <header className="navbar">
          <h1>📚 Library Ucii</h1>
          <nav>
            <Link to="/">Rak Buku</Link>
            <Link to="/stats">Pencapaian</Link>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/stats" element={<Stats />} />
          </Routes>
        </main>
      </div>
    </BookProvider>
  )
}

export default App