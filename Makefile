multiples_of_3_or_5:
	echo $@
	podman build -f Containerfile -t $@ $@/
	podman run --rm localhost/$@		

even_fibonacci_numbers:
	echo $@
	podman build -f Containerfile -t $@ $@/
	podman run --rm localhost/$@
	
largest_prime_factor:
	echo $@
	podman build -f Containerfile -t $@ $@/
	podman run --rm localhost/$@	