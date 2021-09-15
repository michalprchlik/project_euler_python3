build:
	echo $(DIRECTORY)
	podman build -f Containerfile -t $(DIRECTORY) $(DIRECTORY)/
	podman run --rm localhost/$(DIRECTORY)