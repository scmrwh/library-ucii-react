import { render, screen, fireEvent } from '@testing-library/react'
import { describe, it, expect, vi } from 'vitest'
import BookFilter from '../components/BookFilter/BookFilter'

describe('BookFilter', () => {
  it('klik filter', () => {
    const handleFilter = vi.fn()
    render(<BookFilter filter="semua" search="" onFilterChange={handleFilter} onSearchChange={() => {}} />)
    fireEvent.click(screen.getByText('Lagi Dibaca'))
    expect(handleFilter).toHaveBeenCalledWith('baca')
  })
})