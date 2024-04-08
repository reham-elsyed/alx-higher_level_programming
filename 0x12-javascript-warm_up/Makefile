.PHONY: all test push

all: test push

test: FILES ?= $(filter-out $@,$(MAKECMDGOALS))
test:
	@echo "Running Semistandard on $(FILES)..."
	npx semistandard $(FILES)

push:
	@echo "Pushing to GitHub..."
	git add .
	git commit -m "Automated commit"
	git push

chmod:
	@echo "Changing file permissions..."
	chmod +x script.js

