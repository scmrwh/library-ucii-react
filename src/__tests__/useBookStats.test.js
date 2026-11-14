import { renderHook } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import useBookStats from '../hooks/useBookStats'

describe('useBookStats', () => {
  it('hitung statistik', () => {
    const { result } = renderHook(() => useBookStats([{ status: 'milik' }, { status: 'baca' }]))
    expect(result.current.total).toBe(2)
    expect(result.current.milik).toBe(1)
  })
})

