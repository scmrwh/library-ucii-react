import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import BookList from '../components/BookList/BookList'

describe('BookList', () => {
  it('render buku', () => {
    render(<BookList books={[{ id: 1, judul: 'Buku A', penulis: 'Penulis A', status: 'milik' }]} onEdit={() => {}} onDelete={() => {}} />)
    expect(screen.getByText('Buku A')).toBeInTheDocument()
  })
  it('pesan kosong', () => {
    render(<BookList books={[]} onEdit={() => {}} onDelete={() => {}} />)
    expect(screen.getByText(/Rak buku lu masih kosong nih/i)).toBeInTheDocument()
  })
})