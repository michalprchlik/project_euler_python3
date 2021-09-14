multiples_of_3_or_5:
	podman build -f multiples_of_3_or_5/Containerfile -t multiples_of_3_or_5 multiples_of_3_or_5/
	podman run --rm localhost/multiples_of_3_or_5		
