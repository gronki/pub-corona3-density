module xztrin21_wrap
  implicit none
contains
  impure elemental subroutine opacity_table(abuX, abuZ, rho, T, kap, errno)
    real, intent(in) :: abuX, abuZ, rho, T
    real, intent(out) :: kap
    integer, intent(out), optional :: errno

    real :: opact, dopact, dopacr, dopactd
    integer :: opaerr
    common/e/ opact, dopact, dopacr, dopactd, opaerr

    character(len = 256) :: tabfn
    common/extra/ tabfn

    tabfn = "GN93hz"
    tabfn = "OP.tab"

    kap = 0
    call opacgn93(abuZ, abuX, T / 1e6, rho / (T / 1e6)**3)
    if (opaerr /= 0) kap = opact
    if (present(errno)) errno = opaerr
  end subroutine
end module

program optest

  use xztrin21_wrap

  implicit none
  real, parameter :: abuX = 0.7, abuZ = 0.05
  integer :: i, j
  integer, parameter :: n = 200
  real :: kap1, kap2, rho(n), T(n)
  character(len = 128) :: fn

  do i = 1, n
    rho(i) = 10**li(-14.75, 4.0, i, n)
  end do

  open(31, file = 'table-rho.txt', action = 'write')
  write (31, '(f10.3)') log10(rho)
  close(31)

  do i = 1, n
    T(i) = 10**li(3.75, 9.5, i, n)
  end do

  open(32, file = 'table-T.txt', action = 'write')
  write (32, '(f10.3)') log10(T)
  close(32)

  open(33, file = 'table.txt', action = 'write')
  do i = 1, n
    write (fn, '("test.", i0.3 ,".txt")') i
    open(34, file = fn, action = 'write')
    do j = 1, n
      call opacity_table(abuX, abuZ, rho(i), T(j), kap1)
      call opacity_anal(abuX, abuZ, rho(i), T(j), kap2)
      if (kap1 == 0) cycle
      write (33, '(2i5,4f10.4)') i, j, log10(rho(i)), log10(T(j)), kap1, log10(kap2)
      write (34, '(2i5,4f10.4)') i, j, log10(rho(i)), log10(T(j)), kap1, log10(kap2)
    end do
    close(34)
  end do
  close(33)

contains

  elemental real function li(lo, hi, i, n) result(y)
    integer, intent(in) :: i, n
    real, intent(in) :: lo, hi
    y = lo + (hi - lo) * (i - 1) / real(n - 1)
  end function

  elemental subroutine opacity_anal(abuX, abuZ, rho, T, kap)
    real, intent(in) :: abuX, abuZ, rho, T
    real, intent(out) :: kap
    real :: kes, kbff, kcut1, kcut2, kff0, kbf0

    kff0 = 3.68d22 * (1 - abuZ) * (1 + abuX)
    kbf0 = 4.34d25 * abuZ * (1 + abuX)
    kbff = (kff0 + kbf0) * rho * T**(-3.5)

    kes = 0.2 * (1 + abuX) !/ ((1 + (T / 4.5e8)**0.86) * (1 + 2.7e11 * rho / T**2))

    kcut1 = 32 * (rho / 2e-9)**0.2 * (T / 1e4)**12
    kcut2 = 64 * (rho / 2e-9)**0.2 * (T / 1e4)**5

    kap = kbff / (1 ) + kes ! + kbff / kcut1 + kbff / kcut2
  end subroutine

end program optest
