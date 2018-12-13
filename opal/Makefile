FC = gfortran
FFLAGS = -g -O3 -march=native

%.o: %.f
	$(FC) $(FFLAGS) -c $< -o $@

%.o: %.f90
	$(FC) $(FFLAGS) -c $< -o $@

optest: xztrin21.o optest.f90
	$(FC) $(FFLAGS) $^ -o $@
