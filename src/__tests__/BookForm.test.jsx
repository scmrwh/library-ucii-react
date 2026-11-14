import { render, screen, fireEvent } from '@testing-library/react'
import { describe, it, expect, vi } from 'vitest'
import BookForm from '../components/BookForm/BookForm'

describe('BookForm', () => {
  it('validasi error kosong', () => {
    render(<BookForm onSubmit={() => {}} />)
    fireEvent.click(screen.getByText('Ayo Tambahin! 🚀'))
    
    expect(screen.getByText('Hayy Judulnya jangan kosong!')).toBeInTheDocument()
    expect(screen.getByText('Penulisnya siapa?')).toBeInTheDocument()
  })
  
  it('submit data valid', () => {
    const handleSubmit = vi.fn()
    render(<BookForm onSubmit={handleSubmit} />)
    fireEvent.change(screen.getByPlaceholderText('Mau baca apa nih?'), { target: { value: 'Laskar Pelangi' } })
    fireEvent.change(screen.getByPlaceholderText('Siapa authornya?'), { target: { value: 'Andrea' } })
    fireEvent.click(screen.getByText('Ayo Tambahin! 🚀'))
    expect(handleSubmit).toHaveBeenCalled()
  })
})